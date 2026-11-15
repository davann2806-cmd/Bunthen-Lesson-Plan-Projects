# Standard 5-Stage Research-Driven NGS Lesson Package Pipeline

Use this workflow **before** authoring or upgrading any 50-minute NGS Khmer lesson package (`LS_Plan_<Topic>.tex`, `Teaching_Scenario_<Topic>.tex`, `Teaching_Guideline_<Topic>.tex`, `Printable_Materials_<Topic>.tex`, and `ឯកសារស្រាវជ្រាវយោង_PDF\`). It grounds every classroom task in verified peer-reviewed empirical evidence while strictly enforcing anti-CAPTCHA compliance, Black & White (B&W) print safety, true 1:1 scale manipulatives, and clean A4 page balance.

---

## Execution Modes (`/swarm` Parallel vs. Single-Agent)

### Option A: `/swarm` Parallel Mode (Recommended for Complete Lesson Packages)
1. **Stage 1 Literature Researchers** (sharing `03_ឯកសារស្រាវជ្រាវ\...\papers\`, each assigned a distinct filename prefix to prevent collisions):
   - `scholar-misconceptions` (`misconceptions_<year>_<firstauthor>.pdf`): Student misconceptions, cognitive obstacles, visual-prototype/orientation/overlapped-figure bias, tacit premises, diagram-mark curtailment, vertex-order errors, and conceptual confusions.
   - `scholar-activities` (`activities_<year>_<firstauthor>.pdf`): Hands-on manipulatives, dynamic geometry constraints, Predict–Observe–Explain (POE) tasks, embodied gestures with object-focused speech, cut-out/translucent overlay superposition, and real-world inquiry hooks fit for a 50-minute class.
   - `scholar-proof` (`proof_<year>_<firstauthor>.pdf`): Cognitive Load Theory / avoiding "proof shock", monochrome B&W print-safe symbolic diagram coding + bracketed finger-tracing prompts, numbered warrant banks, forward/backward planning (`P2`) + Looking Back (`EIA`), collaborative `Pause-Ask` / `Pause-Review` gates, and rapid diagnostic exit foils.
   - Optional `evidence-curator`: Curates targeted extra Open-Access papers (e.g., erroneous examples, realistic/historical indirect measurement), copies & numbers all verified PDFs into `ឯកសារស្រាវជ្រាវយោង_PDF\`, and generates `00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md`.
2. **Stages 2–5 Package Authors & Verifier**:
   - `lesson-author`: Updates/creates `Research_Brief_<Topic>.md`, `LS_Plan_<Topic>.tex` (4 pp.), and `Teaching_Scenario_<Topic>.tex` (2 pp.).
   - `printables-author`: Authors `Printable_Materials_<Topic>.tex` (1 kit per A4 page, true `1:1` scale manipulatives, B&W thick TikZ).
   - `guideline-author`: Authors `Teaching_Guideline_<Topic>.tex` (Word-styled manual & APA 7th mini-research report referencing exact verified PDFs, `LS_Plan`, and `Printable_Materials` pages).
   - `verifier` + `skill-pkg-updater`: Independently validates PDF integrity (`fitz`), compiles/inspects PNGs for every page, and keeps workspace/global skills in sync.

### Option B: Single-Agent Mode
Run the exact same 5 stages sequentially: gather and verify 5–14 Open-Access PDFs spanning misconceptions, manipulatives/POE, and proof scaffolding/assessment into `papers\`, populate `ឯកសារស្រាវជ្រាវយោង_PDF\`, draft `Research_Brief_<Topic>.md`, author all 4 synchronized `.tex` deliverables, double-compile each with `xelatex`, move explicit `.aux`/`.log`/`.out` artifacts, and visually inspect every rendered PNG page across all 4 PDFs.

---

## Stage 1 — Academic Literature, Verification & Attached Evidence Folder

### 1.1 Archive Locations
Save raw verified PDFs in the research tree, and mirror numbered copies inside each lesson folder (`ឯកសារស្រាវជ្រាវយោង_PDF\`):
```text
Research PDFs : C:\Users\KIT\Desktop\NGS Lesson Plan\03_ឯកសារស្រាវជ្រាវ\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\papers\
Attached Pack : C:\Users\KIT\Desktop\NGS Lesson Plan\01_កិច្ចតែងការបង្រៀន\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\ឯកសារស្រាវជ្រាវយោង_PDF\
```

### 1.2 Mandatory Anti-CAPTCHA & Compliance Rules
- **NEVER** scrape `scholar.google.com` directly using `curl`, `urllib`, `requests`, Selenium/Playwright, or headless browsers.
- **NEVER** solve, click through, wait out, compute, or bypass any CAPTCHA, Cloudflare Turnstile, proof-of-work gate, or paywall/login barrier.
- Discover literature strictly through:
  1. `search_web` tool (e.g., `domain:"scholar.google.com"`, `domain:"eric.ed.gov"`, `domain:"hal.science"`, `domain:"springer.com"`, `domain:"mdpi.com"`, `domain:"nctm.org"`).
  2. **OpenAlex API** (`filter=is_oa:true`)
  3. **ERIC API** (`files.eric.ed.gov/fulltext/<ID>.pdf`)
  4. **Semantic Scholar API** (`openAccessPdf`)
  5. **DOAJ** / legitimate open-access publisher repositories.
- If a candidate PDF URL returns HTML, HTTP 403/429, or a bot check, abort that URL immediately and pick another legitimate Open-Access mirror.

### 1.3 Ready-to-Run Zero-CAPTCHA Python Discovery & PDF Verification Snippets

Run these scripts from PowerShell (`python -c "..."` or a temporary script in `<scratch>` — never leave `.py` scripts inside `01_កិច្ចតែងការបង្រៀន` or `03_ឯកសារស្រាវជ្រាវ`):

```python
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
import fitz  # PyMuPDF

HEADERS = {"User-Agent": "NGSLessonResearch/1.0 (Academic Open-Access Discovery)"}


def fetch_json(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


# 1) OpenAlex Open-Access Search (filter=is_oa:true)
def search_openalex(query: str, per_page: int = 15) -> list[dict]:
    q = urllib.parse.quote_plus(query)
    url = f"https://api.openalex.org/works?search={q}&filter=is_oa:true&per-page={per_page}"
    data = fetch_json(url)
    results = []
    for w in data.get("results", []):
        best = w.get("best_oa_location") or {}
        primary = w.get("primary_location") or {}
        oa = w.get("open_access") or {}
        pdf_url = best.get("pdf_url") or primary.get("pdf_url") or oa.get("oa_url")
        if not pdf_url:
            for loc in w.get("locations", []):
                if loc.get("pdf_url"):
                    pdf_url = loc["pdf_url"]
                    break
        authors = [a["author"]["display_name"] for a in w.get("authorships", []) if a.get("author")]
        results.append({
            "source": "OpenAlex",
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "authors": authors[:4],
            "doi": w.get("doi"),
            "pdf_url": pdf_url,
        })
    return [r for r in results if r["pdf_url"]]


# 2) ERIC Search + Direct Fulltext PDF URLs
def search_eric(query: str, rows: int = 15) -> list[dict]:
    q = urllib.parse.quote_plus(query)
    url = f"https://api.ies.ed.gov/eric/?search={q}&rows={rows}&format=json"
    data = fetch_json(url)
    results = []
    for doc in data.get("response", {}).get("docs", []):
        eric_id = doc.get("id", "")
        if doc.get("e_fulltextauth") == 1 or eric_id.startswith("ED"):
            results.append({
                "source": "ERIC",
                "id": eric_id,
                "title": doc.get("title"),
                "year": doc.get("publicationdateyear"),
                "authors": doc.get("author", [])[:4],
                "pdf_url": f"https://files.eric.ed.gov/fulltext/{eric_id}.pdf",
            })
    return results


# 3) Semantic Scholar Open-Access Search
def search_semantic_scholar(query: str, limit: int = 10) -> list[dict]:
    q = urllib.parse.quote_plus(query)
    fields = "title,authors,year,venue,externalIds,abstract,openAccessPdf"
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={q}&limit={limit}&fields={fields}"
    try:
        data = fetch_json(url)
    except urllib.error.HTTPError as exc:
        print(f"[Semantic Scholar skipped HTTP {exc.code}]")
        return []
    results = []
    for p in data.get("data", []):
        oa_pdf = (p.get("openAccessPdf") or {}).get("url")
        if oa_pdf:
            results.append({
                "source": "SemanticScholar",
                "title": p.get("title"),
                "year": p.get("year"),
                "venue": p.get("venue"),
                "authors": [a.get("name") for a in p.get("authors", [])[:4]],
                "doi": (p.get("externalIds") or {}).get("DOI"),
                "pdf_url": oa_pdf,
            })
    return results


# 4) Mandatory PDF Download & Verification Gate (%PDF- + >=2 pages + >500 chars)
def download_and_verify_pdf(url: str, dest_path: str | Path) -> bool:
    out = Path(dest_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={**HEADERS, "Accept": "application/pdf,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
    except Exception as exc:
        print(f"FAIL download ({exc}): {url}")
        return False

    if raw[:5] != b"%PDF-":
        print(f"FAIL non-PDF header ({raw[:20]!r}): {url}")
        return False

    out.write_bytes(raw)
    passed = False
    pages, chars = 0, 0
    try:
        with fitz.open(str(out)) as doc:
            pages = len(doc)
            chars = sum(len(page.get_text("text")) for page in doc)
            passed = (pages >= 2 and chars > 500)
    except Exception as exc:
        print(f"FAIL fitz parse ({exc}): {out.name}")
        passed = False

    if not passed:
        if out.exists():
            os.remove(out)
        print(f"DELETED invalid/stub PDF ({pages} pp, {chars} chars): {out.name}")
        return False

    print(f"PASS {out.name}: {out.stat().st_size:,} B | {pages} pp | {chars:,} chars")
    return True
```

### 1.4 Reading Verified PDFs
After every file passes `download_and_verify_pdf`, inspect Page 1 and body text with `fitz` to confirm exact **APA 7th bibliographic metadata (authors, year, title, journal/conference, volume/issue/pages, DOI/URL)** as well as **sample sizes (`N`), statistical effects, student quotes, misconception patterns, and activity steps**. Never cite unverified abstracts or invent metrics.

### 1.5 Attached Lesson Evidence Folder (`ឯកសារស្រាវជ្រាវយោង_PDF\`)
Populate `01_កិច្ចតែងការបង្រៀន\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\ឯកសារស្រាវជ្រាវយោង_PDF\` directly inside the lesson deliverable folder:
1. Copy every verified PDF from `03_...\papers\` with sequential ASCII-safe filenames:
   `01_<AuthorYear_ShortTopic>.pdf`, `02_<AuthorYear_ShortTopic>.pdf`, ...
2. Re-run PyMuPDF (`fitz`) verification on all copied PDFs inside `ឯកសារស្រាវជ្រាវយោង_PDF\` (`b'%PDF-'`, `>=2` pp., `>500` chars).
3. Create `00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` inside `ឯកសារស្រាវជ្រាវយោង_PDF\` with a complete Khmer + English table matching **every APA 7th citation** used in `Teaching_Guideline_<Topic>.tex` 1-to-1:
   - Columns: `#` | `ឈ្មោះឯកសារ PDF (Filename)` | `APA 7th Citation` | `តួនាទីក្នុងមេរៀន 5Es (Activity Rationale)` | `ទំព័រ (Pages)` | `Source URL / DOI`

---

## Stage 2 — Pedagogical Synthesis (`Research_Brief_<Topic>.md`)

Save a single unified synthesis file at:
```text
03_ឯកសារស្រាវជ្រាវ\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\Research_Brief_<Topic>.md
```
Write the pedagogical narrative in clear **Khmer** while preserving **exact English APA 7th citations**, DOIs/URLs, and clickable relative links to `papers/<filename>.pdf`. Use this template:

```markdown
# សង្ខេបការស្រាវជ្រាវគរុកោសល្យ (Research Brief): <Topic> (<Grade>)

- **កញ្ចប់ឯកសារបង្រៀនគោលដៅ** (`01_កិច្ចតែងការបង្រៀន\...\`)៖
  - `LS_Plan_<Topic>.tex` (៥០ នាទី, គំរូ 5Es, ៤ ទំព័រ A4)
  - `Teaching_Scenario_<Topic>.tex` (២ ទំព័រ A4)
  - `Teaching_Guideline_<Topic>.tex` (សៀវភៅណែនាំគ្រូ & របាយការណ៍ស្រាវជ្រាវ APA 7th)
  - `Printable_Materials_<Topic>.tex` (សម្ភារៈបោះពុម្ព B&W 1:1 scale)
  - `ឯកសារស្រាវជ្រាវយោង_PDF\` (`00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` + `01_...pdf`..)

## ១. បញ្ជីឯកសារយោងដែលបានផ្ទៀងផ្ទាត់ (Verified Open-Access Sources)
| # | ឯកសារ PDF (`papers/`) | APA 7th Citation & DOI/URL | មុំស្រាវជ្រាវ |
|---|---|---|---|
| 1 | [misconceptions_2025_...](papers/misconceptions_2025_....pdf) | ... | Misconceptions |
| 2 | [activities_2023_...](papers/activities_2023_....pdf) | ... | Hands-on / POE |
| 3 | [proof_2019_...](papers/proof_2019_....pdf) | ... | Proof Scaffolding |

## ២. សំយោគភស្តុតាងជាក់ស្ដែង (Empirical Synthesis)
- **មុំទី១ — ការយល់ច្រឡំ និងឧបសគ្គការគិតរបស់សិស្ស**៖ (សង្ខេបទិន្នន័យ % / N និងកំហុសធំៗ)
- **មុំទី២ — ពិសោធន៍ផ្ទាល់ដៃ ចលនាកាយវិការ និង POE**៖ (សង្ខេបឧបករណ៍ និងប្រសិទ្ធភាព)
- **មុំទី៣ — ជំនួយកាត់បន្ថយបន្ទុកគិត (Cognitive Load), សញ្ញា B&W និងការវាយតម្លៃ**៖ (សង្ខេបទម្រង់គាំទ្រ)

## ៣. ផែនទីបម្លែងចូលក្នុងកិច្ចតែងការ ៥០ នាទី (5Es Mapping Table)
| ជំហាន / 5Es (នាទី) | បញ្ហាភស្តុតាងដែលត្រូវដោះស្រាយ | ការកែលម្អជាក់ស្ដែងក្នុងកញ្ចប់ ៤ ឯកសារ |
|---|---|---|
| E1 - Engage (3 min) | ទំនាក់ទំនងបញ្ហាពិត & POE hook | ... |
| E2 - Explore (11 min) | ពិសោធន៍ផ្ទាល់ដៃ (1:1 mat) + អន្ទាក់កំហុស + បំបែករូបដដែលៗ | ... |
| E3 - Explain (6 min) | លក្ខខណ្ឌកំណត់ + ធនាគារហេតុផល (`①–⑤`) | ... |
| E4 - Elaborate (10 min) | កាតស៊ើបអង្កេត B&W (`[tracing]`) + EIA Looking-Back | ... |
| E5 - Evaluate (10 min) | Relay `Pause-Ask`/`Pause-Review` + Exit Foils ៤ ទម្រង់ | ... |
| ជំហានទី៥ (≤2 min) | កិច្ចការផ្ទះភ្ជាប់ទ្រឹស្ដី ២ ផ្នែក (`ក -> ខ`) | ... |
```

---

## Stage 3 — Authoring the 4 Synchronized Lesson Package Documents

All 4 `.tex` files must synchronize **word-for-word** on measurements, vertex labels, Warrant Bank `①–⑤`, diagnostic foils `A–D`, and homework items `ក`/`ខ`. Enforce these shared research-derived rules first:
- **Monochrome B&W Print-Safe Classroom Scaffolding (Zero Color-Pen Dependency)**: Replace color coding (`២–៣ ពណ៌`, `ពណ៌ខៀវ/ក្រហម/បៃតង`) with **monochrome symbolic coding + embodied tracing prompts**: edge ticks (`|`/`||`), angle arcs, circled shared vertices/midpoints, bracketed finger-tracing cues (`[ចង្អុលអូស...]` / `[tracing]`), and a Numbered Warrant Bank (`①–⑤`).
- **Break Visual-Orientation & Separate-Figure Stereotypes**: Include rotated/reflected/inverted triangles (e.g., ~`140°`) and adjacent/overlapped/bow-tie figures with 100% pure black TikZ labels (`every node/.style={font=\scriptsize, text=black}`) and bold B&W strokes (`line width=0.8pt`–`1.4pt`, `black`, `white`, `gray!8`–`gray!38`/`gray!65`, `tk1`/`tk2` `0.85pt`).

### 3.1 `LS_Plan_<Topic>.tex` (Strictly 4 Balanced A4 Pages)
- Build from `references/lesson_plan_template.tex`, preserving the 3-level Kampong Thom header (`មន្ទីរអប់រំ យុវជន និងកីឡា ខេត្តកំពង់ធំ` → `ការិយាល័យអប់រំ យុវជន និងកីឡា ស្រុកកំពង់ស្វាយ` → `អនុវិទ្យាល័យព្រះក្រសាំង`), `TACTENG.TTF` `'3'` flourish, **50-minute split** (`2 + 9 + 17 + 20 + ≤2`), zero time-summary table inside `LS_Plan`, matching lunar & solar dates (`ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០` / `២០២៦`), and centered `គ្រូបង្រៀន` + `\vspace{32pt}` + `\hfill{\muol ហុក ប៊ុនថែន}\hspace*{1.4cm}`.
- Use modular micro-rows (`\\[-2pt]`) without forced `\pagebreak` (~92–98% page fill). Never use `\rowcolor` inside nested sub-tables (`\cellcolor{headgray}` + `\\[2pt] \hline`), never put Khmer inside `\texttt{...}`, and never prefix `-` before `\ditem`/`$\bullet$`/`\wcirc`.

### 3.2 `Teaching_Scenario_<Topic>.tex` (2 A4 Pages)
- Minute-by-minute execution & board-management script synchronized to the 50-minute 5Es split, listing exact timing checkpoints, classroom transitions, B&W material distribution cues, `Pause-Ask` / `Pause-Review` relay gates, and the empirical misconception diagnosis table.

### 3.3 `Teaching_Guideline_<Topic>.tex` (Mobile-First Pedagogical Manual & Mini-Research Report)
- **Screen/Mobile-First Readability (Contrast with 4-Page `LS_Plan`)**: Because teachers read `Teaching_Guideline_*.pdf` primarily on smartphones/tablets without printing, **NEVER** squeeze prose into `9pt–10pt` margins. Use `\documentclass[a4paper,12pt]{article}` and let pages flow naturally across **~13–16 readable A4 pages** with a strict 5-tier font scale:
  - **Tier 1 (Official Header & Title, unwrapped `\muol`)**: `ព្រះរាជាណាចក្រកម្ពុជា` (`13.5pt/21pt`), `ជាតិ សាសនា ព្រះមហាក្សត្រ` (`12pt/18.5pt`) + `\khmflourish` (`TACTENG` `'3'`, `38pt`); 3-line Kampong Thom / Kampong Svay / Preah Krasang (`10.8pt/17pt`); Main Title (`14pt/22pt`); Subtitle (`11.5pt/18pt`).
  - **Tier 2 (`\secbanner`, 2-line banners)**: Line 1 Khmer title in unwrapped `\muol\fontsize{12pt}{19pt}\selectfont`; Line 2 English subtitle in `\fontsize{10pt}{14.5pt}\selectfont\enit{...}` (`top=6pt, bottom=6pt, left=9pt, right=9pt`).
  - **Tier 3 (Systematic `\muol` Structural Headings)**: `\subsec` (`11.5pt/18.5pt` + bottom rule + `\needspace{2.5cm}`), `phasebox` titles (`11pt/17.5pt`, timing badge `10.5pt`), Callout Box headers (Metadata & Synthesis boxes, `11pt/17pt`), `scriptbox` lead-in `«គ្រូនិយាយថា៖` (`10.8pt/17pt`), figure captions `រូបទី ១៖...` (`10.5pt/16.5pt`), table headers (`10.2pt/16pt`), and signature labels (`11.5pt/18pt`, preserving `\vspace{32pt}` + `\hspace*{1.4cm}`).
  - **Tier 4 (Unified Body Prose, Lists, `phasebox` & `scriptbox`)**: Uniform **`11.5pt / 18.2pt`** (`KhmerOSsiemreap` `FakeBold=1.8, FakeSlant=0.25`, `Cambria Math` `Scale=1.06`, `Times New Roman` `\en{...}` `Scale=1.02`, `\parskip=4.5pt`).
  - **Tier 5 (Dense Tables, APA 7th References & TikZ Diagrams)**: Evidence `longtable` `10.2pt / 15.5pt` (`\arraystretch{1.28}`), APA 7th Reference List `10.8pt / 16.2pt` (`\TimesEn`, `\hangindent=0.85cm`), TikZ diagram labels **`>= 9.8pt–10pt`** cleanly spaced within `18.10 cm` text width (`10.5pt` captions).
- **CRITICAL `\muol` (`KhmerOSmuollight`) Glyph Safety Rule**:
  - **NEVER** wrap `\muol` inside `\textbf{...}` (or apply `FakeBold` to `KhmerOSmuollight`).
  - **ALWAYS** wrap every embedded Latin letter, digit, or ASCII punctuation (`SAS`, `E1–E5`, `POE`, `PDF`, `APA`, `#`, `&`, `/`, `-`, `(`, `)`) inside `\enbf{...}` (or math `$...$`) when inside `\muol`, because `KhmerOSmuollight` lacks Latin/ASCII glyphs. Verify **`0 Missing character`** warnings in `.log`.
- **Spacious Header & Footer Breathing Room (`geometry` + `fancyhdr`)**:
  - `left=1.45cm, right=1.45cm, top=2.30cm, bottom=2.30cm, headheight=18pt, headsep=0.68cm, footskip=0.88cm` (`18.10 cm` text width), `\headrulewidth=0.4pt`, `\footrulewidth=0.4pt`, `9.5pt` header/footer font with `2pt–3pt` vertical strut padding (`\rule[-3pt]{0pt}{14pt}` in `\fancyhead`, `\rule{0pt}{13pt}` in `\fancyfoot`) so Khmer ascenders/subscripts never crowd header/footer rules.
  - On Page 1, apply `\thispagestyle{firstpage}` (`\fancyhead{}`, `\headrulewidth=0pt`, `\footrulewidth=0.4pt`) with `\vspace*{-0.75cm}`.
- **Required Sections**:
  1. **Administrative Header & Lesson Package Context**: 3-level Kampong Thom / Kampong Svay / Preah Krasang header, title, metadata box, and overview of the 4-document package + attached evidence folder.
  2. **APA 7th Mini-Literature Review**: Cohesive academic synthesis in Khmer with accurate `\en{(Author, Year)}` APA 7th citations summarizing verified empirical studies across misconceptions, hands-on/POE manipulatives, and cognitive-load/proof scaffolding (quoting real `N`, %, or effect sizes from the verified PDFs).
  3. **Activity-by-Activity Research Rationale & Pedagogical Objectives**: Explicit mapping of Step 1–5 (E1–E5) and each page of `Printable_Materials_<Topic>.pdf` to research rationale and specific measurable student objectives.
  4. **Explicit Verbatim Teacher Scripts & Classroom Execution**: Step-by-step teacher dialogue in Khmer quote brackets (`«គ្រូនិយាយថា៖ ...»`), expected student answers, board-layout notes, and exact `Pause-Ask` / `Pause-Review` verbal prompts.
  5. **Troubleshooting & Misconception Remediation Guide**: Diagnostic triggers, common traps (e.g., SSA vs SAS, non-standard rotation, omitted shared elements, vertex order), and immediate corrective teacher moves.
  6. **Evidence Table (តារាងភស្តុតាងស្រាវជ្រាវ)**: Structured mapping of `#` / `Paper ID` → `APA Citation` → `Key Empirical Finding` → `Exact Lesson & Printable Integration`.
  7. **APA 7th Reference List**: Complete, properly italicized/formatted APA 7th reference list using `\en{...}`, matching `ឯកសារស្រាវជ្រាវយោង_PDF\00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` 1-to-1.

### 3.4 `Printable_Materials_<Topic>.tex` (B&W Print-Ready Classroom Pack, 1 Kit per A4 Page)
- **Strict B&W Print Contrast**: Use only `black`, `white`, and printer-safe grayscale (`gray!8`, `gray!15`, `gray!25`, `gray!65`); zero color fills or colored text. TikZ geometry lines must be bold (`line width=1.0pt`–`1.4pt`), with dashed/dotted `✂` cut borders and crisp pure-black labels offset cleanly from lines/dots/arcs.
- **CRITICAL True 1:1 Scale Rule (Physical Manipulatives Page)**: Draw ALL physical cut-out strips (e.g., `4 cm`, `6 cm`, decoy `5 cm`) AND angle/protraction mats (e.g., `32°` POE mats) in TikZ with **`x=1cm, y=1cm` (`scale=1.0`, ZERO downscaling)**, accompanied by a `5 cm` **ruler calibration bar** and explicit Khmer printer note: `ពេលបោះពុម្ព សូមជ្រើស Scale: Actual Size 100% — កុំជ្រើស Fit to Page`.
- **1 Material Kit per A4 Page** (separated cleanly with `\clearpage`, zero unintended spillover):
  1. **E2 Hands-On Cut-Out Manipulatives & POE Test Mats** (`x=1cm, y=1cm` true 1:1 scale + calibration bar + Predict/Observe checkboxes).
  2. **E4 3-Step Monochrome Detective / Scaffolding Cards** (`កាតស៊ើបអង្កេតសញ្ញាគន្លឹះ ៣ ជំហាន` with fillable step boxes and bold B&W TikZ figures).
  3. **E5 Collaborative Proof Relay Role Sheets** (Task A & B divided explicitly into Role 1 Visual Marker, Role 2 Warrant Connector `Pause-Ask!`, Role 3 Order Checker `Pause-Review!`).
  4. **Classroom Reference Poster** (Warrant Bank `①–⑤` with mini B&W TikZ visual cues + contrast/warning box).
  5. **E5 Diagnostic Exit Flashcards (`A / B / C / D`)** (cut-apart hold-up cards + bottom `✂` cut-off Teacher Answer & Remediation Key).
  6. **Step 5 Cut-Apart Homework Slips** (2 slips per A4 page matching `LS_Plan` Homework `ក` & `ខ` word-for-word + self-check boxes).

---

## Stage 4 — XeLaTeX Double-Compile, Glyph Check & Explicit Artifact Cleanup

Compile every `.tex` file **twice** with `-halt-on-error`, check `.log` for zero errors, **`0 Missing character`** warnings (especially inside `\muol` headings), and zero overfull boxes `> 5pt`, and move **ONLY explicit** `<JobName>.aux`, `<JobName>.log`, `<JobName>.out` files (plus `<JobName>.xdv` / `<JobName>.synctex.gz` if generated) into `_Build_Logs_and_Duplicates\`. **NEVER use `*.*` wildcards** so `ឯកសារស្រាវជ្រាវយោង_PDF\` and the deliverable `.tex`/`.pdf` files are never disturbed:

```powershell
$dir = "C:\Users\KIT\Desktop\NGS Lesson Plan\01_កិច្ចតែងការបង្រៀន\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>"
$logdir = "C:\Users\KIT\Desktop\NGS Lesson Plan\01_កិច្ចតែងការបង្រៀន\_Build_Logs_and_Duplicates"
New-Item -ItemType Directory -Force -Path $logdir | Out-Null
Set-Location $dir

$jobs = @("LS_Plan_<Topic>", "Teaching_Scenario_<Topic>", "Teaching_Guideline_<Topic>", "Printable_Materials_<Topic>")
foreach ($j in $jobs) {
  xelatex -interaction=nonstopmode -halt-on-error "$j.tex" > $null
  xelatex -interaction=nonstopmode -halt-on-error "$j.tex" | Select-String -Pattern "Output written|Error|Warning|Overfull|Missing character"
  foreach ($ext in @("aux", "log", "out", "xdv", "synctex.gz")) {
    if (Test-Path "$dir\$j.$ext") { Move-Item "$dir\$j.$ext" -Destination $logdir -Force }
  }
}
Get-ChildItem $dir | Select-Object Name
```

Confirm **only the 4 `.tex`/`.pdf` pairs and `ឯកសារស្រាវជ្រាវយោង_PDF\`** remain inside the lesson folder.

---

## Stage 5 — Full-Page Visual PNG Inspection (All 4 PDFs)

Render **every page** of **all 4 compiled PDFs** to **175–190 dpi PNG** via PyMuPDF and inspect **EVERY PNG** with `read_file` before reporting completion:

```powershell
$scratch = "<conversation-scratch>\pages"
New-Item -ItemType Directory -Force -Path $scratch | Out-Null
Remove-Item "$scratch\*.png" -ErrorAction SilentlyContinue
python -c "import fitz; docs=['LS_Plan_<Topic>','Teaching_Scenario_<Topic>','Teaching_Guideline_<Topic>','Printable_Materials_<Topic>']; [([p.get_pixmap(dpi=190).save(rf'$scratch\{d}_p{i+1}.png') for i,p in enumerate(doc)], print(d,'PAGES:',len(doc))) for d in docs for doc in [fitz.open(rf'$dir\{d}.pdf')]]"
```

Visual sign-off checklist (via `read_file` on **every** rendered PNG across all 4 PDFs):
1. **`LS_Plan_<Topic>.pdf`**: Exactly **4 balanced A4 pages** (~92–98% fill), zero sparse spillover pages, no mid-page Column 3 holes, matching dates, and clean `\vspace{32pt}` signature block on Page 4.
2. **`Teaching_Scenario_<Topic>.pdf`**: Clean **2 balanced A4 pages** synced with the 50-minute 5Es pacing and empirical misconception table.
3. **`Teaching_Guideline_<Topic>.pdf`**: Comfortable **mobile-first readability** (~13–16 A4 pages, `11.5pt / 18.2pt` body & `scriptbox`, `10.2pt–10.8pt` tables & APA, `>= 9.8pt–10pt` TikZ labels + `10.5pt` captions), clean unwrapped `\muol` heading hierarchy with zero missing glyphs, spacious `2.30cm` header/footer clearance where Khmer ascenders/subscripts never touch `\headrule`/`\footrule` (and Page 1 omits running header via `\thispagestyle{firstpage}`), `TACTENG` `'3'`, `\en{...}` Times New Roman APA 7th citations/references, verbatim scripts, Evidence Table, and Reference List.
4. **`Printable_Materials_<Topic>.pdf`**: Exact **1 kit per A4 page** (`\clearpage`), pure B&W thick lines (`1.0pt`–`1.4pt`), crisp `✂` cut boxes, and visually verified true `1:1` ruler calibration bar (`5 cm`) & cut-out proportions on the hands-on mat page.
5. **Cross-Package TikZ & Typography Integrity**: Every TikZ label across all 4 PDFs is 100% pure black with zero overlapping lines/arcs/dots/shading; Khmer glyphs (`FakeBold=1.8`, `FakeSlant=0.25`), math symbols, `\cellcolor{headgray}` headers, zero `- \ditem` mixes, and zero `\texttt` Khmer boxes.
