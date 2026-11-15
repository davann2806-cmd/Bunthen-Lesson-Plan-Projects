# Bunthen Lesson Plan Projects — Workspace Rules & Memory (`អនុវិទ្យាល័យព្រះក្រសាំង`)

គោលការណ៍ទាំងនេះត្រូវអនុវត្តជាស្វ័យប្រវត្តិសម្រាប់គ្រប់កញ្ចប់ឯកសារបង្រៀន (គណិតវិទ្យា និងមុខវិជ្ជាពាក់ព័ន្ធ) នៅក្នុង Workspace នេះ ដើម្បីរក្សាស្ដង់ដារ **កញ្ចប់ឯកសារបង្រៀន ៤ ឯកសារ + ថតភស្តុតាងស្រាវជ្រាវភ្ជាប់ (4-Document Lesson Package + Attached Evidence Folder)** សម្រាប់ម៉ោងសិក្សា ៥០ នាទី គំរូ 5Es និងរចនាប័ទ្ម `ls_plan.tex` ឱ្យដូចគ្នាទាំងស្រុងសម្រាប់មេរៀនបន្តបន្ទាប់។

---

## ១. ដំណាក់កាលស្រាវជ្រាវ ផលិតកញ្ចប់ឯកសារ និងផ្ទៀងផ្ទាត់ (Mandatory 5-Stage Pipeline)
មុននឹងនិពន្ធ ឬកែលម្អកញ្ចប់ឯកសារបង្រៀនសម្រាប់មេរៀនថ្មីនីមួយៗ ត្រូវអនុវត្តលំនាំ ៥ ដំណាក់កាលតាម `.agents/skills/ngs-lesson-plan/references/research_workflow.md` ជាដាច់ខាត៖
- **ដំណាក់កាលទី ១ — រុករក និងផ្ទៀងផ្ទាត់ឯកសារ Open-Access**៖
  - ប្រើ `/swarm` (អ្នកស្រាវជ្រាវ ៣ មុំស្របគ្នា៖ `misconceptions_`, `activities_`, `proof_` និង `evidence-curator` បើពង្រីកបន្ថែម) ឬ Single-Agent តាមលំដាប់ ដើម្បីប្រមូលអត្ថបទស្រាវជ្រាវពិត (Peer-Reviewed Open-Access PDFs) តាមរយៈ **OpenAlex API** (`filter=is_oa:true`), **ERIC API** (`files.eric.ed.gov/fulltext/<ID>.pdf`), **Semantic Scholar API** (`openAccessPdf`), **DOAJ** និង `search_web` (`domain:"scholar.google.com"`, `eric.ed.gov`, `mdpi.com`, ។ល។)។
  - **ច្បាប់ប្រឆាំង CAPTCHA ដាច់ខាត**៖ **ហាម** Scrape `scholar.google.com` ដោយផ្ទាល់តាម script/browser និង **ហាម** បំបែក ឬឆ្លងកាត់ CAPTCHA / Cloudflare Turnstile / Paywall ជាដាច់ខាត។
  - រាល់ PDF ត្រូវផ្ទៀងផ្ទាត់ដោយ Python (`b'%PDF-'` magic bytes + PyMuPDF `fitz`: `>= 2` ទំព័រ និងអក្សរ `> 500` តួអក្សរ) មុនរក្សាទុកក្នុង `03_ឯកសារស្រាវជ្រាវ\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\papers\` (លុបចោលភ្លាមបើ HTML/403/ខូច) រួចអានទិន្នន័យពិតពី PDF ដោយគ្មានការប្រឌិត និងចម្លងដាក់លេខរៀង (`01_...pdf`..) ចូលថត `ឯកសារស្រាវជ្រាវយោង_PDF\` ក្នុងថតមេរៀន។
- **ដំណាក់កាលទី ២ — សំយោគគរុកោសល្យ (`Research_Brief_<Topic>.md`)**៖ សង្ខេប APA 7th Citations, DOIs/URLs, ភស្តុតាងទាំង ៣ មុំ និងតារាងបម្លែងចូលក្នុង 5Es ទាំង ៥០ នាទី។
- **ដំណាក់កាលទី ៣ — កញ្ចប់ឯកសារ ៥ ផ្នែក និងស្តង់ដារ B&W**៖
  - និពន្ធឯកសារ LaTeX ទាំង ៤ (`LS_Plan`, `Teaching_Scenario`, `Teaching_Guideline`, `Printable_Materials`) + ថត `ឯកសារស្រាវជ្រាវយោង_PDF\` ឱ្យស៊ីចង្វាក់គ្នាពាក្យ-ទល់-ពាក្យ។
  - ជំនួសការពឹងផ្អែកលើហ្វឺត/កាតពណ៌ (`២–៣ ពណ៌`) លើសន្លឹកកិច្ចការសិស្សដែលព្រីនស-ខ្មៅ ដោយប្រើ **សញ្ញាសម្គាល់ស-ខ្មៅ (Monochrome Symbolic Coding) + `[tracing]` + ធនាគារលេខហេតុផល (`①–⑤`)** (ឆ្នូត `|`/`||`, ធ្នូមុំ, ព័ទ្ធរង្វង់កំពូលរួម)។
  - បញ្ចូលរូបធរណីមាត្របង្វិល/ត្រឡប់/ត្រួតគ្នា (`~140°` ឬឆ្លុះ/ជាប់) និង Exit Foils ច្រើនទម្រង់។
- **ដំណាក់កាលទី ៤ — Compile ×2 និងសម្អាតដោយឈ្មោះឯកសារច្បាស់លាស់**៖ Compile `xelatex -interaction=nonstopmode -halt-on-error` **២ ដង** សម្រាប់ `.tex` នីមួយៗ; ផ្លាស់ទី **តែ** `<JobName>.aux`, `<JobName>.log`, `<JobName>.out` (**ហាមប្រើ wildcard `*.*`**) ទៅ `01_កិច្ចតែងការបង្រៀន\_Build_Logs_and_Duplicates\`។
- **ដំណាក់កាលទី ៥ — បម្លែង PNG និងពិនិត្យគ្រប់ទំព័រ**៖ បម្លែង PDF ទាំង ៤ ជា PNG (190 dpi) តាម `fitz` រួចបើកពិនិត្យ **គ្រប់ទំព័រទាំងអស់** ដោយ `read_file` មុនបិទបញ្ចប់។

---

## ២. ទស្សនវិជ្ជា និងគោលគំនិតបង្រៀន (Pedagogical Philosophy)
- **អត្តសញ្ញាណសាលា និងគ្រូ**៖ `មន្ទីរអប់រំ យុវជន និងកីឡា ខេត្តកំពង់ធំ` → `ការិយាល័យអប់រំ យុវជន និងកីឡា ស្រុកកំពង់ស្វាយ` → **`អនុវិទ្យាល័យព្រះក្រសាំង`** (`NGS`) | គ្រូបង្រៀន៖ **ហុក ប៊ុនថែន** (លុះត្រាតែមានការបញ្ជាក់ផ្សេង) | ព.ស. ២៥៧០ (ឆ្នាំមមី អដ្ឋស័ក) / គ.ស. ២០២៦។
- **គំរូ 5Es ស្ថាបនានិយម (Constructivist 5Es)**៖
  - `E1 - Engage`៖ ស្ថានភាពបញ្ហាពិតជាក់ស្ដែង ឬបេសកកម្មភ្ញាក់ផ្អើល (មិនចាប់ផ្ដើមដោយសូត្រនិយមន័យត្រង់ៗ)។
  - `E2 - Explore`៖ ពិសោធន៍ផ្ទាល់ដៃ / ការរកឃើញដោយសិស្ស + **POE (Predict–Observe–Explain)** + **Misconception Trap / Counter-Example**។
  - `E3 - Explain`៖ សិស្សបង្គុំទ្រឹស្ដីបទ ឬរូបមន្ត រួចសង្ខេបជាតារាង សម្មតិកម្ម--សន្និដ្ឋាន--វិបាក ភ្ជាប់ធនាគារហេតុផល (`①–⑤`)។
  - `E4 - Elaborate`៖ លំហាត់គំរូភ្ជាប់វិធីវិភាគ B&W Print-Safe (កាតស៊ើបអង្កេត ៣ ជំហាន + `[tracing]`) និងសំណួរ `EIA Looking-Back`។
  - `E5 - Evaluate`៖ Relay ក្រុម (`Pause-Ask` / `Pause-Review`) + ឆ្លើយបិទបញ្ចប់បេសកកម្ម E1 + វាយតម្លៃរហ័ស ៦០–៩០ វិនាទី (Exit Foils ៤ ទម្រង់)។
- **គោលការណ៍ភាពថ្មីជានិច្ច (Anti-Boredom / Novelty Rule)**៖ មេរៀនថ្មីនីមួយៗត្រូវប្រើសកម្មភាពបង្រៀន **ថ្មីទាំងស្រុង** ខុសពីម៉ោងមុនៗ។

---

## ៣. ច្បាប់រយៈពេល ៥០ នាទី និងកញ្ចប់ឯកសារ ៥ ផ្នែក (50-Min & 5-Part Package Standard)
- **រយៈពេលស្តង់ដារ**៖ **១ ម៉ោងសិក្សា = ៥០ នាទី** (មិនមែន ៤៥ នាទីទេ)៖
  - ជំហានទី១ (រដ្ឋបាលថ្នាក់)៖ `2 min` | ជំហានទី២ (កំណែ ≤ `3 min` + រំលឹក `3 min` + `E1 3 min`)៖ `9 min`
  - ជំហានទី៣ (`E2 11 min` + `E3 6 min`)៖ `17 min` | ជំហានទី៤ (`E4 10 min` + `E5 10 min`)៖ `20 min` | ជំហានទី៥ (កិច្ចការផ្ទះ)៖ `≤ 2 min` (**សរុប 50 min**)។
- **ស្តង់ដារ ៥ ផ្នែកក្នុងថតមេរៀននីមួយៗ (`01_កិច្ចតែងការបង្រៀន\<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\`)**៖
  1. **`LS_Plan_<Topic>.tex/.pdf`**៖ កិច្ចតែងការបង្រៀន ៥០ នាទីសង្ខេប (**៤ ទំព័រ A4 ពេញស្មើ**); ដាក់តែស្លាកក្នុងជួរដេក `\fiveE{...}` និង `\timenote{...}` (**ហាម**ដាក់តារាងបែងចែកនាទីខាងក្នុង)។
  2. **`Teaching_Scenario_<Topic>.tex/.pdf`**៖ សេណារីយ៉ូគ្រប់គ្រងនាទី-ទល់-នាទី និងក្ដារខៀន (**២ ទំព័រ A4**) ភ្ជាប់តារាងការយល់ច្រឡំតាមឯកសារស្រាវជ្រាវ។
  3. **`Teaching_Guideline_<Topic>.tex/.pdf`**៖ សៀវភៅណែនាំគ្រូ និងរបាយការណ៍ស្រាវជ្រាវគរុកោសល្យបែប **Mobile-First Readability** (អានលើទូរស័ព្ទ/ថេប្លេត លាតធម្មជាតិ ~១៣–១៦ ទំព័រ A4 កុំបង្រួម!) ដោយប្រើ `\documentclass[a4paper,12pt]{article}`, តួអក្សរស្មើ **`11.5pt / 18.2pt`** (`KhmerOSsiemreap` + `\muol` `KhmerOSmuollight` + `TACTENG` `'3'` + `Times New Roman` `\en{...}` `Scale=1.02` + `Cambria Math` `Scale=1.06`) មាន៖ ក្បាលរដ្ឋបាល/បរិបទ, APA 7th Mini-Literature Review, ហេតុផលស្រាវជ្រាវនិងវត្ថុបំណងតាមសកម្មភាព, **ពាក្យពេចន៍គ្រូនិយាយផ្ទាល់ (`«គ្រូនិយាយថា៖ ...»`)**, Troubleshooting, Evidence Table (`10.2pt`), និង APA 7th Reference List (`10.8pt`)។
  4. **`Printable_Materials_<Topic>.tex/.pdf`**៖ កញ្ចប់សម្ភារៈបោះពុម្ព B&W (១ ឈុតក្នុង ១ ទំព័រ A4, `\clearpage` ស្អាត); រាល់បន្ទះកាត់ពិសោធន៍ និងផ្ទាំងមុំត្រូវគូរក្នុងមាត្រដ្ឋាន **1:1 ពិត (`x=1cm, y=1cm`)** + បន្ទះ calibration bar (`5 cm`) និងកំណត់សម្គាល់ `Actual Size 100%`; រួមមាន កាត E4/E5, សន្លឹក Relay ៣ តួនាទី, ផ្ទាំង Warrant Bank `①–⑤`, កាត Exit ៤ ទម្រង់, និងប័ណ្ណកិច្ចការផ្ទះកាត់ចែក។
  5. **`ឯកសារស្រាវជ្រាវយោង_PDF\`**៖ ថតភស្តុតាងភ្ជាប់ក្នុងថតមេរៀន ផ្ទុក PDF Open-Access ផ្ទៀងផ្ទាត់រួចដាក់លេខរៀង (`01_...pdf`..) និង `00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` ត្រូវគ្នា ១០០% នឹងគ្រប់ APA Citation ក្នុង Guideline។

---

## ៤. រចនាប័ទ្ម និងបច្ចេកទេស LaTeX (តាមលំនាំ `ls_plan.tex`)
- **Engine & Guard**៖ `xelatex` (compile 2 ដង) + `\makeatletter\let\@expl@@@mark@update@singlecol@structures@@\relax\makeatother`។
- **ពុម្ពអក្សរផ្លូវការ (Cross-Platform `\NGSFindFonts` — Windows Local + Cloud `fonts/`)**៖
  - Main Khmer: `KhmerOSsiemreap.ttf` (`FakeBold=1.8`, `FakeSlant=0.25`), `KhmerOSmuollight.ttf` (`\muol`, កុំដាក់ fake bold លើ `\muol`), `AKbalthom Naga Bold.ttf` (`\NagaBold`), `TACTENG.TTF` (`\Tacteing` — `'3'` សម្រាប់ `\khmflourish`) តាម `Path={\NGSUserPath}` (រកឃើញស្វ័យប្រវត្តិរវាង Windows local និងថត `fonts/` ក្នុង Repo លើ Linux Cloud)
  - Math/Latin/Footer: `cambria.ttc` (`FontIndex=1, Scale=1.02`), `times.ttf` (`\en{...}` `Times New Roman` សម្រាប់ APA citations/references ក្នុង Guideline), `calibri.ttf`, `cour.ttf` (`\wcirc`) តាម `Path={\NGSSysPath}` (**ហាម**សរសេរ hardcoded Windows path ដោយគ្មាន `\NGSFindFonts`)
  - Word Wrap: `\XeTeXlinebreaklocale "km"` | `\XeTeXlinebreakskip = 0pt plus 1pt minus 0.1pt`
  - **ហាមប្រើ `\texttt{...}` ជាមួយអក្សរខ្មែរ**។ **ហាមដាក់ `-` ពីមុខ `\ditem` / `$\bullet$` / `\wcirc`**។ កាលបរិច្ឆេទខាងលើ និងហត្ថលេខាខាងក្រោម (ចន្ទគតិ + សុរិយគតិ) ត្រូវត្រូវគ្នាជានិច្ច។
- **រចនាសម្ព័ន្ធ `LS_Plan_*.tex` (បោះពុម្ព ៤ ទំព័រពេញ) vs. `Teaching_Guideline_*.tex` (Mobile-First ១៣–១៦ ទំព័រ)**៖
  - `LS_Plan` Geometry: `a4paper, left=0.95cm, right=0.95cm, top=0.85cm, bottom=0.92cm, footskip=0.52cm`។ ក្បាល ៣ ជួរ (`មន្ទីរអប់រំ... ខេត្តកំពង់ធំ` / `ការិយាល័យអប់រំ... ស្រុកកំពង់ស្វាយ` / `អនុវិទ្យាល័យព្រះក្រសាំង`) → កណ្ដាល `កិច្ចតែងការបង្រៀន` → ព័ត៌មានទូទៅ → `I. វត្ថុបំណង` (`វិជ្ជាសម្បទា`, `បំណិនសម្បទា`, `ចរិយាសម្បទា`) → `II. សម្ភារៈឧបទេស` → `III. វិធីសាស្រ្តបង្រៀន` → `IV. ដំណើរការបង្រៀន` (`longtable` `|L{5.50cm}|L{7.90cm}|L{4.80cm}|`) → ហត្ថលេខា (`គ្រូបង្រៀន` កណ្ដាល + `\vspace{32pt}` + `\hfill{\muol ហុក ប៊ុនថែន}\hspace*{1.4cm}`)។ ក្នុងតារាងតូចខាងក្នុង `longtable` **ហាមប្រើ `\rowcolor`** — ប្រើ `\cellcolor{headgray}` និងបិទដោយ `\\[2pt] \hline`។
  - `Teaching_Guideline` Mobile-First Geometry & Header/Footer Clearance: `left=1.45cm, right=1.45cm, top=2.30cm, bottom=2.30cm, headheight=18pt, headsep=0.68cm, footskip=0.88cm`, `\headrulewidth=0.4pt`, `\footrulewidth=0.4pt`, ពុម្ពក្បាល/ជើង `9.5pt` បូក vertical strut (`\rule[-3pt]{0pt}{14pt}` / `\rule{0pt}{13pt}`) កុំឱ្យជើង/សក់អក្សរខ្មែរប៉ះបន្ទាត់; ទំព័រទី១ ប្រើ `\thispagestyle{firstpage}` (លាក់ `\headrule`) + `\vspace*{-0.75cm}`។
  - ឋានានុក្រម **`\muol` (`KhmerOSmuollight`) ជាប្រព័ន្ធ និងសុវត្ថិភាព Glyph**៖ ចំណងជើងផ្លូវការ `13.5pt`/`14pt`, `\secbanner` ២ ជួរ (`12pt` `\muol` + `10pt` `\enit`), `\subsec` `11.5pt`, `phasebox`/Callout Box `11pt`, `scriptbox` `«គ្រូនិយាយថា៖` `10.8pt`, រូបទី១–៤ `10.5pt`, ក្បាលតារាង `10.2pt`, ហត្ថលេខា `11.5pt`។ **ច្បាប់ដាច់ខាត**៖ ហាមដាក់ `\muol` ក្នុង `\textbf{...}`, ហើយគ្រប់តួអក្សរឡាតាំង/លេខ/សញ្ញា ASCII (`SAS`, `E1–E5`, `POE`, `PDF`, `APA`, `#`, `&`, `/`) ខាងក្នុង `\muol` ត្រូវរុំក្នុង `\enbf{...}` (ឬ `$...$`) ជានិច្ច ព្រមទាំងពិនិត្យ `.log` ឱ្យមាន **`0 Missing character`**។

