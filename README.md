# NGS Lesson Plan — គណិតវិទ្យា ថ្នាក់ទី៨ (Cloud XeLaTeX + Antigravity Ready)

ឃ្លាំងកូដ LaTeX (`.tex`), ពុម្ពអក្សរខ្មែរ-គណិត (`fonts/`), សៀវភៅសិក្សាគោល PDF (`02_មេរៀន/`), ឯកសារស្រាវជ្រាវ Open-Access (`03_ឯកសារស្រាវជ្រាវ/`), និង Skills/Rules (`.agents/skills/`, `GEMINI.md`) សម្រាប់ដំណើរការការងារ **នៅលើ Cloud ១០០%** ដោយមិនរំខានពេលកុំព្យូទ័រផ្ទាល់ដាច់ភ្លើង។

---

## ១. រចនាសម្ព័ន្ធឃ្លាំងកូដ (Repository Layout)
- `01_កិច្ចតែងការបង្រៀន/` — កញ្ចប់ឯកសារ ៥ ផ្នែក (`LS_Plan_*.tex/.pdf`, `Teaching_Scenario_*.tex/.pdf`, `Printable_Materials_*.tex/.pdf`, `Teaching_Guideline_*.tex/.pdf`, និង `ឯកសារស្រាវជ្រាវយោង_PDF/`)
- `02_មេរៀន/` — សៀវភៅសិក្សាគោល MoEYS (ថ្នាក់ទី៧–៩ PDF), ស្លាយបង្រៀន និងសន្លឹកកិច្ចការសិស្ស
- `03_ឯកសារស្រាវជ្រាវ/` — `lesson12_roadmap.md`, `Research_Brief_*.md` និងឯកសារ Open-Access PDFs (`papers/`)
- `fonts/` — ពុម្ពអក្សរចាំបាច់ទាំង ២០ (`KhmerOSsiemreap.ttf`, `KhmerOSmuollight.ttf`, `TACTENG.TTF`, `cambria.ttc`, `times*.ttf`, `calibri*.ttf`, `cour*.ttf`, ។ល។) ដែល `.tex` ទាំងអស់រកឃើញដោយស្វ័យប្រវត្តិតាម `\NGSFindFonts`
- `.agents/skills/` & `GEMINI.md` — ច្បាប់ និងជំនាញបង្រៀន (`ngs-lesson-plan`, `latex`) សម្រាប់ AI Agent ទាំងលើ Windows និង Cloud
- `.github/workflows/build-latex.yml` — Workflow **Compile `xelatex` ស្វ័យប្រវត្តិលើ GitHub Cloud**
- `.devcontainer/devcontainer.json` — បរិស្ថាន **GitHub Codespaces** (`Ubuntu 24.04 + TeX Live + PyMuPDF + Khmer Fonts`)

---

## ២. របៀបប្រើប្រាស់ពីទូរស័ព្ទ (មិនពឹងអគ្គិសនីកុំព្យូទ័រនៅផ្ទះ)

### វិធីទី A៖ ប្រើតាម Antigravity Remote Agents (`antigravity.google`)
1. ចូលទៅកាន់ [antigravity.google](https://antigravity.google) លើ Browser ទូរស័ព្ទ (ឬ PWA App)។
2. ភ្ជាប់ GitHub Account របស់លោកគ្រូ (`davann2806-cmd`) រួចជ្រើសរើស Repository **`davann2806-cmd/ngs-lesson-plan`** (Branch `main`)។
3. ឆាតបញ្ជា AI នៅលើ Cloud ដើម្បីបង្កើតមេរៀនបន្ត (ឧ. Slice 7/12 `៣.២ វិសមភាពត្រីកោណ` តាម `03_.../lesson12_roadmap.md`) — នៅពេល push កូដ `.tex` ចូល `main`, **GitHub Actions** នឹង Compile `xelatex` ចេញជា `.pdf` ដោយស្វ័យប្រវត្តិ និងរក្សាទុកត្រឡប់ចូល Repo + Artifacts។

### វិធីទី B៖ ប្រើតាម GitHub Codespaces + `agy remote-control start`
1. នៅលើទូរស័ព្ទ ឬ Browser ណាមួយ បើក Repo `davann2806-cmd/ngs-lesson-plan` → ចុច **`<> Code` → `Codespaces` → `Create codespace on main`**។
2. Codespace នឹងដំឡើង TeX Live + PyMuPDF + ពុម្ពអក្សរខ្មែរ (`bash scripts/setup_cloud.sh`) ដោយស្វ័យប្រវត្តិ។
3. បើដំឡើង `agy` CLI ក្នុង Codespace រួចបើក `agy remote-control start` នោះលោកគ្រូអាចប្រើផ្ទាំង **Remote Control** លើទូរស័ព្ទបានដូចម៉ាស៊ីននៅផ្ទះបេះបិទ។

### វិធីទី C៖ ទាញយក PDF ដែល Compile លើ Cloud (GitHub Actions)
- រាល់ពេលមានការបញ្ជូនកូដ `.tex` ឬចុច **Actions → `Build NGS Khmer XeLaTeX PDFs` → `Run workflow`** ម៉ាស៊ីន Cloud នឹង Compile `xelatex` ២ ដង, ពិនិត្យ `0 Missing character`, បញ្ជូន `.pdf` ចូល Repo (`[skip ci]`), និងបង្កើតកញ្ចប់ទាញយក **`compiled-khmer-pdfs`** នៅខាងក្រោម Workflow Run។

---

## ៣. ការ Compile ដោយដៃលើ Cloud / Codespaces
```bash
bash scripts/setup_cloud.sh
python3 scripts/compile_latex.py --target "01_កិច្ចតែងការបង្រៀន/ថ្នាក់ទី៨/ធរណីមាត្រ_មេរៀនទី១២_ការប្រៀបធៀបត្រីកោណ/៣.១_វិសមភាពចំពោះជ្រុងនិងមុំនៃត្រីកោណមួយ" --in-place
```
