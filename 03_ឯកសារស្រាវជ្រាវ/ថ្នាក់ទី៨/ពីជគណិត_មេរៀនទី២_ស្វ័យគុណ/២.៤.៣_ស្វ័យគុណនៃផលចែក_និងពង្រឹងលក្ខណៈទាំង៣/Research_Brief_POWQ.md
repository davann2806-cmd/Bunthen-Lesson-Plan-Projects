# សង្ខេបការស្រាវជ្រាវគរុកោសល្យ (Research Brief `_POWQ`): ២.៤.៣ ស្វ័យគុណនៃផលចែក និងពង្រឹងលក្ខណៈទាំង ៣ (ថ្នាក់ទី៨)

- **បរិបទបង្រៀន**: គណិតវិទ្យា ថ្នាក់ទី៨ — ពីជគណិត មេរៀនទី២៖ ស្វ័យគុណ (`៤.៣ ស្វ័យគុណនៃផលចែក` និង `ពង្រឹងលក្ខណៈទាំង ៣`៖ $(a^m)^n$, $(ab)^n$, $\left(\frac{a}{b}\right)^n$) | អនុវិទ្យាល័យព្រះក្រសាំង (`NGS`, ស្រុកកំពង់ស្វាយ ខេត្តកំពង់ធំ) | គ្រូបង្រៀន៖ **ហុក ប៊ុនថែន** | កាលបរិច្ឆេទបង្រៀន៖ `ថ្ងៃចន្ទ ទី១៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦` (`ថ្ងៃចន្ទ ៧កើត ខែកត្តិក ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០`)។
- **កញ្ចប់ឯកសារបង្រៀនគោលដៅ** (`01_កិច្ចតែងការបង្រៀន\ថ្នាក់ទី៨\ពីជគណិត_មេរៀនទី២_ស្វ័យគុណ\២.៤.៣_ស្វ័យគុណនៃផលចែក_និងពង្រឹងលក្ខណៈទាំង៣\`)៖
  - `LS_Plan_POWQ.tex` (៥០ នាទី, គំរូ 5Es, `៤–៨+` ទំព័រ A4 បត់បែនតាមខ្លឹមសារជាក់ស្ដែង, ពេញទំព័រ `>= 90%`)
  - `Teaching_Scenario_POWQ.tex` (`២–៤` ទំព័រ A4 តាមខ្លឹមសារជាក់ស្ដែង, ពេញទំព័រ `>= 90%`)
  - `Teaching_Guideline_POWQ.tex` (សៀវភៅណែនាំគ្រូ & របាយការណ៍ស្រាវជ្រាវ APA 7th, Mobile-First `~14–20` ទំព័រ, `breakable` boxes)
  - `Printable_Materials_POWQ.tex` (សម្ភារៈបោះពុម្ព B&W មាត្រដ្ឋាន `1:1` ពិត, ១ ឈុតក្នុង ១ ទំព័រ A4, គ្មានការពឹងផ្អែកលើហ្វឺតពណ៌)
  - `ឯកសារស្រាវជ្រាវយោង_PDF\` (`00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` + `01_Fitria2023...pdf` .. `15_Yeo2019...pdf`)
- **ប្រភពសៀវភៅសិក្សាគោល**: MoEYS គណិតវិទ្យា ថ្នាក់ទី៨ (`Book pp. 17–18, 25–26` = `PDF pp. 22–23, 30–31`)
- **ស្ថានភាពឯកសារស្រាវជ្រាវ Open-Access**: **១៥ PDF** ផ្ទៀងផ្ទាត់រួច (`b'%PDF-'`, `PyMuPDF fitz` `7–39` ទំព័រ, `23,555–112,136` តួអក្សរ, `245,539–7,497,112` បៃ, **SHA-256 ដូចគ្នា ១០០%** រវាង `papers\` និង `ឯកសារស្រាវជ្រាវយោង_PDF\`)។

---

## ១. ការផ្ទៀងផ្ទាត់ខ្លឹមសារសៀវភៅសិក្សាគោល (Textbook Ground-Truth Audit: `Book pp. 17–18, 25–26`)

ការពិនិត្យផ្ទាល់លើរូបភាពទំព័រសៀវភៅសិក្សាគោល (`pdf_p22_book_p17.png`, `pdf_p23_book_p18.png`, `pdf_p30_book_p25.png`, `pdf_p31_book_p26.png`) បញ្ជាក់ខ្លឹមសារពាក្យ-ទល់-ពាក្យសម្រាប់ឯកភាពគ្នានៅក្នុងឯកសារ LaTeX ទាំង ៤៖

### ១.១ កំណែកិច្ចការផ្ទះ (`ប្រតិបត្តិ 4.2`, `Book p. 18` ធៀប `p. 17`)
- **ក.** $-2(a^{-3}\cdot b^5)^2 = -2(a^{-6}\cdot b^{10}) = -2a^{-6}b^{10} = -\dfrac{2b^{10}}{a^6}$ *(សញ្ញាដក និងមេគុណ `-2` ស្ថិតនៅ **ក្រៅ** វង់ក្រចក មិនមែន `(-2)^2` ឡើយ; $a \neq 0$)*។
- **ខ.** $a\cdot(a^4)^5\cdot a^{-6} = a^1\cdot a^{20}\cdot a^{-6} = a^{1+20-6} = a^{15}$ *(កំណត់សម្គាល់ពុម្ពសៀវភៅ៖ ទំព័រ 17 `ប្រតិបត្តិ ខ` បោះពុម្ព $a\cdot(a^4)^5\cdot a^{-6} = a^{15}$ រីឯទំព័រ 18 `ប្រតិបត្តិ ខ` បោះពុម្ពបាត់និទស្សន្តក្រៅ `5` ក្លាយជា $a\cdot(a^4)\cdot a^{-6} = a^{1+4-6} = a^{-1} = \frac{1}{a}$ — គ្រូត្រូវបង្ហាញការផ្ទៀងផ្ទាត់ទាំងទម្រង់ត្រឹមត្រូវ $a^{15}$ និងកំណត់សម្គាល់ពុម្ពទំព័រ 18 $a^{-1}$ ដើម្បីការពារការភាន់ច្រឡំរបស់សិស្ស)*។

### ១.២ ផ្នែក `4.3. ស្វ័យគុណនៃផលចែក` (`Book p. 18` / `PDF p. 23`)
- **ឧទាហរណ៍ : សរសេរកន្សោមខាងក្រោមដោយប្រើនិទស្សន្តតែមួយ**៖
  - **ក.** $\dfrac{2^3}{5^3} = \dfrac{\overbrace{2\times 2\times 2}^{3\text{ កត្តា}}}{\underbrace{5\times 5\times 5}_{3\text{ កត្តា}}} = \underbrace{\left(\dfrac{2}{5}\right)\left(\dfrac{2}{5}\right)\left(\dfrac{2}{5}\right)}_{3\text{ កត្តា}} = \left(\dfrac{2}{5}\right)^3$ `។`
  - **ខ.** $\dfrac{a^n}{b^n} = \dfrac{\overbrace{a\cdot a\cdot \ldots a}^{n\text{ កត្តា}}}{\underbrace{b\cdot b\cdot \ldots b}_{n\text{ កត្តា}}} = \underbrace{\left(\dfrac{a}{b}\right)\cdot\left(\dfrac{a}{b}\right)\cdot\ldots \left(\dfrac{a}{b}\right)}_{n\text{ កត្តា}} = \left(\dfrac{a}{b}\right)^n$ `។`
- **ជាទូទៅ (ប្រអប់ទ្រឹស្ដីបទ `4.3`, `Book p. 18`)**៖
  `បើ a , b ជាចំនួនសនិទានខុសពីសូន្យនិង n ជាចំនួនគត់រ៉ឺឡាទីបខុសពីសូន្យ គេបាន` $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ `។`
  *(សុក្រឹតភាពបន្ថែមក្នុង `E3` និង `Teaching_Guideline`៖ ទម្រង់សមមូលពីរទិស $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n} \Leftrightarrow \frac{a^n}{b^n} = \left(\frac{a}{b}\right)^n$ និងច្បាប់ច្រាសនិទស្សន្តដក $\left(\frac{a}{b}\right)^{-n} = \frac{a^{-n}}{b^{-n}} = \frac{b^n}{a^n} = \left(\frac{b}{a}\right)^n$)*។
- **លំហាត់គំរូទី 1 : សម្រួលកន្សោម (`Book p. 18`)**៖
  - **ក.** $\left(\dfrac{3}{4}\right)^3 = \dfrac{3^3}{4^3} = \dfrac{27}{64}$ `។`
  - **ខ.** $\left(\dfrac{a^2b^3}{c^{-2}}\right)^3 = \dfrac{(a^2)^3(b^3)^3}{(c^{-2})^3} = \dfrac{a^6b^9}{c^{-6}} = a^6b^9c^6$ `។` *($c \neq 0$)*
- **ប្រតិបត្តិ : សម្រួលកន្សោម (`Book p. 18`)**៖
  - **ក.** $\left(\dfrac{-2}{3}\right)^4 = \dfrac{(-2)^4}{3^4} = \dfrac{16}{81}$ `។`
  - **ខ.** $\left(\dfrac{a^4\cdot b^{-2}}{c^3}\right)^2 = \dfrac{(a^4)^2(b^{-2})^2}{(c^3)^2} = \dfrac{a^8b^{-4}}{c^6} = \dfrac{a^8}{b^4c^6}$ `។` *($b, c \neq 0$)*

### ១.៣ កិច្ចការផ្ទះពីលំហាត់ជំពូក (`Book pp. 25–26` / `PDF pp. 30–31`)
- **`#6 គ` (`p. 25`)**: $\left(\dfrac{4}{3}\right)^4\left(\dfrac{4}{3}\right)^{-6}\left(\dfrac{4}{3}\right)^3 = \left(\dfrac{4}{3}\right)^{4-6+3} = \left(\dfrac{4}{3}\right)^1 = \dfrac{4}{3}$ `។`
- **`#7 ង` (`p. 25`)**: $\dfrac{(32a^2x^8)^3}{(5ax)(-2a^2x^2)^2(-4a^3x)^3} = \dfrac{(2^5)^3 a^6 x^{24}}{(5ax)(4a^4x^4)(-64a^9x^3)} = \dfrac{2^{15} a^6 x^{24}}{-5\cdot 2^8 a^{14} x^8} = -\dfrac{2^7 x^{16}}{5a^8} = -\dfrac{128x^{16}}{5a^8}$ *($a,x \neq 0$)*។
- **`#8 ក, គ` (`p. 26`)**:
  - **ក.** សរសេរ $x^{12}$ ជាស្វ័យគុណនៃ $x^2$ $\implies x^{12} = (x^2)^6$ `។`
  - **គ.** *(សៀវភៅខ្វះ `.` ក្រោយ `គ`)* សរសេរ $2^{18}$ និង $(2^5)^6$ ជាស្វ័យគុណនៃ $8$ $\implies 2^{18} = (2^3)^6 = 8^6$ និង $(2^5)^6 = 2^{30} = (2^3)^{10} = 8^{10}$ `។`

---

## ២. បញ្ជីឯកសារយោងដែលបានផ្ទៀងផ្ទាត់ (Verified Open-Access Sources: `15` PDFs)

តារាងខាងក្រោមផ្គូផ្គង ១-ទល់-១ ជាមួយលេខរៀង `01–15` ក្នុងថត `ឯកសារស្រាវជ្រាវយោង_PDF\` (`00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md`) រៀបតាមអក្ខរក្រមនាមត្រកូលអ្នកនិពន្ធទី១៖

| # | ឯកសារ PDF (`papers/`) | ឯកសារភ្ជាប់ (`ឯកសារស្រាវជ្រាវយោង_PDF\`) | ទំព័រ (Chars) | SHA-256 (12) | APA 7th Citation & Official OA URL/DOI | មុំស្រាវជ្រាវ |
|---:|---|---|---:|---|---|---|
| **01** | [misconceptions_2023_fitria.pdf](papers/misconceptions_2023_fitria.pdf) | `01_Fitria2023_AlgebraMisconceptionsMap.pdf` | 27 (72,440) | `104bada493b3` | Fitria, A., Subanji, Susiswo, & Susanto, H. (2023). Cognitive map: Diagnosing and exploring students' misconceptions in algebra. *Mathematics Teaching Research Journal*, *15*(5), 49–75. \| ERIC (`EJ1412238`): https://files.eric.ed.gov/fulltext/EJ1412238.pdf | Misconceptions |
| **02** | [activities_2017_johanning.pdf](papers/activities_2017_johanning.pdf) | `02_Johanning2017_FractionMultiplicationQuestioning.pdf` | 7 (28,543) | `84cfb1320b0b` | Johanning, D. I. (2017). A questioning framework for supporting fraction multiplication understanding. In E. Galindo & J. Newton (Eds.), *Proceedings of the 39th Annual Meeting of the North American Chapter of the International Group for the Psychology of Mathematics Education* (pp. 188–194). Hoosier Association of Mathematics Teacher Educators. \| ERIC (`ED581300`): https://files.eric.ed.gov/fulltext/ED581300.pdf | Hands-on / Area Grid |
| **03** | [misconceptions_2021_kshetree.pdf](papers/misconceptions_2021_kshetree.pdf) | `03_Kshetree2021_EighthGradeMisconceptions.pdf` | 21 (90,797) | `0c28dc2a9e3a` | Kshetree, M. P., Acharya, B. R., Khanal, B., Panthi, R. K., & Belbase, S. (2021). Eighth grade students’ misconceptions and errors in mathematics learning in Nepal. *European Journal of Educational Research*, *10*(3), 1101–1121. https://doi.org/10.12973/eu-jer.10.3.1101 \| ERIC (`EJ1307676`): https://files.eric.ed.gov/fulltext/EJ1307676.pdf | Misconceptions |
| **04** | [activities_2026_leton.pdf](papers/activities_2026_leton.pdf) | `04_Leton2026_ExponentsMathLiteracy.pdf` | 20 (60,689) | `2c0566397ab9` | Leton, S. I., Lakapu, M., Jagom, Y. O., Djong, K. D., Dosinaeng, W. B. N., & Kusuma, D. A. (2026). Integrating augmented reality and local wisdom in teaching exponents: A strategy to improve students’ mathematical literacy. *Infinity Journal*, *15*(3), 901–920. https://doi.org/10.22460/infinity.v15i3.p901-920 \| OA PDF: https://e-journal.stkipsiliwangi.ac.id/index.php/infinity/article/download/7252/2557 | Hands-on / Exponents |
| **05** | [misconceptions_2011_olson.pdf](papers/misconceptions_2011_olson.pdf) | `05_Olson2011_NegativeSignAmbiguity.pdf` | 8 (30,613) | `fc376cfc83a9` | Olson, J. C., Cangelosi, R., Madrid, S., Cooper, S., & Hartter, B. (2011). Ambiguity of the negative sign. In L. R. Wiest & T. Lamberg (Eds.), *Proceedings of the 33rd Annual Meeting of the North American Chapter of the International Group for the Psychology of Mathematics Education* (pp. 113–120). University of Nevada, Reno. \| ERIC (`ED585963`): https://files.eric.ed.gov/fulltext/ED585963.pdf | Misconceptions |
| **06** | [activities_2024_polanin.pdf](papers/activities_2024_polanin.pdf) | `06_Polanin2024_5EModelMetaAnalysis.pdf` | 16 (79,504) | `4a5a2533485f` | Polanin, J. R., Austin, M., Taylor, J. A., Steingut, R. R., Rodgers, M. A., & Williams, R. (2024). Effects of the 5E instructional model: A systematic review and meta-analysis. *AERA Open*, *10*(1), 1–16. https://doi.org/10.1177/23328584241269866 \| ERIC (`EJ1455319`): https://files.eric.ed.gov/fulltext/EJ1455319.pdf | 5Es Meta-Analysis |
| **07** | [proof_2020_rohrer.pdf](papers/proof_2020_rohrer.pdf) | `07_Rohrer2020_InterleavedMathPractice.pdf` | 39 (77,050) | `ba6adb172f16` | Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. *Journal of Educational Psychology*, *112*(1), 40–52. https://doi.org/10.1037/edu0000367 \| ERIC (`ED595322`): https://files.eric.ed.gov/fulltext/ED595322.pdf | Interleaving / Consolidation |
| **08** | [activities_2020_rolfes.pdf](papers/activities_2020_rolfes.pdf) | `08_Rolfes2020_DynamicVisualizationsPOE.pdf` | 16 (84,526) | `c224c567fd6f` | Rolfes, T., Roth, J., & Schnotz, W. (2020). Learning the concept of function with dynamic visualizations. *Frontiers in Psychology*, *11*, Article 693. https://doi.org/10.3389/fpsyg.2020.00693 \| OA PDF: https://www.frontiersin.org/articles/10.3389/fpsyg.2020.00693/pdf | POE / Visual |
| **09** | [activities_2017_runisah.pdf](papers/activities_2017_runisah.pdf) | `09_Runisah2017_5EMetacognitive.pdf` | 12 (39,695) | `c8c340461257` | Runisah, Herman, T., & Dahlan, J. A. (2017). Using the 5E learning cycle with metacognitive technique to enhance students’ mathematical critical thinking skills. *International Journal on Emerging Mathematics Education (IJEME)*, *1*(1), 87–98. https://doi.org/10.12928/ijeme.v1i1.5698 \| OA PDF: http://journal.uad.ac.id/index.php/IJEME/article/download/5698/pdf_6 | 5Es + Metacognition |
| **10** | [misconceptions_2019_ulusoy.pdf](papers/misconceptions_2019_ulusoy.pdf) | `10_Ulusoy2019_IntegerExponentsObstacles.pdf` | 19 (84,577) | `12ec41aca688` | Ulusoy, F. (2019). Serious obstacles hindering middle school students’ understanding of integer exponents. *International Journal of Research in Education and Science (IJRES)*, *5*(1), 52–69. \| ERIC (`EJ1198050`): https://files.eric.ed.gov/fulltext/EJ1198050.pdf | Misconceptions |
| **11** | [misconceptions_2003_vandooren.pdf](papers/misconceptions_2003_vandooren.pdf) | `11_VanDooren2003_IllusionOfLinearity.pdf` | 8 (23,555) | `6528e2f63c87` | Van Dooren, W., De Bock, D., Hessels, A., Janssens, D., & Verschaffel, L. (2003). Remedying secondary school students' illusion of linearity: A teaching experiment. In *Proceedings of the 27th Conference of the International Group for the Psychology of Mathematics Education* (Vol. 4, pp. 331–338). International Group for the Psychology of Mathematics Education. \| ERIC (`ED501140`): https://files.eric.ed.gov/fulltext/ED501140.pdf | Misconceptions |
| **12** | [proof_2022_vest.pdf](papers/proof_2022_vest.pdf) | `12_Vest2022_SelfExplanationWorkedExamples.pdf` | 7 (33,770) | `b754beddbcd5` | Vest, N. A., Silla, E. M., Bartel, A. N., Nagashima, T., Aleven, V., & Alibali, M. W. (2022). Self-explanation of worked examples integrated in an Intelligent Tutoring System enhances problem solving and efficiency in algebra. In J. Culbertson, A. Perfors, H. Rabagliati, & V. Ramenzoni (Eds.), *Proceedings of the 44th Annual Conference of the Cognitive Science Society* (pp. 3466–3472). Cognitive Science Society. \| ERIC (`ED623402`): https://files.eric.ed.gov/fulltext/ED623402.pdf | CLT / Warrants |
| **13** | [proof_2026_wang.pdf](papers/proof_2026_wang.pdf) | `13_Wang2026_CollaborativeWorkedExamples.pdf` | 11 (60,800) | `3ab372044424` | Wang, Y., Li, Q., & Liu, X. (2026). Boundary conditions of collaborative learning using worked-examples: Joint moderating effects of task-specific prior knowledge and task complexity on transfer performance and cognitive load. *Frontiers in Psychology*, *17*, Article 1855051. https://doi.org/10.3389/fpsyg.2026.1855051 \| OA PDF: https://www.frontiersin.org/articles/10.3389/fpsyg.2026.1855051/pdf | CLT / Collaboration |
| **14** | [proof_2026_xu.pdf](papers/proof_2026_xu.pdf) | `14_Xu2026_HubSpokeCognitive.pdf` | 20 (112,136) | `dbe74af0c6ff` | Xu, Z., Zou, Y., Jin, C., & Li, L. (2026). Help students construct a hub-and-spoke cognitive structure: A key pathway to reduce burden and improve quality in mathematics classroom teaching. *Frontiers in Psychology*, *17*, Article 1974303. https://doi.org/10.3389/fpsyg.2026.1974303 \| OA PDF: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1974303/pdf | Hub-and-Spoke |
| **15** | [proof_2019_yeo.pdf](papers/proof_2019_yeo.pdf) | `15_Yeo2019_FingerTracingWorkedExamples.pdf` | 11 (47,022) | `597e4aec633c` | Yeo, L.-M., & Tzeng, Y.-T. (2019). Tracing effect in the worked examples-based learning: An exploration of individual differences in working memory capacity. *EURASIA Journal of Mathematics, Science and Technology Education*, *15*(10), Article em1760. https://doi.org/10.29333/ejmste/105482 \| OA PDF: https://www.ejmste.com/download/tracing-effect-in-the-worked-examples-based-learning-an-exploration-of-individual-differences-in-7717.pdf | CLT / `[tracing]` |

---

## ៣. សំយោគភស្តុតាងជាក់ស្ដែងតាមមុំស្រាវជ្រាវទាំង ៣ (Empirical Synthesis)

- **មុំទី១ — ការយល់ច្រឡំ និងឧបសគ្គការគិតរបស់សិស្ស (`Ulusoy, 2019`; `Olson et al., 2011`; `Fitria et al., 2023`; `Kshetree et al., 2021`; `Van Dooren et al., 2003`)**៖
  1. *ការបែកបាក់ក្នុងផលចែកស្វ័យគុណ ស្វ័យគុណសូន្យ និងស្វ័យគុណអវិជ្ជមាន*៖ `Ulusoy (2019)` បានសិក្សាសិស្សថ្នាក់ទី៨ ចំនួន `N = 165` (+ សម្ភាសន៍ `n = 12`) ដោយរកឃើញថាមានតែ `3.5%` (`n = 4`) ដោះស្រាយត្រូវទាំង ១០ សំណួរ ហើយជាង `65%` បានពិន្ទុក្រោម `3/10`។ ជាក់ស្ដែងលើទម្រង់ផលចែកបញ្ច្រាស `Q10` ($\frac{9^3}{3^3} = \left(\frac{9}{3}\right)^3$) មានសិស្សធ្វើត្រូវតែ **`37.6%`** (`34.5%` ខុស, `27.9%` ទំនេរ) ដោយច្រឡំដកនិទស្សន្ត `(9/3)^(3-3)=3^0` (`4.8%`), ដកគោល `(9-3)^3` (`4.2%`), ឬចែកទាំងគោលទាំងនិទស្សន្ត `(9/3)^(3:3)` (`4.2%`); ចំណែក `Q9` ($\frac{5^6}{5^{-3}}$) ធ្វើត្រូវតែ **`17.0%`** (`51.5%` ខុស ដោយ `13%` ចែកនិទស្សន្ត និង `4.2%` គុណនិទស្សន្ត)។ លើសពីនេះ សិស្សនៅតែច្រឡំគុណនិទស្សន្តពេលគុណគោលដូចគ្នា (`8.4%` ក្នុង `Q6`), បូកនិទស្សន្តពេលបូក (`18.1%` ក្នុង `Q4`), គុណគោលនឹងនិទស្សន្ត (`4%`), ខុស `-3^0` (`66.1%` ខុស; `30.9%` ច្រឡំជា `(-3)^0=1`, `14.5%` `-3`, `6.6%` `0`), និងខុស `2^{-4}` (`63.6%` ខុស; `23.6%` `-16`, `13.9%` `16`)។
  2. *ភាពមិនច្បាស់លាស់នៃសញ្ញាដក និងវង់ក្រចក*៖ `Olson et al. (2011)` (`N = 904` ស្ទង់មតិ ១៩ លំហាត់ដោយ `>40%` ខុស ៤ លំហាត់គ្រប់កម្រិត + សម្ភាសន៍ `n = 19`) រកឃើញថានៅពេលប្រៀបធៀប `(-17)^8` និង `-17^8` មានតែ `5/19` នាក់ (`26.3%`) ឆ្លើយត្រូវ ខណៈ `6/19` នាក់ (`31.6%`) អះអាងថា *"វង់ក្រចកមិនសំខាន់"* ដោយចាត់ទុក `-17` និង `(-17)` ជាវត្ថុតែមួយ ជំនួសការមើលឃើញ $-1 \times 17^8$ (`additive inverse`) និងខ្វះគោលគំនិតច្រាសគុណលើ `n^-1`។ កំហុសនេះគំរាមកំហែងផ្ទាល់ដល់ Step 2 `-2(a^{-3}b^5)^2`, E5 Task 1 $\left(\frac{-2}{3}\right)^4$, Task 3 $\left(\frac{-2x^3}{y^2}\right)^3$, និង Exit Foil `D` (`-9x^4y^8`)។
  3. *ការបំផ្លើសលក្ខណៈបំបែកលើផលបូក (`Freshman's Dream / Illusion of Linearity`) និងភាពចាំបាច់នៃការផ្គូផ្គងទម្រង់*៖ `Fitria et al. (2023)` (`N = 68` ថ្នាក់ទី៨ អាយុ `13–14` ឆ្នាំ) រកឃើញថា `45/68` (`66.2%`) មានកំហុសវិនិច្ឆ័យ (`20.8%–58.3%`), រួមទាំងការអនុវត្តច្បាប់បំបែក $a(b+c)=ab+ac$ ខុសកន្លែងទៅលើស្វ័យគុណ $(5+x)^2 \to 5^2+x^2$ ដោយ *"ប្រើវិចារណញាណសុទ្ធ"* និងបំបែកសញ្ញាដកខុសក្នុងវង់ក្រចក។ `Kshetree et al. (2021)` (`N = 80` ថ្នាក់ទី៨៖ `n = 37` exp vs `n = 43` ctrl, សម្ភាសន៍ `n = 24`; split-half `0.731`, Spearman-Brown `0.844`) ក៏បានរកឃើញកំហុស $(x+y)^n = x^n+y^n$, $(-x)^2 = -x^2$, $x^2\cdot x^4 = x^8$ ហើយបញ្ជាក់ថាវិធីបង្រៀនផ្ដោតលើជម្លោះគំនិតនិងកិច្ចពិភាក្សាក្រុមឈ្នះក្រុមប្រៀបធៀបយ៉ាងច្បាស់ ($U = 1194.000, Z = 3.859, p = .000, r = 0.431$; ផ្នែក Conceptual $r = 0.383$, Procedural $r = 0.458$, Application $r = 0.405$)។ ប៉ុន្តែ `Van Dooren et al. (2003)` (`N = 35` ថ្នាក់ទី៨៖ `n = 18` exp vs `n = 17` ctrl) ព្រមានថា ទោះបីការបង្រៀនជំទាស់កែលម្អលំហាត់មិនមែនលីនេអ៊ែរ (`29.2% → 61.1%`, $t(488)=3.09, p=.0001$; ANCOVA posttest `44.3%` vs `22.3%`, $F(1,32)=6.42, p=.0164$) ប៉ុន្តែភាពត្រឹមត្រូវលើទម្រង់សមាមាត្រពិតបានធ្លាក់ចុះ (`83.3% → 58.3%`, $t(488)=-2.62, p=.0090$) ព្រោះកំហុសបំផ្លើសកើន `13% → 36%` — ដូច្នេះ **ត្រូវតែផ្គូផ្គង** ច្បាប់ចែកចាយត្រឹមត្រូវ $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ ទន្ទឹមគ្នានឹងអន្ទាក់ $(a\pm b)^n \neq a^n \pm b^n$ តាំងពីដំបូង!

- **មុំទី២ — ពិសោធន៍ផ្ទាល់ដៃ `1:1`, `POE` និងរចនាសម្ព័ន្ធ `5Es` (`Johanning, 2017`; `Leton et al., 2026`; `Rolfes et al., 2020`; `Polanin et al., 2024`; `Runisah et al., 2017`)**៖
  - `Polanin et al. (2024)` (វិភាគមេតា WWC លើ **61 RCTs**, 156 ES, `70%` ស្របតាមស្តង់ដារ WWC) បង្ហាញថាគំរូ `5Es` បង្កើនលទ្ធផល **គណិតវិទ្យា** ($g = 0.70, SE = 0.20, 95\%\text{ CI }[0.31, 1.10]$, `+26` ពិន្ទុភាគរយ WWC) និងលើសគំរូ `3E` ($g = 0.42$ ធៀប $g = 0.82$ ក្នុងវិទ្យាសាស្ត្រ, $p < .01$) ដោយសារដំណាក់កាល `Engage` ដាស់ចំណេះមុន និង `Evaluate` បិទបញ្ចប់។ `Runisah et al. (2017)` (`N = 173` **ថ្នាក់ទី៨** ៦ ថ្នាក់) បញ្ជាក់បន្ថែមថា `5E + មេតាកូញីទីវ (LCM)` ទទួលបានពិន្ទុគិតវិភាគគណិតវិទ្យាខ្ពស់ជាង `5E` ធម្មតា និងប្រពៃណី (Normalized gain: `LCM 0.62 > LC 0.49 > CL 0.34`, $\chi^2 = 57.37, p < .001$; មធ្យមក្រោយរៀន `27.30 [68.3%] > 22.84 [57.1%] > 17.80 [44.5%]`, $\chi^2 = 44.01, p < .001$) ដោយមិនអាស្រ័យលើកម្រិតសាលា ($p > .30$)។
  - `Leton et al. (2026)` (ការសាកល្បង ADDIE ស្វ័យគុណ **ថ្នាក់ទី៨** `N = 72`; ការអនុវត្តផ្ទាល់ `81.10%` សិស្ស និង `96%` គ្រូ) រកឃើញថា មុនអន្តរាគមន៍ សិស្សថ្នាក់ទី៨ ខ្សោយបំផុតត្រង់ការបកស្រាយការទស្សន៍ទាយ (`15.83%`) និងការវិភាគដ្យាក្រាម/តារាង (`36.13%`), ប៉ុន្តែបរិបទពិតភ្ជាប់សកម្មភាពរូបភាព និងសំណួរត្រួតពិនិត្យ *Looking-Back* បង្កើនអក្ខរកម្មគណិតវិទ្យាពី `58.72 (SD=12.64)` ទៅ `82.57 (SD=11.80)` ($t(71) = 20.63, p < .001, d_z = 2.43, N\text{-gain} = 0.60$)។
  - `Johanning (2017)` (សិក្សាគ្រូជំនាញ ៤ នាក់ប្រើក្រឡាផ្ទៃការ៉េ *brownie pan*) បង្ហាញថា ការប្រើក្រឡាផ្ទៃឯកតា `1:1` ភ្ជាប់សំណួរគាំទ្រ ១០ ជំហាន ជួយឱ្យសិស្សមើលឃើញឯកតាធៀប $(1\times 1)$ និងទប់ស្កាត់ជំនឿខុសថា *"គុណ/លើកស្វ័យគុណតែងធ្វើឱ្យធំជាងមុន"* — គាំទ្រផ្ទាល់ដល់ក្រឡា $5\times 5\text{ cm}$ ($\left(\frac{2}{5}\right)^2 = \frac{4}{25}$) និង $4\times 4\text{ cm}$ ($\left(\frac{3}{4}\right)^2 = \frac{9}{16}$) ក្នុង E2។ `Rolfes et al. (2020)` (`N = 157`, **88 នាក់ថ្នាក់ទី៨**; `N = 152` imputed) បញ្ជាក់ថា តារាង `Predict–Observe–Explain (POE)` ជាមួយការប្រែប្រួលរូបភាពមានរបៀបបង្កើនពិន្ទុលើសរូបភាពស្ងៀមស្ងាត់ ($M_{\text{adj}} = 7.20/7.34$ vs $6.12$, $\beta = 0.18, t(145.03) = 2.81, p = .006$) ដោយមិនមានឧបសគ្គសម្រាប់សិស្សសមត្ថភាពលំហទាបឡើយ។

- **មុំទី៣ — ជំនួយកាត់បន្ថយបន្ទុកគិត (`CLT`), `[tracing]`, `Hub-and-Spoke`, ធនាគារហេតុផល និងការហ្វឹកហាត់ចម្រុះ (`Xu et al., 2026`; `Yeo & Tzeng, 2019`; `Rohrer et al., 2020`; `Wang et al., 2026`; `Vest et al., 2022`)**៖
  - `Xu et al. (2026)` (សិក្សាប្រតិបត្តិ ២ ជុំ៖ `Class A n = 61`, `Class B n = 60`; ពិន្ទុដើម `102.3±12.5` vs `103.1±11.8`) បង្ហាញថា ការរៀបចំចំណេះដឹងតាមរចនាសម្ព័ន្ធ **Hub-and-Spoke** ភ្ជាប់លំហាត់គំរូដំបូងយ៉ាងលម្អិតនិងប្រៀបធៀបវិធីសាស្ត្រ បង្កើនសូចនាករទាំង ៣ ($p < .001$)៖ ភាពច្បាស់លាស់ `M = 2.57±1.12 -> 3.88±1.08`, ការទទួលយក `M = 2.39±1.07 -> 3.50±1.07`, និងការយល់/អនុវត្ត `M = 2.56±1.10 (19.7% ពិន្ទុ 4–5) -> 4.32±0.89 (86.7% ពិន្ទុ 4–5)` — គាំទ្រ E3 បង្គុំដ្យាក្រាមមជ្ឈមណ្ឌល $x^n$ តភ្ជាប់កាំទាំង ៣៖ $(a^m)^n$, $(ab)^n$, $\left(\frac{a}{b}\right)^n$។
  - `Yeo & Tzeng (2019)` (`N = 72` អាយុ `11–13` ឆ្នាំ, Low/High WMC `n = 36` ម្នាក់) បញ្ជាក់ថា ការបង្គាប់ឱ្យប្រើម្រាមដៃអូសតាមសញ្ញាវង់ក្រចក (`[tracing]`) កាត់បន្ថយភាពលំបាកលើលំហាត់ដូចគ្នា ($M = 1.82$ vs $2.36$, $F(1,68)=9.24, p=.003, \eta^2=.120$) និងផ្ទេរ ($M = 2.67$ vs $3.25$, $F(1,68)=13.94, p<.001, \eta^2=.170$) ព្រមទាំងបង្កើនភាពសុក្រឹតផ្ទេរ ($M = 3.00\pm 0.85$ vs $2.31\pm 1.01$, $F(1,68)=9.38, p=.003, \eta^2=.121$) ដោយមានប្រសិទ្ធភាព MANOVA ទាំង Similar (`Wilks' Lambda=.847, p=.012, η^2=.153`) និង Transfer (`Wilks' Lambda=.785, p=.001, η^2=.215`) គ្រប់កម្រិត WMC។
  - `Vest et al. (2022)` (`N = 167` ថ្នាក់ទី៦–៨, $M = 12.81\pm 0.76$; `n = 134` self-explanation vs `n = 33` control) បង្ហាញថា ការជ្រើសមូលហេតុគោលគំនិតពីម៉ឺនុយ (Warrant Bank) លើឧទាហរណ៍ត្រូវនិងខុស បង្កើនលទ្ធផល Procedural ($\beta = 0.28, F(1,161)=5.32, p=.022$) និង Conceptual ($\beta = 1.23, F(1,161)=7.18, p=.008$), កាត់បន្ថយកំហុស/ជំហាន ($\beta = -0.34, F(1,160)=8.75, p=.004$), កាត់បន្ថយជំនួយ/ជំហាន ($\beta = -0.10, F(1,160)=6.97, p=.009$) និងបង្កើនល្បឿន (`-5.83 s/step`, $F(1,160)=7.84, p=.006$)។
  - `Wang et al. (2026)` (`N = 134` ពិសោធន៍ `2×2×2`) រកឃើញថា កិច្ចសហការកាត់បន្ថយបន្ទុកគិតជារួម ($F(1,130)=8.74, p<.01, \eta_p^2=.063$) ប៉ុន្តែក្រុម ៣ នាក់ឈ្នះបុគ្គលលើលំហាត់ស្មុគស្មាញលុះត្រាតែមានចំណេះមុនរឹងមាំ ($M=55.40\pm 13.64$ vs $45.31\pm 18.02, F(1,65)=6.74, p<.05, \eta_p^2=.094$; low-PK $31.08\pm 14.86$ vs $26.51\pm 16.73$) — ដូច្នេះ **ត្រូវពង្រឹងមូលដ្ឋាន E2–E4 មុនបើក E5 Relay ៣ តួនាទី**។
  - `Rohrer et al. (2020)` (Cluster RCT លើ 54 ថ្នាក់ទី៧, គ្រូ ១៥ នាក់, `N = 787`: Interleaved `n = 398` vs Blocked `n = 389`) បញ្ជាក់ថា ការហ្វឹកហាត់លាយចម្រុះលក្ខណៈជួយបង្កើនពិន្ទុតេស្តពន្យារពេល ~៣៣ ថ្ងៃ (`60.7% [SD=28.6]` vs `37.6% [SD=27.3]`, $d = 0.83, 95\%\text{ CI }[0.68, 0.97], p < .001$, វិជ្ជមានគ្រប់គ្រូ ១៥ នាក់ $d = 0.23\text{–}1.48$, រួមទាំងការសម្រួលកន្សោម $d = 0.40$) — គាំទ្រការលាយចម្រុះលក្ខណៈទាំង ៣ ក្នុង E4 គ, E5 Task 3 និងកិច្ចការផ្ទះ។

---

## ៤. ផែនទីបម្លែងចូលក្នុងកិច្ចតែងការ ៥០ នាទី (`2 + 9 + 17 + 20 + ≤2 = 50 min`)

| ជំហាន / 5Es (នាទី) | បញ្ហាភស្តុតាងដែលត្រូវដោះស្រាយ | ការកែលម្អជាក់ស្ដែងក្នុងកញ្ចប់ ៤ ឯកសារ (`_POWQ`) |
|---|---|---|
| **ជំហានទី ១** (`2 min`) | រៀបចំវិន័យថ្នាក់ និងតួនាទីសហការក្រុម `៣ នាក់/ក្រុម` (`Wang et al., 2026`) | រដ្ឋបាលថ្នាក់ ចែកក្រុម `៣ នាក់/ក្រុម` និងត្រៀម `Printable p. 1` ព្រមទាំងកន្ត្រៃ/បន្ទះក្រឡា `1:1` |
| **ជំហានទី ២ — កំណែ & រំលឹក** (`≤3 + 3 = 6 min`) | សញ្ញាដកក្រៅវង់ក្រចក (`Olson et al., 2011`) និងពុម្ពខុសទំព័រ 18 vs 17 | កំណែ `ប្រតិបត្តិ 4.2` (`p. 18`): `-2(a^-3 b^5)^2 = -2b^10/a^6` (`-2` ក្រៅវង់ក្រចក) និង `a(a^4)^5 a^-6 = a^15` (បញ្ជាក់ពុម្ព `p. 18`: `a^-1`); រំលឹក `§3`, `§4.1`, `§4.2` |
| **E1 - Engage** (`3 min`) | ទស្សន៍ទាយខ្សោយ `15.83%` (`Leton et al., 2026`) និងបាត់បង់ឯកតា (`Johanning, 2017`) | **«បេសកកម្មកាត់បង្រួមធុងស្តុកទឹក និងផ្ទាំងសំណាញ់នៅព្រះក្រសាំង»**：បង្រួមគែមធុងគូប `1 m` មក `2/5 m`; អន្ទាក់ $\frac{2^3}{5} = \frac{8}{5} > 1\text{ m}^3$ (មិនអាចធុងតូចជាងផ្ទុកទឹកច្រើនជាងធុងដើម `1 m³` ឡើយ!) |
| **E2 - Explore** (`11 min`) | បំផ្លើសឯកតា (`Johanning, 2017`), ភ្លេចភាគបែង (`Ulusoy, 2019`), អន្ទាក់បំបែកលើ `+` (`Fitria et al., 2023`; `Kshetree et al., 2021`; `Van Dooren et al., 2003`) | **ពិសោធន៍ក្រឡា `1:1` & Dual POE (`Printable p. 1`, `Rolfes et al., 2020`)**：<br>• **Act 1 (`1:1`)**: ក្រឡាឯកតា $5.00\times 5.00\text{ cm}$ (`25` ការ៉េ) + បន្ទះកាត់ $2.00\times 2.00\text{ cm}$ ($\left(\frac{2}{5}\right)^2 = \frac{4}{25} \neq \frac{4}{5}$) + បន្ទាត់ calibration `5.00 cm` + ផ្គុំកត្តា `p. 18` ($\frac{2^3}{5^3}=\left(\frac{2}{5}\right)^3$, $\frac{a^n}{b^n}=\left(\frac{a}{b}\right)^n$)<br>• **POE 2A (`1:1`)**: $4.00\times 4.00\text{ cm}$ និងការ៉េឈូស $3.00\times 3.00\text{ cm}$ $\implies \left(\frac{3}{4}\right)^2 = \frac{9}{16} \neq \frac{9}{4}$<br>• **POE 2B**: អន្ទាក់បំបែកលើផលបូក $\left(\frac{6+4}{2}\right)^2 = 25$ vs $\frac{6^2+4^2}{2^2} = 13$ |
| **E3 - Explain** (`6 min`) | ចំណេះបែកខ្ញែក និងការបំបាត់វង់ក្រចក (`Xu et al., 2026`; `Van Dooren et al., 2003`; `Runisah et al., 2017`) | សិស្សបង្គុំប្រអប់ `ជាទូទៅ 4.3` (`p. 18`) $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ ($a,b\neq 0, n\neq 0$, ពីរទិស & $(a/b)^{-n}=(b/a)^n$) + **ដ្យាក្រាម Hub-and-Spoke** ជុំវិញ $x^n$ + **Warrant Bank `①–⑤`** |
| **E4 - Elaborate** (`10 min`) | បន្ទុកគិតខ្ពស់ និងកំហុសស្វ័យគុណច្រាស/ចម្រុះ (`Yeo & Tzeng, 2019`; `Vest et al., 2022`; `Rohrer et al., 2020`) | `លំហាត់គំរូទី 1` (`p. 18` ក, ខ) + `Reverse Consolidation គ` ($\frac{6^4}{3^4}\cdot(2^{-1})^2 = 4$) លើកាត B&W `[tracing]` (`Printable p. 2`) + សំណួរ **EIA Looking-Back (30s)** |
| **E5 - Evaluate** (`10 min`) | កំហុសលាយរូបមន្ត & សញ្ញាដក (`Olson et al., 2011`; `Wang et al., 2026`; `Rohrer et al., 2020`) | • **Relay ៣ តួនាទី (`Printable p. 3`)**: Task 1 (`ប្រតិបត្តិ ក` p. 18), Task 2 (`ប្រតិបត្តិ ខ` p. 18), Task 3 (`3-Property Synthesis` $\left(\frac{-2x^3}{y^2}\right)^3\cdot\frac{y^7}{x^5} = -8x^4y$) + បិទ E1 ($\left(\frac{2}{5}\right)^3 = \frac{8}{125}\text{ m}^3$)<br>• **Exit Foils `A–D` (`Printable p. 5`)** លើ $\left(\frac{-3x^2}{y^{-4}}\right)^2$ + សំណួរ Exit Ticket ខ្លី ៣ |
| **ជំហានទី ៥ — កិច្ចការផ្ទះ** (`≤2 min`) | ពង្រឹងការអនុវត្តលាយចម្រុះ (`Rohrer et al., 2020`) (`Printable p. 6`) | **ផ្នែក ក** (ទំ.១៨ & ២៥ `#6 គ`): ៣ លំហាត់; **ផ្នែក ខ** (ទំ.២៥ `#7 ង` & ទំ.២៦ `#8 ក, គ`): ២ លំហាត់ + អានមុន `៤.៤. ស្វ័យគុណនៃ 10` (ទំ.១៩–២០) |

---

## ៥. លក្ខខណ្ឌកំណត់ឯកភាព ១០០% សម្រាប់អ្នកនិពន្ធ LaTeX ទាំង ៣ (`Locked Master Sync Spec`)

> [!IMPORTANT]
> អ្នកនិពន្ធឯកសារ LaTeX ទាំង ៣ រូប (`LS_Plan_POWQ.tex`, `Teaching_Scenario_POWQ.tex`, `Teaching_Guideline_POWQ.tex`, `Printable_Materials_POWQ.tex`) ត្រូវគោរពលក្ខខណ្ឌខាងក្រោមនេះ **ពាក្យ-ទល់-ពាក្យ ១០០%** ដោយគ្មានការកែប្រែតួលេខ សំណួរ ឬលំដាប់ហេតុផលឡើយ៖

1. **អត្តសញ្ញាណសាលា គ្រូ និងកាលបរិច្ឆេទ**：
   - ក្បាលរដ្ឋបាល៖ `មន្ទីរអប់រំ យុវជន និងកីឡា ខេត្តកំពង់ធំ` $\to$ `ការិយាល័យអប់រំ យុវជន និងកីឡា ស្រុកកំពង់ស្វាយ` $\to$ `អនុវិទ្យាល័យព្រះក្រសាំង`
   - គ្រូបង្រៀន៖ `ហុក ប៊ុនថែន`
   - កាលបរិច្ឆេទសូរ្យគតិ៖ `ថ្ងៃចន្ទ ទី១៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦` (ក្នុងហត្ថលេខា៖ `កំពង់ស្វាយ, ថ្ងៃទី១៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦`)
   - កាលបរិច្ឆេទចន្ទគតិ៖ `ថ្ងៃចន្ទ ៧កើត ខែកត្តិក ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០`
2. **ការបែងចែកពេល ៥០ នាទី**：
   - `ជំហានទី ១` (`2 min`) + `ជំហានទី ២` (`កំណែ ≤3 min` + `រំលឹក 3 min` + `E1 3 min` = `9 min`) + `ជំហានទី ៣` (`E2 11 min` + `E3 6 min` = `17 min`) + `ជំហានទី ៤` (`E4 10 min` + `E5 10 min` = `20 min`) + `ជំហានទី ៥` (`≤2 min`) = **`50 min`**។
3. **ជំហានទី ២ — កំណែ (`ប្រតិបត្តិ 4.2` ទំ.១៨) និងរំលឹក**：
   - កំណែ ក. $-2(a^{-3}\cdot b^5)^2 = -2a^{-6}b^{10} = -\dfrac{2b^{10}}{a^6}$ *(សង្កត់ធ្ងន់ `-2` នៅក្រៅវង់ក្រចក មិនមែន `(-2)^2` ទេ!)*។
   - កំណែ ខ. $a\cdot(a^4)^5\cdot a^{-6} = a^{15}$ *(និងបញ្ជាក់កំណត់សម្គាល់ពុម្ពទំព័រ ១៨ $a\cdot(a^4)\cdot a^{-6} = a^{-1}$)*។
   - រំលឹក៖ `§3` វិធីចែក $\dfrac{a^m}{a^n} = a^{m-n},\; a^0 = 1,\; a^{-n} = \dfrac{1}{a^n}$ ($a\neq 0$); `§4.1` $(a^m)^n = a^{mn}$; `§4.2` $(ab)^n = a^n b^n$។
4. **E1 Hook (`3 min`)**：
   - **«បេសកកម្មកាត់បង្រួមធុងស្តុកទឹក និងផ្ទាំងសំណាញ់នៅព្រះក្រសាំង»** — បង្រួមជ្រុងធុងគូប `1 m` មកត្រឹម $\frac{2}{5}\text{ m}$; លាតត្រដាងអន្ទាក់ចែកស្វ័យគុណមិនគ្រប់ភាគបែង $\frac{2^3}{5} = \frac{8}{5} > 1\text{ m}^3$ *(មិនអាចធុងតូចជាងមានមាឌផ្ទុកទឹកធំជាងធុង `1 m³` ដើមបានឡើយ!)*។
5. **E2 Hands-On `1:1` Grid Overlay & Dual POE (`11 min`, `Printable p. 1`)**：
   - **Act 1 (`x=1cm, y=1cm`)**: ក្រឡាឯកតា $5.00\text{ cm}\times 5.00\text{ cm}$ (`25` ការ៉េតូច) + បន្ទះកាត់ឈូស $2.00\text{ cm}\times 2.00\text{ cm}$ ($\left(\frac{2}{5}\right)^2 = \frac{4}{25} \neq \frac{4}{5}$) + បន្ទាត់ calibration bar `5.00 cm` (`ពេលបោះពុម្ព សូមជ្រើស Scale: Actual Size 100% — កុំជ្រើស Fit to Page`) + ការផ្គុំកត្តាសៀវភៅ ទំ.១៨ (`ឧទាហរណ៍ ក` $\frac{2^3}{5^3}=\left(\frac{2}{5}\right)^3$, `ខ` $\frac{a^n}{b^n}=\left(\frac{a}{b}\right)^n$)។
   - **`POE 2A` (`1:1`)**: ក្រឡា $4.00\text{ cm}\times 4.00\text{ cm}$ ជាមួយការ៉េឈូស $3.00\text{ cm}\times 3.00\text{ cm}$ — ទស្សន៍ទាយ និងផ្ទៀងផ្ទាត់ $\left(\frac{3}{4}\right)^2 = \frac{9}{16} \neq \frac{9}{4}$។
   - **`POE 2B` (ឧទាហរណ៍ជំទាស់លើផលបូក)**: ទស្សន៍ទាយ និងពិសោធន៍ $\left(\frac{6+4}{2}\right)^2 = 5^2 = 25$ ធៀប $\frac{6^2+4^2}{2^2} = \frac{52}{4} = 13$ — ស្វ័យគុណ **មិនចែកចាយ** លើ `+` ឬ `-` ជាដាច់ខាត!
6. **E3 Formalization & Hub-and-Spoke Warrant Bank (`6 min`, `Printable p. 4`)**：
   - ប្រអប់ `ជាទូទៅ` (ទំ.១៨)៖ $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ ($a,b$ ជាចំនួនសនិទានខុសពីសូន្យ និង $n$ ជាចំនួនគត់រ៉ឺឡាទីបខុសពីសូន្យ; អនុវត្ត **ពីរទិស** ព្រមទាំងច្បាប់ច្រាស $\left(\dfrac{a}{b}\right)^{-n} = \left(\dfrac{b}{a}\right)^n$)។
   - **ធនាគារហេតុផល B&W (`Warrant Bank ①–⑤`)**：
     - **`①`** $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ (`§4.3` ពីរទិស៖ ចែកចាយ និងផ្គុំបញ្ច្រាស $\frac{a^n}{b^n} = \left(\frac{a}{b}\right)^n$, ព្រមទាំង $\left(\frac{a}{b}\right)^{-n}=\left(\frac{b}{a}\right)^n$)
     - **`②`** $(ab)^n = a^n b^n$ (`§4.2` ចែកចាយគ្រប់កត្តារួមទាំងមេគុណ)
     - **`③`** $(a^m)^n = a^{mn}$ (`§4.1` គុណនិទស្សន្តនឹងនិទស្សន្ត មិនមែនបូកទេ)
     - **`④`** $a^m a^n = a^{m+n},\ \dfrac{a^m}{a^n} = a^{m-n},\ a^0 = 1,\ a^{-n} = \dfrac{1}{a^n} \Leftrightarrow \dfrac{1}{c^{-n}} = c^n$ ($a,c \neq 0$)
     - **`⑤`** $(-x)^{\text{គូ}} = +x^{\text{គូ}},\ (-x)^{\text{សេស}} = -x^{\text{សេស}},\ (a\pm b)^n \neq a^n\pm b^n$
7. **E4 Worked Examples & `[tracing]` Card (`10 min`, `Printable p. 2`)**：
   - `លំហាត់គំរូទី 1` (ទំ.១៨)៖
     - **ក.** $\left(\dfrac{3}{4}\right)^3 = \dfrac{3^3}{4^3} = \dfrac{27}{64}$
     - **ខ.** $\left(\dfrac{a^2 b^3}{c^{-2}}\right)^3 = \dfrac{(a^2)^3(b^3)^3}{(c^{-2})^3} = \dfrac{a^6 b^9}{c^{-6}} = a^6 b^9 c^6$
     - **Reverse Consolidation គ.** $\dfrac{6^4}{3^4}\cdot(2^{-1})^2 = \left(\dfrac{6}{3}\right)^4\cdot 2^{-2} = 2^4\cdot 2^{-2} = 2^2 = 4$
   - ភ្ជាប់សញ្ញា B&W `[tracing]` / `[ចង្អុលអូស]` ម្រាមដៃពីនិទស្សន្តក្រៅទៅភាគយកនិងភាគបែង + **EIA Looking-Back (`30s`)**។
8. **E5 3-Role Collaborative Relay & Exit Foils (`10 min`, `Printable pp. 3 & 5`)**：
   - **Relay ៣ តួនាទី (`p. 3`)**:
     - **Task 1 (`ប្រតិបត្តិ ក` ទំ.១៨)**: $\left(\dfrac{-2}{3}\right)^4 = \dfrac{(-2)^4}{3^4} = \dfrac{16}{81}$
     - **Task 2 (`ប្រតិបត្តិ ខ` ទំ.១៨)**: $\left(\dfrac{a^4\cdot b^{-2}}{c^3}\right)^2 = \dfrac{(a^4)^2(b^{-2})^2}{(c^3)^2} = \dfrac{a^8b^{-4}}{c^6} = \dfrac{a^8}{b^4 c^6}$
     - **Task 3 (`3-Property Synthesis`)**: $\left(\dfrac{-2x^3}{y^2}\right)^3\cdot\dfrac{y^7}{x^5} = \dfrac{-8x^9}{y^6}\cdot\dfrac{y^7}{x^5} = -8x^4 y$ + **បិទបេសកកម្ម E1** ($\left(\dfrac{2}{5}\right)^3 = \dfrac{8}{125}\text{ m}^3$)។
   - **Exit Foils `A–D` (`p. 5`)** លើ $\left(\dfrac{-3x^2}{y^{-4}}\right)^2$៖
     - **`A`**: $\dfrac{9x^4}{y^{-4}}$ *(ភ្លេចលើកស្វ័យគុណភាគបែង — ល្មើស `①`)*
     - **`B`**: $9x^4 y^2$ *(បូកនិទស្សន្តជំនួសគុណ — ល្មើស `③`)*
     - **`C`**: $9x^4 y^8$ *(**ត្រឹមត្រូវ** តាម `①–⑤`)*
     - **`D`**: $-9x^4 y^8$ *(ខុសសញ្ញាដកគូ/សេស — ល្មើស `⑤`)*
     - បូកនឹងសំណួរ **Exit Ticket ខ្លី ៣ សំណួរ** (ពិនិត្យវិសាលភាព/វង់ក្រចក, ច្រាសបញ្ច្រាស, និងហេតុផល `①–⑤`)។
9. **ជំហានទី ៥ — កិច្ចការផ្ទះ (`≤2 min`, `Printable p. 6`)**：
   - **ផ្នែក ក** (ទំ.១៨ & ២៥ `#6 គ`):
     - `(១)` $\left(\dfrac{-3}{5}\right)^3$ $\left(= -\dfrac{27}{125}\right)$
     - `(២)` $\left(\dfrac{2x^3 y^{-1}}{z^4}\right)^3$ $\left(= \dfrac{8x^9}{y^3 z^{12}}\right)$
     - `(៣)` $\left(\dfrac{4}{3}\right)^4\left(\dfrac{4}{3}\right)^{-6}\left(\dfrac{4}{3}\right)^3$ $\left(= \dfrac{4}{3}\right)$
   - **ផ្នែក ខ** (ទំ.២៥ `#7 ង` & ទំ.២៦ `#8 ក, គ`):
     - `(១)` $\dfrac{(32a^2x^8)^3}{(5ax)(-2a^2x^2)^2(-4a^3x)^3}$ $\left(= -\dfrac{128x^{16}}{5a^8}\right)$
     - `(២)` សរសេរ $x^{12}$ ជាស្វ័យគុណនៃ $x^2$ $\left((x^2)^6\right)$ និងសរសេរ $2^{18}, (2^5)^6$ ជាស្វ័យគុណនៃ $8$ $\left(8^6,\; 8^{10}\right)$; រួចអានមេរៀន `៤.៤. ស្វ័យគុណនៃ 10` (ទំ.១៩–២០)។