---

## ៥. ការប្រើប្រាស់ក្រដាស ពុម្ពអក្សរ និងការពិនិត្យ PNG (Page Balance & Visual Sign-Off)
- `LS_Plan`: ប្រើ `\fontsize{9.5pt}{14.0pt}\selectfont`, `\arraystretch{1.05}`, `\cfig` padding `1pt`, បំបែក **modular micro-rows** (`\\[-2pt]`), **ហាម `\pagebreak` បង្ខំ** ដើម្បីចប់លើ **៤ ទំព័រ A4 ពេញស្មើ (~៩២–៩៨%)** និងហត្ថលេខាស្អាតនៅទំព័រចុងក្រោយ។
- `Teaching_Scenario`: **២ ទំព័រ A4**។ `Teaching_Guideline`: **~១៣–១៦ ទំព័រ A4** (`11.5pt/18.2pt` body, `10.2pt–10.8pt` tables/APA, `>= 9.8pt–10pt` TikZ labels + `10.5pt` captions)។ `Printable_Materials`: **១ ឈុតក្នុង ១ ទំព័រ** ដោយ `\clearpage` គ្មានទំព័រលើស។
- បម្លែង **គ្រប់ PDF ទាំង ៤** ជា PNG (175–190 dpi) តាម `fitz` រួចពិនិត្យ **គ្រប់ទំព័រ** ជាមួយ `read_file`។

