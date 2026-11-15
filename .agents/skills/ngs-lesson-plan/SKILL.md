---
name: ngs-lesson-plan
description: Design, write, illustrate (TikZ), and compile research-driven 50-minute NGS Khmer lesson packages (កិច្ចតែងការបង្រៀន ៥០ នាទីតាមគំរូ 5Es និងលំនាំ ls_plan.tex) delivering the standard 4-document suite (LS_Plan, Teaching_Scenario, Teaching_Guideline, Printable_Materials) plus an attached verified Open-Access evidence folder (ឯកសារស្រាវជ្រាវយោង_PDF), crisp black-labeled B&W TikZ geometry figures, true 1:1 printable manipulatives, balanced A4 density, and clean folder hygiene. Use whenever creating, updating, or reviewing NGS lesson packages for any grade or topic.
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
   - Keep only inline `\fiveE{...}` / `\timenote{...}` cues inside `LS_Plan_<Topic>.tex` — **never** include a time-summary table inside `LS_Plan`. Put detailed minute-by-minute scripts into the separate `Teaching_Scenario_<Topic>.tex/.pdf` (2 pages).
3. **Standard 5-Part Deliverable Per Lesson Folder (`01_កិច្ចតែងការបង្រៀន\<Grade>\<Topic>\<Sublesson>\`)**:
   - **`LS_Plan_<Topic>.tex` + `.pdf`**: Compact 50-minute 5Es Lesson Plan (classroom execution plan, **strictly 4 balanced A4 pages** at ~92–98% density).
   - **`Teaching_Scenario_<Topic>.tex` + `.pdf`**: Minute-by-minute pacing & board-management script (**2 A4 pages**), synced with `LS_Plan`, Pause-Ask/Pause-Review gates, B&W materials checklist, and empirical misconceptions table.
   - **`Teaching_Guideline_<Topic>.tex` + `.pdf`**: Comprehensive **Mobile-First** pedagogical manual & mini-research report (~13–16 comfortable A4 pages for phone/tablet reading — NEVER squeezed into 9pt–10pt margins!). Uses `\documentclass[a4paper,12pt]{article}`, uniform `11.5pt / 18.2pt` body & `scriptbox` prose (`KhmerOSsiemreap`, `Cambria Math` `Scale=1.06`, `Times New Roman` `\en{...}` `Scale=1.02`), `10.2pt–10.8pt` tables & APA 7th Reference List, `>= 9.8pt–10pt` TikZ labels (`10.5pt` captions), `TACTENG` `'3'` `\khmflourish`, spacious `left/right=1.45cm, top/bottom=2.30cm, headheight=18pt, headsep=0.68cm, footskip=0.88cm` (`\headrulewidth=0.4pt`, `\footrulewidth=0.4pt`, `9.5pt` header/footer with `2pt–3pt` vertical strut padding, Page 1 `\thispagestyle{firstpage}` + `\vspace*{-0.75cm}`), and a systematic unwrapped `KhmerOSmuollight` (`\muol`) heading hierarchy (see item 5 for glyph safety). Covers administrative header/context, APA 7th mini-literature review, activity-by-activity rationale & objectives, explicit verbatim teacher scripts (`«គ្រូនិយាយថា៖ ...»`), troubleshooting, Evidence Table, and APA 7th Reference List.
   - **`Printable_Materials_<Topic>.tex` + `.pdf`**: B&W print-ready classroom pack (pure monochrome `black`/`white`/`gray!8`–`gray!65`, zero color, bold `1.0pt`–`1.4pt` TikZ strokes & dashed `✂` cut boxes; **1 kit per A4 page** via `\clearpage`; **true 1:1 `x=1cm, y=1cm` scale** with zero downscaling for physical cut-out strips & angle mats + ruler calibration bar & `Actual Size 100%` note; E4/E5 cards, Relay role sheets, Warrant Bank poster, diagnostic exit flashcards + teacher key, and cut-apart homework slips matching `LS_Plan` verbatim).
   - **`ឯកសារស្រាវជ្រាវយោង_PDF\`**: Attached evidence folder inside the lesson directory containing numbered verified Open-Access PDFs (`01_<AuthorYear_ShortTopic>.pdf` ..) and `00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` matching every APA citation in `Teaching_Guideline_<Topic>.tex` 1-to-1.
4. **Research-Driven Constructivist 5Es, Novelty & B&W Print-Safe Scaffolding**:
   - Ground every new or upgraded lesson in verified Open-Access academic literature (Stages 1–2 in `references/research_workflow.md`, archived in `03_ឯកសារស្រាវជ្រាវ\`).
   - Source PDFs via OpenAlex (`filter=is_oa:true`), ERIC (`files.eric.ed.gov/fulltext/<ID>.pdf`), Semantic Scholar (`openAccessPdf`), DOAJ / OA publisher repositories, and `search_web` (`domain:"scholar.google.com"`, `eric.ed.gov`, `mdpi.com`, etc.). **NEVER** scrape `scholar.google.com` directly or bypass any CAPTCHA/Turnstile/paywall gate. Validate every downloaded and attached PDF via Python (`b'%PDF-'` magic bytes + PyMuPDF `fitz`: `>=2` pages and `>500` extracted chars; delete any HTML/403/stub file immediately).
   - Design genuinely fresh classroom hooks, hands-on POE experiments, misconception traps, **monochrome symbolic/tracing classroom scaffolding** (tick marks `|`/`||`, angle arcs, circled shared vertices/midpoints, bracketed finger-tracing cues `[tracing]`, and numbered warrant banks `①–⑤` — **never** color-pen/color-marker dependencies on B&W printed worksheets), non-standard rotated/reflected/overlapped figures, and active evaluation games.
5. **LaTeX Technical Rules, `\muol` Glyph Safety, Page Utilization & TikZ B&W Clarity**:
   - **Print-Compact `LS_Plan` (`lesson_plan_template.tex`) vs. Mobile-First `Teaching_Guideline`**: Keep `LS_Plan_<Topic>.tex` compact (`\fontsize{9.5pt}{14.0pt}\selectfont`, `\arraystretch{1.05}`, `\cfig` `1pt` padding, `0.95cm`/`0.85cm` margins, modular micro-rows `\\[-2pt]`, NO forced `\pagebreak`) to fill **strictly 4 balanced A4 pages**. Conversely, let `Teaching_Guideline_<Topic>.tex` breathe across ~13–16 A4 pages at `11.5pt / 18.2pt` with `2.30cm` top/bottom header/footer clearance.
   - **Systematic `\muol` (`KhmerOSmuollight`) Hierarchy & CRITICAL Glyph Safety**: In `Teaching_Guideline` (and headings across all files), **NEVER** wrap `\muol` inside `\textbf{...}` (or apply `FakeBold` to `KhmerOSmuollight`), and **ALWAYS** wrap embedded Latin letters, digits, or ASCII punctuation (`SAS`, `E1–E5`, `POE`, `PDF`, `APA`, `#`, `&`, `/`, `-`, `(`, `)`) inside `\enbf{...}` (or `$...$`) when inside `\muol`, verifying **`0 Missing character`** warnings in `.log`.
   - Keep MiKTeX 2025 `longtable` guard & `\XeTeXlinebreaklocale "km"`. Never use `\rowcolor` inside nested `longtable` sub-tables (use `\cellcolor{headgray}` + `\\[2pt] \hline`). Never wrap Khmer text in `\texttt{...}` or mix `-` before `\ditem`/`$\bullet$`/`\wcirc`.
   - Set `every node/.style={font=\scriptsize, text=black}` on `LS_Plan` TikZ (`>= 9.8pt–10pt` node labels on `Teaching_Guideline` TikZ) and never apply color to `\node` text. Draw figures strictly in B&W (`black`, `white`, `gray!8`–`gray!38`/`gray!65`) with bold print-safe strokes (`line width=0.8pt`–`1.4pt`, `tk1`/`tk2` `0.85pt`). Use **`TACTENG.TTF` `'3'`** (`\Tacteing`) for `\khmflourish`.
6. **3-Folder Workspace Separation & Explicit Cleanup**:
   - Keep `01_កិច្ចតែងការបង្រៀន\` (4-document package + `ឯកសារស្រាវជ្រាវយោង_PDF\`), `02_មេរៀន\` (student lessons, worksheets, and textbooks/សៀវភៅសិក្សាគោល), and `03_ឯកសារស្រាវជ្រាវ\` (verified Open-Access PDFs in `papers\` + `Research_Brief_<Topic>.md`) strictly separate.
   - Move **ONLY explicit `<JobName>.aux`, `<JobName>.log`, `<JobName>.out`** (never `*.*` wildcards) to `01_កិច្ចតែងការបង្រៀន\_Build_Logs_and_Duplicates\`.

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
1. **`LS_Plan_<Topic>.tex`**: Sections I–IV (`longtable` `L{5.50cm}|L{7.90cm}|L{4.80cm}`), monochrome symbolic/tracing scaffolds, Numbered Warrant Bank `①–⑤`, rotated/overlapped B&W TikZ figures, `Pause-Ask`/`Pause-Review` relay, multi-foil exit checks, no internal time-summary table.
2. **`Teaching_Scenario_<Topic>.tex`**: 2-page minute-by-minute execution script synced to the 50-minute 5Es, board plan, B&W material list, and empirical misconception table.
3. **`Printable_Materials_<Topic>.tex`**: 1 kit per A4 page (`\clearpage`), pure B&W (`1.0pt`–`1.4pt`), true `1:1` `x=1cm, y=1cm` cut-outs & angle mats + calibration bar + `Actual Size 100%` note, verbatim alignment with `LS_Plan`.
4. **`Teaching_Guideline_<Topic>.tex`**: Mobile-First manual & mini-research report (`12pt` class, `11.5pt/18.2pt` prose & `scriptbox`, `10.2pt–10.8pt` tables/APA, `>= 9.8pt–10pt` TikZ labels + `10.5pt` captions, `2.30cm` top/bottom header/footer struts, systematic unwrapped `\muol` headings with `\enbf{...}` for embedded Latin/ASCII, `TACTENG` `'3'`, `Times New Roman` `\en{...}`, `Cambria Math` `Scale=1.06`) containing header/context, APA 7th mini-lit review, activity-by-activity rationale & objectives (referencing exact `Printable_Materials` pages), verbatim teacher scripts (`«គ្រូនិយាយថា៖ ...»`), troubleshooting, Evidence Table, and APA 7th Reference List matching `ឯកសារស្រាវជ្រាវយោង_PDF\` 1-to-1.

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

### Step 5: Full-Page Visual PNG Inspection (Stage 5)
Render **every page** of **all 4 compiled PDFs** to 175–190 dpi PNG via PyMuPDF and inspect **every PNG** with `read_file`:

```powershell
$scratch = "<conversation-scratch>\pages"
New-Item -ItemType Directory -Force -Path $scratch | Out-Null
Remove-Item "$scratch\*.png" -ErrorAction SilentlyContinue
python -c "import fitz; docs=['LS_Plan_<Topic>','Teaching_Scenario_<Topic>','Teaching_Guideline_<Topic>','Printable_Materials_<Topic>']; [([p.get_pixmap(dpi=190).save(rf'$scratch\{d}_p{i+1}.png') for i,p in enumerate(doc)], print(d,'PAGES:',len(doc))) for d in docs for doc in [fitz.open(rf'$dir\{d}.pdf')]]"
```

Verify visually across ALL rendered PNGs:
1. `LS_Plan`: strictly 4 balanced A4 pages (~92–98% density), clean signature block on page 4.
2. `Teaching_Scenario`: strictly 2 balanced A4 pages.
3. `Printable_Materials`: 1 kit per A4 page, pure B&W thick strokes, crisp cut lines, and true 1:1 `1 cm = 1 cm` calibration bar & cut-out proportions.
4. `Teaching_Guideline`: comfortable mobile-first readability (~13–16 A4 pages), clean `\muol` heading hierarchy with zero missing glyphs, spacious header/footer rules with zero touching ascenders/subscripts, `\en{...}` Times New Roman APA 7th citations/references, `TACTENG` `'3'`, verbatim scripts, Evidence Table, and Reference List.
5. Every TikZ label across all documents is 100% black with zero overlap, and all Khmer glyphs, bolding (`FakeBold=1.8`), slants (`FakeSlant=0.25`), math symbols, and nested tables render cleanly.
