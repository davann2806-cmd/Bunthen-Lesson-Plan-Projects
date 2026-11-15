# Bunthen Lesson Plan Projects

គម្រោង **Bunthen Lesson Plan Projects** (`https://github.com/davann2806-cmd/Bunthen-Lesson-Plan-Projects` — **Public Repository**) ផ្ទុកកូដ LaTeX (`.tex`), ឯកសារបង្រៀន PDF រួចរាល់ (`.pdf`), ពុម្ពអក្សរខ្មែរ-គណិត (`fonts/`), សៀវភៅសិក្សាគោល PDF (`02_មេរៀន/`), ឯកសារស្រាវជ្រាវ Open-Access (`03_ឯកសារស្រាវជ្រាវ/`), និង Skills/Rules (`.agents/skills/`, `GEMINI.md`) សម្រាប់ដំណើរការការងារ **Compile នៅលើ Antigravity Cloud ១០០% ហើយបញ្ជូនទាំង Source Code និង PDF ចូល GitHub** ដោយគ្មានការរំខានពីការដាច់ភ្លើងកុំព្យូទ័រ។

---

## ១. លំដាប់ការងារលើ Cloud ពីទូរស័ព្ទ (Antigravity Cloud → GitHub Public)

1. **បើក Remote Chat តាម Antigravity (`https://antigravity.google`)**៖
   - បើក Browser លើទូរស័ព្ទ (ឬ PWA App) → ភ្ជាប់ GitHub `davann2806-cmd/Bunthen-Lesson-Plan-Projects` (`main`)។
   - ឆាតបញ្ជា AI Agent ឱ្យបន្តនិពន្ធមេរៀនបន្ទាប់ (ឧ. Slice 7/12 `៣.២ វិសមភាពត្រីកោណ` តាម `03_.../lesson12_roadmap.md`)។
2. **Compile នៅលើ Antigravity Cloud ដោយផ្ទាល់**៖
   - AI Agent លើ Antigravity Cloud នឹងរត់ `bash scripts/setup_cloud.sh` (ដំឡើង TeX Live XeLaTeX + PyMuPDF + ពុម្ពអក្សរខ្មែរ-គណិតទាំង ២០) រួច Compile ឯកសារ `.tex` ចេញជា `.pdf` ដោយស្វ័យប្រវត្តិតាម `scripts/compile_latex.py --target ... --in-place`។
3. **បញ្ជូនទាំង `.tex` និង `.pdf` មក Public GitHub**៖
   - ក្រោយពិនិត្យ PNG គ្រប់ទំព័ររួច Agent នឹង `commit` និង `push` ទាំង `.tex`, `.pdf`, និង `ឯកសារស្រាវជ្រាវយោង_PDF/` មក Branch `main` នៃ Repository នេះ។
4. **មើល និងទាញយក PDF ពីទូរស័ព្ទភ្លាមៗ (Public Access)**៖
   - ដោយសារ Repo នេះជា **Public** លោកគ្រូអាចបើកតំណ [`https://github.com/davann2806-cmd/Bunthen-Lesson-Plan-Projects`](https://github.com/davann2806-cmd/Bunthen-Lesson-Plan-Projects) ពីទូរស័ព្ទ ឬកុំព្យូទ័រណាមួយដើម្បីទាញយក PDF យកទៅព្រីនបានភ្លាមៗ ឬ `git pull` យកមកម៉ាស៊ីននៅផ្ទះដោយឥតគិតថ្លៃ។

---

## ២. រចនាសម្ព័ន្ធឃ្លាំងកូដ (Repository Layout)
- `01_កិច្ចតែងការបង្រៀន/` — កញ្ចប់ឯកសារ ៥ ផ្នែក (`LS_Plan_*.tex/.pdf`, `Teaching_Scenario_*.tex/.pdf`, `Printable_Materials_*.tex/.pdf`, `Teaching_Guideline_*.tex/.pdf`, និង `ឯកសារស្រាវជ្រាវយោង_PDF/`)
- `02_មេរៀន/` — សៀវភៅសិក្សាគោល MoEYS (ថ្នាក់ទី៧–៩ PDF), ស្លាយបង្រៀន និងសន្លឹកកិច្ចការសិស្ស
- `03_ឯកសារស្រាវជ្រាវ/` — `lesson12_roadmap.md`, `Research_Brief_*.md` និងឯកសារ Open-Access PDFs (`papers/`)
- `fonts/` — ពុម្ពអក្សរចាំបាច់ទាំង ២០ (`KhmerOSsiemreap.ttf`, `KhmerOSmuollight.ttf`, `TACTENG.TTF`, `cambria.ttc`, `times*.ttf`, `calibri*.ttf`, `cour*.ttf`, ។ល។) ដែល `.tex` ទាំងអស់រកឃើញដោយស្វ័យប្រវត្តិតាម `\NGSFindFonts`
- `.agents/skills/` & `GEMINI.md` — ច្បាប់ និងជំនាញបង្រៀន (`ngs-lesson-plan`, `latex`) និងលំដាប់ការងារលើ Antigravity Cloud
- `scripts/setup_cloud.sh` & `scripts/compile_latex.py` — ស្គ្រីបដំឡើង XeLaTeX + PyMuPDF + ពុម្ពអក្សរ និង Compile PDF ផ្ទៀងផ្ទាត់ `0 missing characters`
- `.devcontainer/devcontainer.json` — បរិស្ថាន Cloud Ubuntu `24.04` (`Codespaces` / Dev Container)
- `.github/workflows/build-latex.yml` — Workflow `workflow_dispatch` (បម្រុងសម្រាប់ចុចរត់ដោយដៃ ប្រសិនបើថ្ងៃក្រោយបើក GitHub Actions ប្រើបន្ថែម)

---

## ៣. ការ Compile ដោយដៃលើ Cloud Linux / Codespaces / Antigravity VM
```bash
bash scripts/setup_cloud.sh
python3 scripts/compile_latex.py --target "01_កិច្ចតែងការបង្រៀន/ថ្នាក់ទី៨/ធរណីមាត្រ_មេរៀនទី១២_ការប្រៀបធៀបត្រីកោណ/៣.១_វិសមភាពចំពោះជ្រុងនិងមុំនៃត្រីកោណមួយ" --in-place
```