---

## ៦. ស្ដង់ដារគូររូបធរណីមាត្រ TikZ (B&W Print-Safe, 100% Black Text & 1:1 Scale)
- **អក្សរពណ៌ខ្មៅ ១០០%**៖ `every node/.style={font=\scriptsize, text=black}` ។ **ហាមដាក់ពណ៌លើ `\node` text** ជាដាច់ខាត។
- **បន្ទាត់ B&W ដិតច្បាស់**៖ ប្រើតែ `black`, `white`, `gray!8`–`gray!38` (`gray!65` សម្រាប់ស៊ុមបោះពុម្ព) និងកម្រាស់ **`line width=0.8pt`–`1.4pt`** (`tk1`/`tk2` `0.85pt`) — ហាមប្រើ `very thin` / `thin` ឬពណ៌ចម្រុះ។
- **គ្មានអក្សរជាន់គ្នា និង 1:1 Scale**៖ ទុកគម្លាតច្បាស់រវាងអក្សរ និងបន្ទាត់/ធ្នូមុំ/វត្ថុ។ រាល់សម្ភារៈកាត់ និងផ្ទាំងវាស់មុំក្នុង `Printable_Materials` ត្រូវប្រើ `x=1cm, y=1cm` ដោយគ្មានការបង្រួម (`scale=1.0`)។

