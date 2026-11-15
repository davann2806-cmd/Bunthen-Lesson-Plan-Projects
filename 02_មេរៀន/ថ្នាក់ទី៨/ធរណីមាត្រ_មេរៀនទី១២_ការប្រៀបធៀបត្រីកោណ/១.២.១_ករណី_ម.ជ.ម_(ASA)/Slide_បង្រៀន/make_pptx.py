"""PDF (beamer) -> per-page SVG -> animated PPTX.

Every beamer frame becomes ONE PowerPoint slide.  Overlay pages of the same
frame become click-triggered fade-in layers: for each page the pixels that
changed w.r.t. the previous page are found, grouped into regions and each
region is placed on the slide as an (opaque) cropped SVG picture that fades in.
"""
import re, subprocess, io, sys, copy
from pathlib import Path
import numpy as np
import fitz
from PIL import Image
from lxml import etree
from pptx import Presentation
from pptx.util import Emu
from pptx.opc.package import Part
from pptx.opc.packuri import PackURI
from pptx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT = Path(__file__).parent
PDF = ROOT / "main.pdf"
OUT = ROOT / "out"
SVGDIR = OUT / "svg"
SVGDIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- frames
nav = (ROOT / "main.nav").read_text(encoding="utf-8", errors="ignore")
frames = [(int(a), int(b)) for a, b in re.findall(r"\\beamer@framepages \{(\d+)\}\{(\d+)\}", nav)]
npages = fitz.open(PDF).page_count
print("frames:", len(frames), "pages:", npages)

# ---------------------------------------------------------------- SVG per page
def page_svg(n):
    p = SVGDIR / f"page_{n:03d}.svg"
    if not p.exists():
        subprocess.run(["pdftocairo", "-svg", "-f", str(n), "-l", str(n), str(PDF), str(p)], check=True)
    return p

for n in range(1, npages + 1):
    page_svg(n)
print("svg done")

# ---------------------------------------------------------------- raster for diffing / fallback
doc = fitz.open(PDF)
W_PT, H_PT = doc[0].rect.width, doc[0].rect.height
DIFF_S, PNG_S = 2.0, 1.5

def render(n, scale, clip=None):
    pix = doc[n - 1].get_pixmap(matrix=fitz.Matrix(scale, scale), clip=clip, alpha=False)
    return pix

def small_png(pix):
    """palette-quantized fallback (only used by apps without SVG support)"""
    im = Image.frombytes("RGB", (pix.w, pix.h), pix.samples).quantize(64, dither=Image.Dither.NONE)
    b = io.BytesIO(); im.save(b, "PNG", optimize=True)
    return b.getvalue()

def arr(n):
    pix = render(n, DIFF_S)
    return np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.w, pix.n).astype(np.int16)

BLOCK = 12  # px grid for clustering

