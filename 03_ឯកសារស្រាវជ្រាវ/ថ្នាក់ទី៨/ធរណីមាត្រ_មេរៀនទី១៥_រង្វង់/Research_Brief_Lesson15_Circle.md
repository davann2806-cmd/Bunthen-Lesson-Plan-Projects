# Research Brief (`Lesson 15 — រង្វង់`): ការសំយោគវិធីសាស្ត្របង្រៀនដោយប្រើសន្លឹកកិច្ចការជាគោល (គ្មានស្លាយ LCD)

- **មុខវិជ្ជា និងថ្នាក់**: គណិតវិទ្យា ថ្នាក់ទី៨ — **មេរៀនទី១៥ ៖ រង្វង់** (សៀវភៅសិក្សាគោល ទំព័រ ១៩៧–២០៤ / PDF ទំព័រ ២០២–២០៩)
- **គ្រឹះស្ថានសិក្សា**: អនុវិទ្យាល័យព្រះក្រសាំង ស្រុកកំពង់ស្វាយ ខេត្តកំពង់ធំ | **គ្រូបង្រៀន**: ហុក ប៊ុនថែន
- **បរិបទថ្នាក់រៀន**: **គ្មានស្លាយ LCD / គ្មានឧបករណ៍បញ្ចាំង** — ប្រើតែក្ដារខៀន ដីស បន្ទាត់-ដែកឈាន-រ៉ាព័រទ័រក្ដារខៀន សៀវភៅគោល និង **សន្លឹកកិច្ចការសិស្សបោះពុម្ព ស-ខ្មៅ (Guided-Inquiry Worksheet)** ជាគោល (គ្មានសម្ភារៈកាត់បិទស្មុគស្មាញ)។
- **កញ្ចប់ឯកសារក្នុងមួយម៉ោងសិក្សា (៥០ នាទី)**: `LS_Plan_<CODE>.tex/.pdf` + `Worksheet_<CODE>.tex/.pdf`។
- **ភស្តុតាងស្រាវជ្រាវ Open-Access**: **១១ ឯកសារ PDF** ផ្ទៀងផ្ទាត់រួច (`b'%PDF-'`, PyMuPDF `>= 8` ទំព័រ, `> 26,000` តួអក្សរ) ក្នុងថត `papers/`។

---

## ១. ផែនទីបែងចែកម៉ោងសិក្សាទាំង ៤ ម៉ោង (៤ × ៥០ នាទី) និងវិធីសាស្ត្រស្រាវជ្រាវដាច់ដោយឡែក

