---
name: ngs-lesson-plan
description: Design, write, illustrate (TikZ), and compile research-driven 50-minute NGS Khmer lesson packages (កិច្ចតែងការបង្រៀន ៥០ នាទីតាមគំរូ 5Es និងលំនាំ ls_plan.tex) delivering the standard 4-document suite (LS_Plan across flexible 4–8+ content-driven A4 pages, Teaching_Scenario, Teaching_Guideline, Printable_Materials) plus an attached verified Open-Access evidence folder (ឯកសារស្រាវជ្រាវយោង_PDF), proportional B&W TikZ geometry figures (3.8–6.8 cm, black labels), true 1:1 printable manipulatives, line-by-line structured teacher formatting, full A4 page fill (>=90% / <=1.5 cm bottom gap on non-final pages), and mandatory Stage 5 quantitative bottom-gap & visual PNG audit. Use whenever creating, updating, or reviewing NGS lesson packages for any grade or topic.
---

# NGS Lesson Plan Package Builder (`ngs-lesson-plan`)

Use this skill whenever the user asks to create, update, polish, or standardize an NGS lesson package (`កិច្ចតែងការបង្រៀន` + `Teaching Scenario` + `Teaching Guideline` + `Printable Materials` + `ឯកសារស្រាវជ្រាវយោង_PDF`). Follow the complete 5-stage pipeline in `references/research_workflow.md`.

## Mandatory Standards (Summary)

1. **School & Author Context**: 3-level administrative header (`មន្ទីរអប់រំ យុវជន និងកីឡា ខេត្តកំពង់ធំ` → `ការិយាល័យអប់រំ យុវជន និងកីឡា ស្រុកកំពង់ស្វាយ` → `អនុវិទ្យាល័យព្រះក្រសាំង`), គ្រូបង្រៀន **ហុក ប៊ុនថែន** (unless overridden), ឆ្នាំសិក្សា ២០២៦ (ព.ស. ២៥៧០, ឆ្នាំមមី អដ្ឋស័ក)។ Under the administrative signature block, center `គ្រូបង្រៀន`, leave `\vspace{32pt}` for signing, and shift the teacher name down-right (`\hfill{\muol ហុក ប៊ុនថែន}\hspace*{1.4cm}`)។ Match top teaching date with both Khmer lunar & solar dates in the signature block.
2. **50-Minute Teaching Period (Never 45 min)**:
   - Step 1 (រដ្ឋបាលថ្នាក់): `2 min`
   - Step 2 (កំណែ `≤3 min` + រំលឹក `3 min` + `E1 - Engage 3 min`): `9 min`
   - Step 3 (`E2 - Explore 11 min` + `E3 - Explain 6 min`): `17 min`
   - Step 4 (`E4 - Elaborate 10 min` + `E5 - Evaluate 10 min`): `20 min`
   - Step 5 (កិច្ចការផ្ទះ + បណ្ដាំផ្ញើ): `≤2 min`
   - **Total**: `50 min`.
   - Keep only inline `\fiveE{...}` / `\timenote{...}` cues inside `LS_Plan_<Topic>.tex` — **never** include a time-summary table inside `LS_Plan`. Put detailed minute-by-minute scripts into the separate `Teaching_Scenario_<Topic>.tex/.pdf` (flexible 2–4 pages as content requires).