def regions(a, b):
    """bounding boxes (px, at DIFF_S) of changed areas between page images a and b."""
    d = (np.abs(a - b).max(axis=2) > 10)
    if not d.any():
        return []
    H, W = d.shape
    gh, gw = -(-H // BLOCK), -(-W // BLOCK)
    g = np.zeros((gh, gw), bool)
    ys, xs = np.nonzero(d)
    g[ys // BLOCK, xs // BLOCK] = True
    # dilate by 2 cells so nearby changes (glyph + label) join
    gd = g.copy()
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            gd |= np.roll(np.roll(g, dy, 0), dx, 1)
    lab = np.zeros(g.shape, int); k = 0; boxes = []
    for y in range(gh):
        for x in range(gw):
            if gd[y, x] and not lab[y, x]:
                k += 1; st = [(y, x)]; lab[y, x] = k
                while st:
                    cy, cx = st.pop()
                    for ny, nx in ((cy+1,cx),(cy-1,cx),(cy,cx+1),(cy,cx-1)):
                        if 0 <= ny < gh and 0 <= nx < gw and gd[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = k; st.append((ny, nx))
    for i in range(1, k + 1):
        m = (lab == i)
        # tight box from the real changed pixels that fall in this cluster
        mm = np.kron(m & g, np.ones((BLOCK, BLOCK), bool))[:H, :W] & d
        if not mm.any():
            continue
        yy, xx = np.nonzero(mm)
        boxes.append([xx.min(), yy.min(), xx.max() + 1, yy.max() + 1])
    # pad + merge overlapping
    pad = 6
    boxes = [[max(0, x0-pad), max(0, y0-pad), min(W, x1+pad), min(H, y1+pad)] for x0, y0, x1, y1 in boxes]
    merged = True
    while merged:
        merged = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                A, B = boxes[i], boxes[j]
                if A[0] < B[2] and B[0] < A[2] and A[1] < B[3] and B[1] < A[3]:
                    boxes[i] = [min(A[0],B[0]), min(A[1],B[1]), max(A[2],B[2]), max(A[3],B[3])]
                    del boxes[j]; merged = True; break
            if merged: break
    return sorted(boxes, key=lambda b: (b[0], b[1]))

# ---------------------------------------------------------------- SVG cropping
_num = re.compile(r"(-?\d*\.\d{4,})")
_use = re.compile(r'<use\b[^>]*?/>')
_xf = re.compile(r'matrix\(([-\d.e]+),[-\d.e]+,[-\d.e]+,([-\d.e]+),([-\d.e]+),([-\d.e]+)\)')

def slim_svg(s, w, h):
    """Vector-preserving shrink: cull glyphs outside the picture, drop unused
    glyph outlines, strip text metadata, round coordinates to 3 decimals."""
    def keep(m):
        u = m.group(0)
        t = _xf.search(u)
        if not t:
            return u
        a, d, e, f = (float(v) for v in t.groups())
        sz = abs(a) or 1
        return u if (-2*sz <= e <= w + 2*sz and -2*sz <= f <= h + 2*sz) else ""
    s = _use.sub(keep, s)
    s = re.sub(r'\sdata-text="[^"]*"', "", s)
    cut = s.find("</defs>")
    head, body = s[:cut], s[cut:]
    used = set(re.findall(r'xlink:href="#([^"]+)"', body))
    head = re.sub(r'<path id="([^"]+)"[^>]*?/>\s*',
                  lambda m: m.group(0) if m.group(1) in used else "", head)
    return _num.sub(lambda m: f"{float(m.group(1)):.3f}".rstrip("0").rstrip("."), head + body)

def crop_svg(n, x0, y0, w, h, dst):
    """MuPDF SVG of just the crop box (glyphs as outlines, so no fonts needed)."""
    pg = doc[n - 1]
    pg.set_cropbox(fitz.Rect(x0, y0, x0 + w, y0 + h))
    svg = pg.get_svg_image(text_as_path=True)
    pg.set_cropbox(pg.mediabox)
    dst.write_text(slim_svg(svg, w, h), encoding="utf-8")

# ---------------------------------------------------------------- PPTX
prs = Presentation()
SW, SH = 12192000, 6858000
prs.slide_width, prs.slide_height = Emu(SW), Emu(SH)
blank = prs.slide_layouts[6]
EMU_PT = SW / W_PT
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
svg_counter = [0]

def add_svg_picture(slide, svg_path, png_bytes, left, top, width, height, name):
    pic = slide.shapes.add_picture(io.BytesIO(png_bytes), Emu(int(left)), Emu(int(top)), Emu(int(width)), Emu(int(height)))
    pic.name = name
    svg_counter[0] += 1
    part = Part(PackURI(f"/ppt/media/svgimg{svg_counter[0]}.svg"), "image/svg+xml",
                prs.part.package, svg_path.read_bytes())
    rid = slide.part.relate_to(part, RT.IMAGE)
    blip = pic._element.find(f".//{{{NS_A}}}blip")
    ext_lst = etree.SubElement(blip, f"{{{NS_A}}}extLst")
    ext = etree.SubElement(ext_lst, f"{{{NS_A}}}ext", uri="{96DAC541-7B7A-43D3-8B79-37D633B846F1}")
    sb = etree.SubElement(ext, "{http://schemas.microsoft.com/office/drawing/2016/SVG/main}svgBlip",
                          nsmap={"asvg": "http://schemas.microsoft.com/office/drawing/2016/SVG/main"})
    sb.set(f"{{{NS_R}}}embed", rid)
    return pic

def timing_xml(clicks):
    """clicks: list of lists of shape ids; each inner list fades in on one click."""
    nid = [2]
    def n():
        nid[0] += 1; return nid[0]
    body = []
    for ids in clicks:
        c1, c2 = n(), n()
        effs = []
        for k, sid in enumerate(ids):
            e, s_, a_ = n(), n(), n()
            node = "clickEffect" if k == 0 else "withEffect"
            effs.append(f'''<p:par><p:cTn id="{e}" presetID="1" presetClass="entr" presetSubtype="0" fill="hold" nodeType="{node}">
<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>
<p:set><p:cBhvr><p:cTn id="{s_}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
<p:tgtEl><p:spTgt spid="{sid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
<p:to><p:strVal val="visible"/></p:to></p:set></p:childTnLst></p:cTn></p:par>''')
        body.append(f'''<p:par><p:cTn id="{c1}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>
<p:par><p:cTn id="{c2}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{''.join(effs)}</p:childTnLst></p:cTn></p:par>
</p:childTnLst></p:cTn></p:par>''')
    return f'''<p:timing xmlns:p="{NS_P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>
<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>{''.join(body)}</p:childTnLst></p:cTn>
<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>
<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>
</p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'''

CROPDIR = OUT / "crops"; CROPDIR.mkdir(exist_ok=True)

for fi, (p0, p1) in enumerate(frames, 1):
    slide = prs.slides.add_slide(blank)
    # base layer: full first page
    png = small_png(render(p0, PNG_S))
    bsvg = CROPDIR / f"f{fi:02d}_p{p0:03d}_base.svg"
    crop_svg(p0, 0, 0, W_PT, H_PT, bsvg)
    base = add_svg_picture(slide, bsvg, png, 0, 0, SW, SH, f"f{fi}_p{p0}_base")
    clicks = []
    prev = arr(p0)
    for n in range(p0 + 1, p1 + 1):
        cur = arr(n)
        boxes = regions(prev, cur)
        prev = cur
        if not boxes:
            continue
        ids = []
        for bi, (x0, y0, x1, y1) in enumerate(boxes):
            px0, py0, px1, py1 = x0 / DIFF_S, y0 / DIFF_S, x1 / DIFF_S, y1 / DIFF_S   # points
            w, h = px1 - px0, py1 - py0
            dst = CROPDIR / f"f{fi:02d}_p{n:03d}_{bi}.svg"
            crop_svg(n, px0, py0, w, h, dst)
            png = small_png(render(n, PNG_S, clip=fitz.Rect(px0, py0, px1, py1)))
            pic = add_svg_picture(slide, dst, png, px0 * EMU_PT, py0 * EMU_PT, w * EMU_PT, h * EMU_PT,
                                  f"f{fi}_p{n}_{bi}")
            ids.append(pic.shape_id)
        clicks.append(ids)
    sld = slide._element
    if clicks:
        sld.append(etree.fromstring(timing_xml(clicks)))
    print(f"frame {fi}: pages {p0}-{p1}, clicks {len(clicks)}")

out = OUT / "lesson_ASA_small_v2.pptx"
prs.save(out)
print("saved", out, out.stat().st_size // 1024, "KB")