| ម៉ោង | កូដ | ចំណងជើងរង និងទំព័រសៀវភៅគោល | កាលបរិច្ឆេទបង្រៀន (ចន្ទគតិ & សុរិយគតិ) | វិធីសាស្ត្របង្រៀនលើសន្លឹកកិច្ចការ (No-LCD Research Methodology) |
|:---:|:---:|---|---|---|
| **១** | `CIRC1` | **១៥.១ សញ្ញាណ និងការកំណត់រង្វង់** (ទំ.១៩៧–១៩៨; លំហាត់គំរូ, ប្រតិបត្តិ; កិច្ចការផ្ទះ #6, #7 ទំ.២០៤) | ថ្ងៃចន្ទ ៥កើត ខែមិគសិរ ព.ស.២៥៧០ / ១៤ ធ្នូ ២០២៦ | **Contrasting Cases & Variation-Theory Locus Worksheet** (`Sidney et al., 2015`; `Puspitasari & Fitriatien, 2026`) — ប្រៀបធៀបករណីផ្ទុយ ៤ ករណី (១ ចំណុច, ២ ចំណុច, ៣ ចំណុចមិនរត់ត្រង់ជួរ, ៣ ចំណុចរត់ត្រង់ជួរ) និងទីតាំងរង្វង់ពីរ ($AB=6\text{ cm}$) លើក្រឡាវាស់ ១:១។ |
| **២** | `CIRC2` | **១៥.២.១ មុំផ្ចិត និងរង្វាស់ប្រវែងធ្នូ** (ទំ.១៩៩–២០០; លំហាត់គំរូ ១–២, ប្រតិបត្តិ; កិច្ចការផ្ទះ #1 ទំ.២០៤) | ថ្ងៃអង្គារ ៦កើត ខែមិគសិរ ព.ស.២៥៧០ / ១៥ ធ្នូ ២០២៦ | **POGIL (Process-Oriented Guided Inquiry Learning) + Double-Scale Proportional Ratio Table** (`Ruder et al., 2020`; `De Bock et al., 2003`) — តារាងសមាមាត្រពីរជួរ ($360^\circ \leftrightarrow 2\pi r$, $90^\circ$, $1^\circ$, $n^\circ$) បំបាត់ការច្រឡំរង្វាស់មុំធ្នូ ($^\circ$) នឹងប្រវែងធ្នូ ($\text{cm}$)। |
| **៣** | `CIRC3` | **១៥.២.២ ធ្នូ និងអង្កត់ធ្នូ** (ទំ.២០០–២០១; លំហាត់គំរូ ១–៣; កិច្ចការផ្ទះ #2, #3, #5 ទំ.២០៤) | ថ្ងៃពុធ ៧កើត ខែមិគសិរ ព.ស.២៥៧០ / ១៦ ធ្នូ ២០២៦ | **POE (Predict–Observe–Explain) + Backward-Faded Proof Worksheet with Warrant Bank `①–⑤`** (`Winer & Battista, 2022`; `Yeo & Tzeng, 2019`; `Mosia et al., 2023`) — វាស់ផ្ទៀងលើរូប ១:១ រួចបំពេញសម្រាយបញ្ជាក់បន្ថយជំនួយជាជំហាន ($AB_{\text{អង្កត់ផ្ចិត}} > CD$, $MN=PQ \iff \widehat{MN}=\widehat{PQ}$)। |
| **៤** | `CIRC4` | **១៥.២.៣ លក្ខណៈឆ្លុះនៃរង្វង់ និងលំហាត់សំយោគ** (ទំ.២០២–២០៤; លំហាត់គំរូ ១–២, ប្រតិបត្តិ, #4; កិច្ចការផ្ទះ #8, #9, #10 ទំ.២០៤) | ថ្ងៃព្រហស្បតិ៍ ៨កើត ខែមិគសិរ ព.ស.២៥៧០ / ១៧ ធ្នូ ២០២៦ | **Van Hiele Guided-Orientation Symmetry + Erroneous-Example Diagnostic Worksheet** (`Arlianti et al., 2025`; `Puspitasari & Fitriatien, 2026`; `Mifetu & Larbi, 2026`) — ស្វែងរកអ័ក្សឆ្លុះអង្កត់ផ្ចិតកែងអង្កត់ធ្នូ និងវិនិច្ឆ័យកំហុស «អង្កត់ផ្ចិតកាត់ចំកណ្ដាលអង្កត់ផ្ចិតមួយទៀតតែមិនកែង»។ |

---

## ២. កំហុសបោះពុម្ពក្នុងសៀវភៅគោល (MoEYS Textbook Errata) ដែលត្រូវកែតម្រូវក្នុងមេរៀន

1. **ទំព័រ ២០០ (`លំហាត់គំរូ ១`)**: សរសេរ `P = 2 × 3.14 × 10 = 62.832 dm` និង `l = 6.2832 dm` (តាមពិតប្រើ $\pi \approx 3.1416$ តែសរសេរ `3.14`) — ក្នុងមេរៀនត្រូវបញ្ជាក់ច្បាស់ថា បើប្រើ $\pi \approx 3.1416$ បាន $P \approx 62.832\text{ dm}, l \approx 6.2832\text{ dm}$ (ឬបើ $\pi \approx 3.14$ បាន $62.8\text{ dm}$ និង $6.28\text{ dm}$)।
2. **ទំព័រ ២០០ (`លំហាត់គំរូ ២`)**: ក្នុងប្រភាគសរសេរខុសខ្នាត `94.2 dm × 80°` ជំនួសឱ្យ `94.2 cm × 80°` (ខណៈចម្លើយចុងក្រោយ `20.93 cm` ជា $\text{cm}$) — កែខ្នាតទៅជា `94.2 cm` ឱ្យឯកភាព។
3. **ទំព័រ ២០១ (`លំហាត់គំរូ ២`)**: ឃ្លាចុងក្រោយសរសេរច្រំដែល `នាំឱ្យអង្កត់ធ្នូ MN = PQ` (ដែលជាសម្មតិកម្មស្រាប់) — សម្រួលឱ្យច្បាស់លើសន្និដ្ឋាន `ធ្នូ MN = ធ្នូ PQ`។
4. **ទំព័រ ២០៤ (`លំហាត់ទី៣` និង `លំហាត់ទី៨`)**:
   - លំហាត់ទី៣ បោះពុម្ព `Q(O, r)` ជំនួស `C(O, r)`។
   - លំហាត់ទី៨ បោះពុម្ព `គូសអង្កត់ AP និង DS កែងនឹង CD ... បង្ហាញថា PC = DS` ខណៈរូបភាពមានអង្កត់ផ្ចិត $AB$ — កែតម្រូវជា `គូសអង្កត់ AP និង BS កែងនឹងបន្ទាត់ CD (ត្រង់ P និង S) ... បង្ហាញថា PC = SD` (ព្រោះចំណោលកែងពីផ្ចិត $O$ មក $CD$ ជាចំណុចកណ្ដាល $H$ នៃ $CD$ និងជាចំណុចកណ្ដាលនៃ $PS$ តាមចតុកោណព្នាយកែង $APSB$)។

---

## ៣. បញ្ជីឯកសារយោង Open-Access ផ្ទៀងផ្ទាត់រួច (APA 7th Edition — 11 PDFs)

1. **Puspitasari, A., & Fitriatien, S. R. (2026).** Exploring learning obstacles in circle and chord geometry through diagnostic assessment: Evidence from Indonesian senior high school students. *Journal of Advanced Sciences and Mathematics Education*, *6*(3), 23–46. `https://doi.org/10.58524/jasme.v6i3.1404` (`01_Puspitasari2026_CircleChordObstacles.pdf`)
2. **Mosia, M., Matabane, M. E., & Moloi, T. J. (2023).** Errors and misconceptions in Euclidean geometry problem solving questions: The case of Grade 12 learners. *Research in Social Sciences and Technology*, *8*(3), 89–104. `https://doi.org/10.46303/ressat.2023.23` (`02_Mosia2023_EuclideanGeometryMisconceptions.pdf`)
3. **Mifetu, R. K., & Larbi, E. (2026).** Enhancing students’ interest, self-efficacy, and achievement in circle geometry through Think-Pair-Share integrated with GeoGebra. *Journal of Mathematics Science and Technology Education*, *3*(2), 73–86. `https://doi.org/10.12973/jmste.3.2.73` (`03_Mifetu2026_CircleGeometryThinkPairShare.pdf`)
4. **Ruder, S., Brown, P. J. P., & Stanford, C. (2020).** Developing POGIL materials: Writing and refining activities for a spectrum of content areas. *Journal on Excellence in College Teaching*, *31*(1), 195–228. ERIC `EJ1251897`. (`04_EJ1251897_DevelopingPOGILMaterials.pdf`)
5. **Sidney, P. G., Hattikudur, S., & Alibali, M. W. (2015).** How do contrasting cases and self-explanation promote learning? Evidence from fraction division. *Learning and Instruction*, *40*, 29–38. `https://doi.org/10.1016/j.learninstruc.2015.07.006` (`05_Sidney2015_ContrastingCasesSelfExplanation.pdf`)
6. **Hlongwana, P., Mudaly, V., & Zulu, M. W. (2025).** Enhancing geometry problem-solving through visualization for multilingual learners. *EURASIA Journal of Mathematics, Science and Technology Education*, *21*(7), Article em2662. `https://doi.org/10.29333/ejmste/16564` (`06_Hlongwana2025_GeometryVisualization.pdf`)
7. **Arlianti, N., Kamid, K., Marzal, J., & Hasibuan, M. H. E. (2025).** Improving geometry transformation thinking skills using student activity sheets based on discovery-contextual learning based on Van Hiele's theory. *Jurnal Penelitian Pendidikan Indonesia*, *11*(3), 1–13. `https://doi.org/10.29210/020254836` (`07_Arlianti2025_VanHieleDiscoveryWorksheets.pdf`)
8. **De Bock, D., Verschaffel, L., Janssens, D., Van Dooren, W., & Claes, K. (2003).** Do realistic contexts and graphical representations always have a beneficial impact on students’ performance? *Learning and Instruction*, *13*(4), 441–463. (`08_DeBock2003_GraphicalNonLinear.pdf`)
9. **Dietiker, L., Brakoniecki, A., & Riling, M. (2017).** The changing expectations for the reading of geometric diagrams. *PME-NA 39* (pp. 136–143). ERIC `ED581303`. (`09_Dietiker2017_ReadingGeometricDiagrams.pdf`)
10. **Winer, M. L., & Battista, M. T. (2022).** Investigating students' proof reasoning: Analyzing students' oral proof explanations and their written proofs in high school geometry. *IEJME*, *17*(2), Article em0677. (`10_Winer2022_ProofReasoningGaps.pdf`)
11. **Yeo, L.-M., & Tzeng, Y.-T. (2019).** Tracing effect in the worked examples-based learning: An exploration of individual differences in working memory capacity. *EJMSTE*, *15*(10), Article em1760. (`11_Yeo2019_FingerTracingWorkedExamples.pdf`)