3. **Standard 5-Part Deliverable Per Lesson Folder (`01_កិច្ចតែងការបង្រៀន\<Grade>\<Topic>\<Sublesson>\`)**:
   - **`LS_Plan_<Topic>.tex` + `.pdf`**: Teacher-friendly 50-minute 5Es Lesson Plan spanning a **flexible, content-driven `4` to `7–8+` A4 pages** (**NEVER** artificially force-capped at 4 pages). Non-final pages (`1..N-1`) must fill **`>= 90%` (`bottom_gap <= 1.5 cm`)** via granular `2–5 line` `longtable` sub-rows (`\\[3pt]`) and dedicated TikZ sub-rows (`& \cfig{...} & \\[3pt]`), final page `N` `>= 40%` full, with structured line-by-line vertical breaks and proportional `3.8–6.8 cm` B&W TikZ diagrams.
   - **`Teaching_Scenario_<Topic>.tex` + `.pdf`**: Minute-by-minute pacing & board-management script (**flexible `2–4` A4 pages** according to actual content, granular `longtable` sub-rows, `>= 90%` fill on Pages `1..N-1`), synced with `LS_Plan`, Pause-Ask/Pause-Review gates, B&W materials checklist, and empirical misconceptions table.
   - **`Teaching_Guideline_<Topic>.tex` + `.pdf`**: Comprehensive **Mobile-First** pedagogical manual & mini-research report (`~14–20` comfortable A4 pages for phone/tablet reading — NEVER squeezed into 9pt–10pt margins!). Uses `\documentclass[a4paper,12pt]{article}`, `breakable` `phasebox`/`scriptbox`/`tcolorbox` (`\tcbuselibrary{breakable,skins}`), no arbitrary `\clearpage`, and `\Needspace <= 2.2cm` (`\secbanner`/`\refbanner`/tables) or `<= 1.7cm` (`\subsec`) to eliminate large mid-document bottom gaps; uniform `11.5pt / 18.2pt` body & `scriptbox` prose (`KhmerOSsiemreap`, `Cambria Math` `Scale=1.06`, `Times New Roman` `\en{...}` `Scale=1.02`), `10.2pt–10.8pt` tables & APA 7th references, `>= 9.8pt–10pt` TikZ labels (`10.5pt` captions), `TACTENG` `'3'` `\khmflourish`, spacious `left/right=1.45cm, top/bottom=2.30cm, headheight=18pt, headsep=0.68cm, footskip=0.88cm` (`\headrulewidth=0.4pt`, `\footrulewidth=0.4pt`, `9.5pt` header/footer with `2pt–3pt` vertical strut padding, Page 1 `\thispagestyle{firstpage}` + `\vspace*{-0.75cm}`), and a systematic unwrapped `KhmerOSmuollight` (`\muol`) heading hierarchy (see item 5 for glyph safety). Covers administrative header/context, APA 7th mini-literature review, activity-by-activity rationale & objectives, explicit verbatim teacher scripts (`«គ្រូនិយាយថា៖ ...»`), troubleshooting, Evidence Table, and APA 7th reference list under the concise single-line banner **`\refbanner{ឯកសារយោង}`** (pure Khmer `ឯកសារយោង` ONLY — no English subtitle, no section prefix like `ផ្នែកទី ៧៖ បញ្ជី...`, and NO fixed `14` or `15` reference quota; include the exact genuine number of verified Open-Access papers discovered during research).
   - **`Printable_Materials_<Topic>.tex` + `.pdf`**: B&W print-ready classroom pack (pure monochrome `black`/`white`/`gray!8`–`gray!65`, zero color, bold `1.0pt`–`1.4pt` TikZ strokes & dashed `✂` cut boxes; **1 kit per A4 page** via `\clearpage`; **true 1:1 `x=1cm, y=1cm` scale** with zero downscaling for physical cut-out strips & angle mats + ruler calibration bar & `Actual Size 100%` note; crystal-clear, valid, unambiguous student-facing instructions/`Introduction` structured with `itemize` and `align` alignment for effortless eye readability — never run-on blocks; E4/E5 cards, Relay role sheets, Warrant Bank poster, diagnostic exit flashcards + teacher key, and cut-apart homework slips matching `LS_Plan` verbatim).
   - **`ឯកសារស្រាវជ្រាវយោង_PDF\`**: Attached evidence folder inside the lesson directory containing numbered verified Open-Access PDFs (`01_<AuthorYear_ShortTopic>.pdf` .. matching the genuine count discovered during research — never padded or capped to a fixed quota of `14` or `15`) and `00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` matching every APA citation in `ឯកសារយោង` inside `Teaching_Guideline_<Topic>.tex` 1-to-1.
4. **Research-Driven Constructivist 5Es, Novelty & B&W Print-Safe Scaffolding**:
   - Ground every new or upgraded lesson in verified Open-Access academic literature (Stages 1–2 in `references/research_workflow.md`, archived in `03_ឯកសារស្រាវជ្រាវ\`).
   - Source PDFs via OpenAlex (`filter=is_oa:true`), ERIC (`files.eric.ed.gov/fulltext/<ID>.pdf`), Semantic Scholar (`openAccessPdf`), DOAJ / OA publisher repositories, and `search_web` (`domain:"scholar.google.com"`, `eric.ed.gov`, `mdpi.com`, etc.). **NEVER** scrape `scholar.google.com` directly or bypass any CAPTCHA/Turnstile/paywall gate. Validate every downloaded and attached PDF via Python (`b'%PDF-'` magic bytes + PyMuPDF `fitz`: `>=2` pages and `>500` extracted chars; delete any HTML/403/stub file immediately).
   - Design genuinely fresh classroom hooks, hands-on POE experiments, misconception traps, **monochrome symbolic/tracing classroom scaffolding** (tick marks `|`/`||`, angle arcs, circled shared vertices/midpoints, bracketed finger-tracing cues `[tracing]`, and numbered warrant banks `①–⑤` — **never** color-pen/color-marker dependencies on B&W printed worksheets), non-standard rotated/reflected/overlapped figures, and active evaluation games.
5. **LaTeX Technical Rules, Full Page Fill, Flexible Page Count, Vertical TikZ, Itemize/Aligned Typography, Textbook Fidelity & `\muol` Safety**:
   - **Rule A — Full Page Utilization (`>= 90%` Fill / `<= 1.5 cm` Bottom Gap on Pages `1..N-1`)**: Because `longtable` can only break pages between rows (`\\`), **forbid** monolithic `longtable` rows (`> 5–6 lines`, or bundling prose + TikZ diagram + nested table in one row). Split every 5E phase (`E1..E5`) into **granular `2–5 line` sub-rows** separated by `\\[3pt]` (**without** `\hline` inside the same step; place `\hline` only between major steps `ជំហានទី១..៥`) and place each TikZ diagram in its **own dedicated sub-row** (`& \cfig{...} & \\[3pt]`). In `Teaching_Guideline`, always load `\tcbuselibrary{breakable,skins}`, mark `phasebox`/`scriptbox`/multi-paragraph boxes as `breakable`, and keep `\needspace <= 2.2cm` (headings only).
   - **Rule B — Unlimited Content-Driven Page Count (`4` to `7–8+` Pages)**: **NEVER** force `LS_Plan` into a rigid 4-page cap (`teaching_scenario` `2–4` pp.; `teaching_guideline` `~14–20` pp. at `11.5pt/18.2pt` with `2.30cm` header/footer clearance). Use as many pages as needed so every formal derivation and vertical diagram fits cleanly without cramming (`\fontsize{10pt}{15.2pt}\selectfont`, `\arraystretch{1.15}`, `\cfig` `4pt` vertical padding, NO forced `\pagebreak`), keeping Pages `1..N-1` `>= 90%` full and Final Page `N` `>= 40%` full.
   - **Rule C — Zero Khan (`។`) in Teacher/Student Columns, Mandatory `itemize` + `aligned`, Full Formal Math & 100% Textbook Box Fidelity**:
     - **ZERO `។` (Khmer Khan) in Teacher & Student Activity Columns**: In `LS_Plan`, **NEVER** use the Khmer punctuation mark `។` inside Column 1 (`សកម្មភាពគ្រូ`) or Column 3 (`សកម្មភាពសិស្ស`).
     - **Mandatory `itemize` & `align` (`aligned`) — Zero Run-On Inline Lists**: Whenever listing points 1, 2, 3, etc., **NEVER** write them continuously inline; use proper `itemize` / bulleted line items (`\item` / `\ditem` / `\wcirc`) and `\begin{aligned}...\end{aligned}` (or aligned columns) for clean eye-friendly alignment, forbidding negative spacing `\\[-2pt]`. Put every phase badge (`\fiveE{...} \timenote{...}`) on its own line (`\par\vspace{2pt}`), and start every teacher action, guiding question, board heading, individual math step, and student response on a new line.
     - **Full Formal Mathematical Writing (No Shortcuts)**: In Column 2 (`ខ្លឹមសារមេរៀន`), all worked examples, exercises, and proofs MUST be written in **complete, formal mathematical prose** with full step-by-step derivations (`\begin{aligned}`, `សម្មតិកម្ម`, `សន្និដ្ឋាន`, `ដំណោះស្រាយ`, `ដូច្នេះ`, 1 line = 1 step) — **never** abbreviate or skip steps.
     - **100% Verbatim MoEYS Textbook Boxes**: Whenever the official MoEYS textbook has a **`ជាទូទៅ`**, **`និយមន័យ`**, **`លក្ខណៈ`**, or **`ទ្រឹស្ដីបទ`** box, reproduce its wording **100% verbatim** matching the textbook.
   - **Rule D — Clear B&W TikZ Figures Stacked Vertically (`1 Figure Per Row` — NEVER 2–3 Side-by-Side)**: **FORBID** placing 2 or 3 TikZ figures horizontally side-by-side in one row! Every diagram must be drawn clearly and stacked **vertically from top to bottom (1 figure = 1 dedicated row `& \cfig{...} & \\[3pt]`)**, regardless of total page count. Keep generous proportional widths (`3.8 cm – 5.2 cm` in Col 1/Col 3; **`4.5 cm – 6.8 cm`** in Col 2; forbid `< 3.5 cm` or `scale < 0.80`). Set `every node/.style={font=\footnotesize, text=black}` (`\footnotesize` `8.5pt–9pt` or `\small` `10pt` in `LS_Plan`; `>= 10pt` in `Teaching_Guideline`), `>= 2.5mm` label clearance from lines/arcs/ticks, forbid `\tiny` and forbid color on `\node` text. Draw strokes strictly B&W (`black`, `white`, `gray!8`–`gray!38`/`gray!65`, `line width=0.8pt`–`1.4pt`, `tk1`/`tk2` `0.85pt`), using **`TACTENG.TTF` `'3'`** (`\Tacteing`) for `\khmflourish`.
   - **Systematic `\muol` (`KhmerOSmuollight`) Hierarchy & CRITICAL Glyph Safety**: In `Teaching_Guideline` (and headings across all files), **NEVER** wrap `\muol` inside `\textbf{...}` (or apply `FakeBold` to `KhmerOSmuollight`), and **ALWAYS** wrap embedded Latin letters, digits, or ASCII punctuation (`SAS`, `E1–E5`, `POE`, `PDF`, `APA`, `#`, `&`, `/`, `-`, `(`, `)`) inside `\enbf{...}` (or `$...$`) when inside `\muol`, verifying **`0 Missing character`** warnings in `.log`. Keep MiKTeX/TeX Live `longtable` guard & `\XeTeXlinebreaklocale "km"`, never use `\rowcolor` inside nested `longtable` sub-tables (use `\cellcolor{headgray}` + `\\[2pt] \hline`), never wrap Khmer text in `\texttt{...}`, and never prefix `-` before `\ditem`/`$\bullet$`/`\wcirc`.
6. **3-Folder Workspace Separation, Explicit Cleanup & Mandatory Git Commit + Push**:
   - Keep `01_កិច្ចតែងការបង្រៀន\` (4-document package + `ឯកសារស្រាវជ្រាវយោង_PDF\`), `02_មេរៀន\` (student lessons, worksheets, and textbooks/សៀវភៅសិក្សាគោល), and `03_ឯកសារស្រាវជ្រាវ\` (verified Open-Access PDFs in `papers\` + `Research_Brief_<Topic>.md`) strictly separate.
   - Move **ONLY explicit `<JobName>.aux`, `<JobName>.log`, `<JobName>.out`** (never `*.*` wildcards) to `01_កិច្ចតែងការបង្រៀន\_Build_Logs_and_Duplicates\`.
   - **Mandatory `git commit` + `git push`**: After completing or updating **any** lesson plan package (or skill/rules update), **ALWAYS** stage all `.tex`, `.pdf`, `ឯកសារស្រាវជ្រាវយោង_PDF/`, `03_ឯកសារស្រាវជ្រាវ/`, and rule files (`git -c core.quotePath=false add ...`), then **`git commit` and `git push origin main`** to GitHub so every deliverable and preference is permanently preserved.

---

## Step-by-Step Workflow (5-Stage Pipeline)

### Step 1: Scholarly Pedagogical Research & Evidence Folder Setup (Stages 1–2)
Read `references/research_workflow.md` and complete research **before** drafting LaTeX:
- Prepare mirrored folders `<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>`:
  - `C:\Users\KIT\Desktop\NGS Lesson Plan\03_ឯកសារស្រាវជ្រាវ\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\papers\`
  - `C:\Users\KIT\Desktop\NGS Lesson Plan\01_កិច្ចតែងការបង្រៀន\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\ឯកសារស្រាវជ្រាវយោង_PDF\`
- Discover, download, and verify Open-Access PDFs (`b'%PDF-'` + `fitz` `>=2` pp. & `>500` chars) via zero-CAPTCHA APIs/DOAJ/`search_web` (`/swarm` parallel lenses `misconceptions_`, `activities_`, `proof_`, or single-agent sequential). Extract real empirical data with `fitz`.
- Copy verified PDFs with numbered filenames (`01_<AuthorYear_ShortTopic>.pdf` ..) into `ឯកសារស្រាវជ្រាវយោង_PDF\`, re-verify with `fitz`, and create `00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md`.
- Synthesize empirical findings into `Research_Brief_<Topic>.md` inside `03_ឯកសារស្រាវជ្រាវ\...\`.

### Step 2: Start from the Reference Template & Continuity Check
- Read `references/lesson_plan_template.tex` in this skill directory and copy its exact packages, cross-platform `\NGSFindFonts` font resolver (`fonts/` repo bundle + Windows fallback for `KhmerOSsiemreap`, `KhmerOSmuollight`, `AKbalthom Naga Bold`, `cambria.ttc`, `calibri.ttf`, `cour.ttf`, `TACTENG.TTF`; add `times.ttf` `\en{...}` for APA citations in `Teaching_Guideline`), MiKTeX/TeX Live `longtable` guard, `\khmflourish`, helper macros, header, and signature block.
- Inspect neighboring lessons in `01_កិច្ចតែងការបង្រៀន\` so E2/E3/E4/E5 activities are 100% fresh and homework continuity aligns cleanly.

### Step 3: Author All 4 Synchronized `.tex` Deliverables (Stage 3)
1. **`LS_Plan_<Topic>.tex`**: Sections I–IV (`longtable` `L{5.50cm}|L{7.90cm}|L{4.80cm}`, `10pt/15.2pt`, `\arraystretch{1.15}`), flexible **`4–8+` content-driven A4 pages**, granular `2–5 line` sub-rows (`\\[3pt]`) + dedicated figure sub-rows (`& \cfig{...} & \\[3pt]`), line-by-line vertical formatting (no run-on walls, no `\\[-2pt]`), monochrome symbolic/tracing scaffolds, Numbered Warrant Bank `①–⑤`, proportional `3.8–6.8 cm` rotated/overlapped B&W TikZ figures (`\footnotesize`/`\small` labels), `Pause-Ask`/`Pause-Review` relay, multi-foil exit checks, no internal time-summary table.
2. **`Teaching_Scenario_<Topic>.tex`**: Flexible **`2–4` A4 pages** minute-by-minute execution script synced to the 50-minute 5Es, granular `longtable` sub-rows (`>= 90%` page fill), board plan, B&W material list, and empirical misconception table.
3. **`Printable_Materials_<Topic>.tex`**: 1 kit per A4 page (`\clearpage`), pure B&W (`1.0pt`–`1.4pt`), proportional generous layouts + true `1:1` `x=1cm, y=1cm` cut-outs & angle mats + calibration bar + `Actual Size 100%` note, verbatim alignment with `LS_Plan`.
4. **`Teaching_Guideline_<Topic>.tex`**: Mobile-First manual & mini-research report (`12pt` class, `~14–20` natural A4 pages, `breakable` `phasebox`/`scriptbox`/`tcolorbox` via `\tcbuselibrary{breakable,skins}`, no arbitrary `\clearpage`, `\Needspace <= 2.2cm` / `\subsec` `<= 1.7cm`, `11.5pt/18.2pt` prose & `scriptbox`, `10.2pt–10.8pt` tables/APA, `>= 10pt` TikZ labels `6.5–14.0 cm` wide + `10.5pt` captions, `2.30cm` top/bottom header/footer struts, systematic unwrapped `\muol` headings with `\enbf{...}` for embedded Latin/ASCII, `TACTENG` `'3'`, `Times New Roman` `\en{...}`, `Cambria Math` `Scale=1.06`) containing header/context, APA 7th mini-lit review, activity-by-activity rationale & objectives (referencing exact `Printable_Materials` pages), verbatim teacher scripts (`«គ្រូនិយាយថា៖ ...»`), troubleshooting, Evidence Table, and APA 7th references under the concise single-line heading **`\refbanner{ឯកសារយោង}`** matching the genuine number of verified PDFs in `ឯកសារស្រាវជ្រាវយោង_PDF\` 1-to-1 (never fixed to a `14` or `15` quota).

### Step 4: Compile Twice, Check `.log` & Explicit Artifact Cleanup (Stage 4)
Compile every `.tex` file **twice** with `xelatex -interaction=nonstopmode -halt-on-error`, check `.log` for zero errors, **`0 Missing character`** warnings, and zero severe overfull boxes (`> 5pt`), and move **ONLY explicit** `.aux`, `.log`, `.out` (and `.xdv`/`.synctex.gz` if used) files (**never `*.*`**) to `_Build_Logs_and_Duplicates\`:

```powershell
$dir = "<lesson-folder>"
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

Confirm **only the 4 `.tex`/`.pdf` pairs and `ឯកសារស្រាវជ្រាវយោង_PDF\`** remain in the lesson folder.

### Step 5: Mandatory Final Teacher-Friendliness, Bottom-Fill & Visual PNG Gate (Stage 5)

Before finishing **any** lesson package, run **BOTH** the quantitative PyMuPDF (`fitz`) bottom-gap check AND full-page visual PNG inspection:

1. **Quantitative PyMuPDF (`fitz`) Bottom-Gap & Fill Check**: Run on `LS_Plan`, `Teaching_Scenario`, and `Teaching_Guideline` to verify **every non-final page (`1..N-1`) has `bottom_gap <= 1.6 cm` (~`>= 90%` fill)** and **final page `N` has `>= 40%` fill** (`min_y` to `max_y` of body content, excluding header/footer margin bands):

```python
import fitz
from pathlib import Path

def audit_page_fill(pdf_path: Path, top_band_pt: float = 30.0, bot_limit_pt: float = 812.0, max_gap_cm: float = 1.6):
    # A4 height = 841.89 pt (29.7 cm); bottom limit ~ 812 pt for LS_Plan (0.92 cm margin), ~ 776 pt for Guideline (2.30 cm bottom margin)
    with fitz.open(pdf_path) as doc:
        n = len(doc)
        usable_h = bot_limit_pt - top_band_pt
        flagged = []
        for idx, page in enumerate(doc):
            blocks = [b for b in page.get_text("blocks") if b[3] > top_band_pt + 4 and b[1] < bot_limit_pt - 8]
            drawings = [d["rect"] for d in page.get_drawings() if d["rect"].y1 > top_band_pt + 4 and d["rect"].y0 < bot_limit_pt - 8]
            max_y = max([b[3] for b in blocks] + [r.y1 for r in drawings] + [top_band_pt])
            gap_cm = (bot_limit_pt - max_y) * 2.54 / 72.0
            fill_pct = 100.0 * (max_y - top_band_pt) / usable_h
            is_last = (idx == n - 1)
            ok = (fill_pct >= 40.0) if is_last else (gap_cm <= max_gap_cm)
            print(f"{pdf_path.name} P{idx+1}/{n}: fill={fill_pct:.1f}% bottom_gap={gap_cm:.2f}cm ok={ok}")
            if not ok:
                flagged.append((idx + 1, fill_pct, gap_cm))
        if flagged:
            raise AssertionError(f"Layout bottom-fill gate failed on {pdf_path.name}: {flagged}")
```

2. **Full-Page PNG Rendering & `read_file` Sign-Off**: Render **every page** of **all 4 compiled PDFs** to 175–190 dpi PNG via PyMuPDF and inspect **every PNG** with `read_file`:

```powershell
$scratch = "<conversation-scratch>\pages"
New-Item -ItemType Directory -Force -Path $scratch | Out-Null
Remove-Item "$scratch\*.png" -ErrorAction SilentlyContinue
python -c "import fitz; docs=['LS_Plan_<Topic>','Teaching_Scenario_<Topic>','Teaching_Guideline_<Topic>','Printable_Materials_<Topic>']; [([p.get_pixmap(dpi=190).save(rf'$scratch\{d}_p{i+1}.png') for i,p in enumerate(doc)], print(d,'PAGES:',len(doc))) for d in docs for doc in [fitz.open(rf'$dir\{d}.pdf')]]"
```

Verify visually across ALL rendered PNGs against the **5-Item Mandatory Final Gate**:
1. **Bottom Utilization (`<= 1.5–1.6 cm` gap / `>= 90%` fill on Pages `1..N-1`)**: Zero large unused whitespace before page breaks; final page `N` balanced (`>= 40%` fill) with clean signature block.
2. **Flexible Content-Driven Page Count**: `LS_Plan` (`4–8+` A4 pp. or as many pages as needed) and `Teaching_Scenario` (`2–4` A4 pp.) match actual content naturally (zero forced cramming); `Teaching_Guideline` flows cleanly (`~14–20` pp.) with `breakable` boxes and clear header/footer clearance.
3. **Vertical Uncramped TikZ Figures (`1 Figure Per Row` — NEVER 2–3 Side-by-Side)**: Every figure stands alone vertically (`3.8–6.8 cm` in `LS_Plan`, `>= 10pt` in `Guideline`), no micro-shrunk `< 3.5 cm` figures, `100%` black `\footnotesize`/`\small` labels cleanly offset (`>= 2.5mm`); `Printable_Materials` 1 kit per page (`\clearpage`) with true 1:1 `1 cm = 1 cm` calibration bar, cut-out proportions, and crystal-clear valid student instructions formatted with `itemize` + `align`.
4. **Structured `itemize`/`aligned` Formatting, Zero `។` in Activity Columns & 100% Verbatim Textbook Boxes**: Zero `។` inside Teacher & Student Activity columns, every numbered/bulleted point uses `itemize`, every worked solution uses complete formal mathematical writing with `\begin{aligned}`, and all textbook `ជាទូទៅ`/`និយមន័យ`/`លក្ខណៈ` boxes match the MoEYS textbook 100% verbatim.
5. **Typography, Glyph Integrity & GitHub Delivery**: Zero overlapping text, crisp `\muol` hierarchy (`0 Missing character`), clean `FakeBold=1.8`/`FakeSlant=0.25`, `\en{...}` Times New Roman APA citations/references, `TACTENG` `'3'`, `\cellcolor{headgray}`, zero `- \ditem` mixes, zero `\texttt` Khmer boxes, followed by **`git commit` and `git push origin main`**.

If **ANY** item fails quantitative `fitz` checks or visual PNG inspection, **edit the `.tex` (split monolithic `longtable` rows into `2–5 line` sub-rows, isolate TikZ diagrams into dedicated vertical rows, enlarge cramped figures, add `itemize`/`aligned` formatting, remove `។` from Teacher/Student columns) and recompile & re-inspect** before finishing and pushing to GitHub.