---

## ៧. ឋានានុក្រមថតឯកសារ ៣ ផ្នែក និងការសម្អាត (3-Folder Hierarchy & Explicit Cleanup)
Workspace បែងចែកជា **៣ ថតធំ** តាមផ្លូវ `<ថ្នាក់>\<ជំពូក_មេរៀន>\<ចំណងជើងរង>\`៖
1. **`01_កិច្ចតែងការបង្រៀន\`**៖ ផ្ទុកកញ្ចប់ ៥ ផ្នែក (`LS_Plan_<Topic>.tex/.pdf`, `Teaching_Scenario_<Topic>.tex/.pdf`, `Teaching_Guideline_<Topic>.tex/.pdf`, `Printable_Materials_<Topic>.tex/.pdf`, និងថត `ឯកសារស្រាវជ្រាវយោង_PDF\`)។ ក្រោយ compile ត្រូវផ្លាស់ទី **តែ** `<JobName>.aux`, `<JobName>.log`, `<JobName>.out` (**ហាមប្រើ `*.*`**) ទៅ `01_កិច្ចតែងការបង្រៀន\_Build_Logs_and_Duplicates\` ដោយរក្សាទុកតែឯកសារ `.tex/.pdf` ទាំង ៤ គូ និង `ឯកសារស្រាវជ្រាវយោង_PDF\` ប៉ុណ្ណោះក្នុងថតមេរៀន។
2. **`02_មេរៀន\`**៖ ផ្ទុកឯកសារមេរៀនសិស្ស សន្លឹកកិច្ចការ និងសៀវភៅសិក្សាគោល។
3. **`03_ឯកសារស្រាវជ្រាវ\`**៖ ផ្ទុក Open-Access PDFs ដែលបានផ្ទៀងផ្ទាត់រួចនៅក្នុង `papers\` និង `Research_Brief_<Topic>.md`។

---

## ៨. គោលការណ៍ដំណើរការលើ Antigravity Cloud និង GitHub (`Bunthen-Lesson-Plan-Projects`)
- **Repository ផ្លូវការ (`Public`)**៖ `https://github.com/davann2806-cmd/Bunthen-Lesson-Plan-Projects` (Branch `main`)។
- **លំដាប់ការងារពេលបើក Session លើ Antigravity Cloud / Linux VM**៖
  1. ដំឡើងបរិស្ថាន Cloud មុនគេដោយរត់ `bash scripts/setup_cloud.sh` (ស្គ្រីបនឹងដំឡើង TeX Live XeLaTeX, PyMuPDF និងចម្លងពុម្ពអក្សរខ្មែរ-គណិតទាំង ២០ ពី `fonts/` ដោយស្វ័យប្រវត្តិ)។
  2. បន្ទាប់ពីនិពន្ធឯកសារ `.tex` ទាំង ៤ ក្នុងថតមេរៀនរួច ត្រូវ **Compile ដោយផ្ទាល់នៅលើ Antigravity Cloud** តាមពាក្យបញ្ជា៖
     `python3 scripts/compile_latex.py --target "<lesson_folder>" --in-place`
     (ធានាថា Compile `xelatex` ២ ដង, `0` LaTeX errors និង `0 Missing character: There is no`)។
  3. បម្លែងទំព័រ PDF ជា PNG តាម `fitz` ដើម្បីត្រួតពិនិត្យដោយ `read_file` និងរក្សាទុកតែ `.tex/.pdf` + `ឯកសារស្រាវជ្រាវយោង_PDF\` ក្នុងថតមេរៀន (សម្អាត `.aux`, `.log`, `.out` ចូល `01_កិច្ចតែងការបង្រៀន\_Build_Logs_and_Duplicates\` ឬទុកឱ្យ `compile_latex.py` រត់ក្នុង tmp dir)។
  4. **បញ្ជូនទាំង Source Code (`.tex`) និង PDF (`.pdf`) ចូល GitHub**៖ រាល់ពេលបញ្ចប់មេរៀនមួយ ត្រូវ `git -c core.quotePath=false add` ទាំង `.tex`, `.pdf`, និង `ឯកសារស្រាវជ្រាវយោង_PDF/` រួច `git commit` និង `git push origin main` ដើម្បីឱ្យលោកគ្រូអាចទាញយក PDF រួចរាល់ពី Public GitHub លើទូរស័ព្ទបានភ្លាមៗដោយមិនពឹង GitHub Actions។
