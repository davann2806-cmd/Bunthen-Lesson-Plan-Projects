# សង្ខេបការស្រាវជ្រាវគរុកោសល្យ (Research Brief `_EXP412`): ២.៤.១ ស្វ័យគុណនៃស្វ័យគុណ និង ២.៤.២ ស្វ័យគុណនៃផលគុណ (ថ្នាក់ទី៨)

- **បរិបទបង្រៀន**: គណិតវិទ្យា ថ្នាក់ទី៨ — ពីជគណិត មេរៀនទី២៖ ស្វ័យគុណ (`៤.១ ស្វ័យគុណនៃស្វ័យគុណ` និង `៤.២ ស្វ័យគុណនៃផលគុណ`) | អនុវិទ្យាល័យព្រះក្រសាំង (`NGS`, ស្រុកកំពង់ស្វាយ ខេត្តកំពង់ធំ) | គ្រូបង្រៀន៖ **ហុក ប៊ុនថែន** | ព.ស. ២៥៧០ (ឆ្នាំមមី អដ្ឋស័ក) / គ.ស. ២០២៦។
- **កញ្ចប់ឯកសារបង្រៀនគោលដៅ** (`01_កិច្ចតែងការបង្រៀន\ថ្នាក់ទី៨\ពីជគណិត_មេរៀនទី២_ស្វ័យគុណ\២.៤.១_២.៤.២_ស្វ័យគុណនៃស្វ័យគុណ_និងស្វ័យគុណនៃផលគុណ\`)៖
  - `LS_Plan_EXP412.tex` (៥០ នាទី, គំរូ 5Es, `៤–៨+` ទំព័រ A4 បត់បែនតាមខ្លឹមសារជាក់ស្ដែង, ពេញទំព័រ `>= 90%`)
  - `Teaching_Scenario_EXP412.tex` (`២–៤` ទំព័រ A4 តាមខ្លឹមសារជាក់ស្ដែង, ពេញទំព័រ `>= 90%`)
  - `Teaching_Guideline_EXP412.tex` (សៀវភៅណែនាំគ្រូ & របាយការណ៍ស្រាវជ្រាវ APA 7th, Mobile-First `~14–20` ទំព័រ)
  - `Printable_Materials_EXP412.tex` (សម្ភារៈបោះពុម្ព B&W មាត្រដ្ឋាន `1:1` ពិត, គ្មានការពឹងផ្អែកលើហ្វឺតពណ៌)
  - `ឯកសារស្រាវជ្រាវយោង_PDF\` (`00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md` + `01_Booth2014...pdf` .. `15_Yeo2019...pdf`)
- **ប្រភពសៀវភៅសិក្សាគោល**: MoEYS គណិតវិទ្យា ថ្នាក់ទី៨ (`Book pp. 16–18, 25–26` = `PDF pp. 21–23, 30–31`)
- **ស្ថានភាពឯកសារស្រាវជ្រាវ Open-Access**: **១៥ PDF** ផ្ទៀងផ្ទាត់រួច (`b'%PDF-'`, `PyMuPDF fitz` `7–22` ទំព័រ, `27,705–84,577` តួអក្សរ, **SHA-256 ដូចគ្នា ១០០%** រវាង `papers\` និង `ឯកសារស្រាវជ្រាវយោង_PDF\`)។

---

## ១. ការផ្ទៀងផ្ទាត់ខ្លឹមសារសៀវភៅសិក្សាគោល (Textbook Ground-Truth Audit: `Book pp. 16–18, 25–26`)

ការពិនិត្យដោយផ្ទាល់លើទំព័រសៀវភៅសិក្សាគោល (`tb_pdf_p021.png`, `tb_pdf_p022.png`, `tb_pdf_p023.png`, `tb_pdf_p030.png`, `tb_pdf_p031.png`) បញ្ជាក់ខ្លឹមសារដូចតទៅសម្រាប់ឯកភាពពាក្យ-ទល់-ពាក្យនៅក្នុងឯកសារ LaTeX ទាំង ៤៖

### ១.១ មេរៀនមុនសម្រាប់កំណែលំហាត់ផ្ទះ (`Book p. 16` / `PDF p. 21`)
- **ប្រតិបត្តិ : គណនា** (បាតទំព័រ 16 — កំណែជំហានទី២)៖
  - ក. $\dfrac{x^9}{x^4} = x^{9-4} = x^5$ ($x \neq 0$)
  - ខ. $\dfrac{\left(\frac{3}{2}\right)^2}{\left(\frac{3}{2}\right)^4} = \left(\frac{3}{2}\right)^{2-4} = \left(\frac{3}{2}\right)^{-2} = \frac{1}{\left(\frac{3}{2}\right)^2} = \frac{4}{9}$
  - គ. $\dfrac{y^9}{y^9} = y^{9-9} = y^0 = 1$ ($y \neq 0$)
  - ឃ. $\left(\dfrac{3yx^9}{-15y^5x^4}\right)^0 = 1$ ($x, y \neq 0$; អន្ទាក់ស្វ័យគុណសូន្យ!)

### ១.២ ផ្នែក `4.1. ស្វ័យគុណនៃស្វ័យគុណ` (`Book p. 17` / `PDF p. 22`)
- **ឧទាហរណ៍ : សរសេរកន្សោមខាងក្រោមដោយប្រើនិទស្សន្តតែមួយ**៖
  - ក. $(2^3)^4 = (2^3)\cdot(2^3)\cdot(2^3)\cdot(2^3) = 2^{\underbrace{3+3+3+3}_{4\text{ កត្តា}}} = 2^{3\times 4} = 2^{12}$ ។
  - ខ. $(5^6)^4 = (5^6)\cdot(5^6)\cdot(5^6)\cdot(5^6) = 5^{\underbrace{6+6+6+6}_{4\text{ កត្តា}}} = 5^{6\times 4} = 5^{24}$ ។
- **ជាទូទៅ (ប្រអប់ទ្រឹស្ដីបទ `4.1`)**៖ `បើ a ជាចំនួនសនិទាននិង m , n ជាចំនួនគត់រ៉ឺឡាទីបខុសពីសូន្យ គេបាន (a^m)^n = (a^n)^m = a^{m \cdot n} ។`
  - *(កំណត់សម្គាល់សុក្រឹតភាពគណិតវិទ្យាសម្រាប់ `E3` និង `Teaching_Guideline`៖ នៅពេល $m < 0$ ឬ $n < 0$ ឬស្មើ $0$ ត្រូវបន្ថែមលក្ខខណ្ឌ $a \neq 0$ ដើម្បីចៀសវាង $0^{-k}$ ឬ $0^0$ គ្មានន័យ ហើយរូបមន្ត $(a^m)^n = a^{m\cdot n}$ ក៏នៅពិតដែរពេល $m=0$ ឬ $n=0$ ចំពោះ $a \neq 0$ ។)*
- **លំហាត់គំរូ : គណនា (`4.1`)**៖
  - ក. $(10^2)^3 = 10^{2\times 3} = 10^6 = 1\ 000\ 000$ ។
  - ខ. $(a^{-2})^k \cdot (a^k)^5 = a^{-2\cdot k} \cdot a^{5k} = a^{-2k+5k} = a^{3k}$ ។ *(ជាមួយលក្ខខណ្ឌ $a \neq 0$)*
- **ប្រតិបត្តិ : គណនា (`4.1`)**៖
  - ក. $(a^3)^{-2} = a^{3\cdot(-2)} = a^{-6} = \frac{1}{a^6}$ ($a \neq 0$)
  - ខ. $a \cdot (a^4)^5 \cdot a^{-6} = a^1 \cdot a^{20} \cdot a^{-6} = a^{1+20-6} = a^{15}$ ($a \neq 0$) ។

### ១.៣ ផ្នែក `4.2. ស្វ័យគុណនៃផលគុណ` (`Book pp. 17–18 top` / `PDF pp. 22–23`)
- **ឧទាហរណ៍ : សរសេរកន្សោមខាងក្រោមដោយប្រើនិទស្សន្តតែមួយ** (`p. 17`)៖
  - ក. $2^3 \times 5^3 = \underbrace{2\times 2\times 2}_{3\text{ កត្តា}} \times \underbrace{5\times 5\times 5}_{3\text{ កត្តា}} = \underbrace{(2\times 5)(2\times 5)(2\times 5)}_{3\text{ កត្តា}} = (2\times 5)^3$ *(សៀវភៅខ្វះសញ្ញាបញ្ចប់ `។`)*
  - ខ. $2^2 \times 5^2 \times 7^2 = \underbrace{2\times 2}_{2\text{ កត្តា}} \times \underbrace{5\times 5}_{2\text{ កត្តា}} \times \underbrace{7\times 7}_{2\text{ កត្តា}} = \underbrace{(2\times 5\times 7)(2\times 5\times 7)}_{2\text{ កត្តា}} = (2\times 5\times 7)^2$ *(សៀវភៅខ្វះ `។`)*
  - គ. $a^n \cdot b^n = \underbrace{a \cdot a \ldots a}_{n\text{ កត្តា}} \cdot \underbrace{b \cdot b \ldots b}_{n\text{ កត្តា}} = \underbrace{(ab)(ab)\ldots (ab)}_{n\text{ កត្តា}} = (ab)^n$ ។
- **ជាទូទៅ (ប្រអប់ទ្រឹស្ដីបទ `4.2`, `p. 17`)**៖ `បើ a , b ជាចំនួនសនិទាននិង n ជាចំនួនគត់រ៉ឺឡាទីបខុសពីសូន្យ គេបាន (a \cdot b)^n = a^n \cdot b^n ។` *(បើ $n < 0$ ត្រូវ $a \neq 0,\; b \neq 0$)*
- **លំហាត់គំរូ : សម្រួលកន្សោម (`4.2`, `p. 18 top`)**៖
  - ក. $(3xy^2)^3 = 3^3 \cdot x^3 \cdot (y^2)^3 = 27x^3 y^6$ ។
  - ខ. $(b^3)(b^{2k-1})^3 = b^3 \cdot b^{3(2k-1)} = b^{3+6k-3} = b^{6k}$ ។
- **ប្រតិបត្តិ : គណនា (`4.2`, `p. 18 top`) & ការផ្ទៀងផ្ទាត់ពុម្ពខុស (`Erratum Audit`)**៖
  - ក. $-2(a^{-3} \cdot b^5)^2 = -2(a^{-6} \cdot b^{10}) = -2a^{-6}b^{10} = -\dfrac{2b^{10}}{a^6}$ *(សញ្ញាដកនិងមេគុណ `-2` នៅក្រៅវង់ក្រចក មិនលើកស្វ័យគុណ ២ ឡើយ!)*
  - ខ. សៀវភៅទំព័រ `18` បោះពុម្ពថា `a · (a^4) · a^{-6}` (បាត់និទស្សន្តក្រៅ `5` ដូចក្នុងទំព័រ `17` `a · (a^4)^5 · a^{-6}`)! បើគណនាតាមពុម្ពទំព័រ `18` ត្រង់ៗបាន $a^{1+4-6} = a^{-1} = \frac{1}{a}$ រីឯទំព័រ `17` `a · (a^4)^5 · a^{-6} = a^{15}`។ ឯកសារគ្រូត្រូវប្រើលំហាត់ `p. 17 ក–ខ` និង `p. 18 ក` ក្នុង `E5 Relay` ព្រមទាំងបញ្ជាក់ពុម្ព `p. 18 ខ` ក្នុង `Teaching_Guideline_EXP412.tex` កុំឱ្យគ្រូនិងសិស្សភាន់ច្រឡំ។

### ១.៤ កិច្ចការផ្ទះ (`Book pp. 25–26` / `PDF pp. 30–31`)
- **`#2ក` (`p. 25`)**: `ចូរសរសេរស្វ័យគុណខាងក្រោមជាផលគុណកត្តាដូចគ្នារួចគណនា ។` $\to$ ក. $(4^3)(2^2) = (2^2)^3 \cdot 2^2 = 2^6 \cdot 2^2 = 2^8 = 256$ (ឬ $64 \times 4 = 256$)។
- **`#7ង` ភាគយក (`p. 25`)**: ក្នុងលំហាត់ $\dfrac{(32a^2x^8)^3}{(5ax)(-2a^2x^2)^2(-4a^3x)^3}$ ភាគយកត្រូវប្រើ `4.1 & 4.2` គឺ $(32a^2x^8)^3 = 32^3 \cdot (a^2)^3 \cdot (x^8)^3 = (2^5)^3 a^6 x^{24} = 32{,}768\,a^6x^{24}$ *(ទុកការចែកភាគបែងសម្រាប់មេរៀន `2.4.3`)*។
- **`#8ក, ខ, គ` (`p. 26`)**:
  - ក. សរសេរ $x^{12}$ ជាស្វ័យគុណនៃ $x^2$ $\implies x^{12} = (x^2)^6$ ។
  - ខ. សរសេរ $y^{15}$ ជាស្វ័យគុណនៃ $y^3$ $\implies y^{15} = (y^3)^5$ ។
  - គ. សរសេរ $2^{18}$ និង $(2^5)^6$ ជាស្វ័យគុណនៃ $8$ *(សៀវភៅខ្វះ `.` ក្រោយ `គ`)* $\implies 2^{18} = (2^3)^6 = 8^6$ និង $(2^5)^6 = 2^{30} = (2^3)^{10} = 8^{10}$ ។
- **កន្សោមបញ្ច្រាសស្វ័យគុណនៃផលគុណ (Inverse Corollary)**៖ $25^3 \cdot 4^3 = (25 \times 4)^3 = 100^3 = 1{,}000{,}000$ ។

---

## ២. បញ្ជីឯកសារយោងដែលបានផ្ទៀងផ្ទាត់ (Verified Open-Access Sources: `15` PDFs)

តារាងខាងក្រោមផ្គូផ្គង ១-ទល់-១ ជាមួយលេខរៀង `01–15` ក្នុងថត `ឯកសារស្រាវជ្រាវយោង_PDF\` (`00_បញ្ជីឯកសារភស្តុតាង_Evidence_Index.md`) រៀបតាមអក្ខរក្រមនាមត្រកូលអ្នកនិពន្ធទី១៖

| # | ឯកសារ PDF (`papers/`) | លេខរៀងក្នុង `ឯកសារស្រាវជ្រាវយោង_PDF\` | ទំព័រ (Chars) | SHA-256 (12) | APA 7th Citation & DOI/URL | មុំស្រាវជ្រាវ |
|---:|---|---|---:|---|---|---|
| **01** | [misconceptions_2014_booth.pdf](papers/misconceptions_2014_booth.pdf) | `01_Booth2014_AlgebraicErrors.pdf` | 14 (59,945) | `c785589fbec5` | Booth, J. L., Barbieri, C., Eyer, F., & Paré-Blagoev, E. J. (2014). Persistent and pernicious errors in algebraic problem solving. *Journal of Problem Solving*, *7*, 10–23. https://doi.org/10.7771/1932-6246.1161 \| ERIC: https://files.eric.ed.gov/fulltext/EJ1059995.pdf | Misconceptions |
| **02** | [activities_2013_ellis.pdf](papers/activities_2013_ellis.pdf) | `02_Ellis2013_ExponentialCovariation.pdf` | 8 (27,705) | `ecfe2d471d8b` | Ellis, A. B., Ozgur, Z., Kulow, T., Dogan, M. F., Williams, C., & Amidon, J. (2013). Correspondence and covariation: Quantities changing together. In M. Martinez & A. Castro Superfine (Eds.), *Proceedings of the 35th Annual Meeting of the North American Chapter of the International Group for the Psychology of Mathematics Education* (pp. 119–126). University of Illinois at Chicago. https://files.eric.ed.gov/fulltext/ED584480.pdf | Hands-on / Covariation |
| **03** | [activities_2023_gustina.pdf](papers/activities_2023_gustina.pdf) | `03_Gustina2023_POEMetaAnalysis.pdf` | 13 (40,604) | `f429a73f11cd` | Gustina, R., Hastuti, I. D., Nizaar, M., & Syaharuddin, S. (2023). Predict Observe Explain learning model: Implementation and its influence on students’ critical thinking ability and learning outcomes (A meta-analysis study). *Jurnal Kependidikan: Jurnal Hasil Penelitian dan Kajian Kepustakaan di Bidang Pendidikan, Pengajaran dan Pembelajaran*, *9*(2), 706–718. https://doi.org/10.33394/jk.v9i2.7388 \| OA PDF: https://e-journal.undikma.ac.id/index.php/jurnalkependidikan/article/download/7388/4538 | POE Meta-Analysis |
| **04** | [proof_2024_klingbeil.pdf](papers/proof_2024_klingbeil.pdf) | `04_Klingbeil2024_FormativeAssessmentMC.pdf` | 15 (67,617) | `0bf550669f5b` | Klingbeil, K., Rösken, F., Barzel, B., Schacht, F., Stacey, K., Steinle, V., & Thurm, D. (2024). Validity of multiple-choice digital formative assessment for assessing students’ (mis)conceptions: Evidence from a mixed-methods study in algebra. *ZDM – Mathematics Education*, *56*(4), 713–726. https://doi.org/10.1007/s11858-024-01556-0 | Formative MC Foils |
| **05** | [activities_2016_larbi.pdf](papers/activities_2016_larbi.pdf) | `05_Larbi2016_AlgebraTileManipulatives.pdf` | 9 (44,372) | `d75db11a8882` | Larbi, E., & Mavis, O. (2016). The use of manipulatives in mathematics education. *Journal of Education and Practice*, *7*(36), 53–61. https://files.eric.ed.gov/fulltext/EJ1126428.pdf | Hands-on / Area Tiles |
| **06** | [proof_2023_ngo.pdf](papers/proof_2023_ngo.pdf) | `06_Ngo2023_SuperfluousBrackets.pdf` | 22 (83,609) | `8362869c81f4` | Ngo, V., Perez Lacera, L., Closser, A. H., & Ottmar, E. (2023). The effects of operator position and superfluous brackets on student performance in simple arithmetic. *Journal of Numerical Cognition*, *9*(1), 107–128. https://doi.org/10.5964/jnc.9535 | B&W Bracket Grouping |
| **07** | [misconceptions_2011_olson.pdf](papers/misconceptions_2011_olson.pdf) | `07_Olson2011_NegativeSignAmbiguity.pdf` | 8 (30,613) | `fc376cfc83a9` | Olson, J. C., Cangelosi, R., Madrid, S., Cooper, S., & Hartter, B. (2011). Ambiguity of the negative sign. In L. R. Wiest & T. Lamberg (Eds.), *Proceedings of the 33rd Annual Meeting of the North American Chapter of the International Group for the Psychology of Mathematics Education* (pp. 113–120). University of Nevada, Reno. https://files.eric.ed.gov/fulltext/ED585963.pdf | Misconceptions |
| **08** | [proof_2024_ozcan.pdf](papers/proof_2024_ozcan.pdf) | `08_Ozcan2024_WEI4SWorkedExamples.pdf` | 20 (77,351) | `7bb1025acf0e` | Özcan, Z. Ç. (2024). Evaluating the impact of the WEI4S instructional approach on middle school students’ algebraic problem-solving skills. *Education Sciences*, *14*(1), 102. https://doi.org/10.3390/educsci14010102 | Worked Examples / CLT |
| **09** | [activities_2017_runisah.pdf](papers/activities_2017_runisah.pdf) | `09_Runisah2017_5EMetacognitive.pdf` | 12 (39,695) | `c8c340461257` | Runisah, Herman, T., & Dahlan, J. A. (2017). Using the 5E learning cycle with metacognitive technique to enhance students’ mathematical critical thinking skills. *International Journal on Emerging Mathematics Education (IJEME)*, *1*(1), 87–98. https://doi.org/10.12928/ijeme.v1i1.5698 \| OA PDF: http://journal.uad.ac.id/index.php/IJEME/article/download/5698/pdf_6 | 5E + Metacognition |
| **10** | [misconceptions_2024_senay.pdf](papers/misconceptions_2024_senay.pdf) | `10_Senay2024_ExponentsAbstraction.pdf` | 15 (46,081) | `587dd2371c13` | Şenay, Ş. C. (2024). Analysis of misconceptions and errors regarding exponential and radical expressions through the theory of reducing abstraction. *Research on Education and Psychology (REP)*, *8*(2), 281–295. https://doi.org/10.54535/rep.1520588 | Misconceptions |
| **11** | [misconceptions_2024_theba.pdf](papers/misconceptions_2024_theba.pdf) | `11_Theba2024_BracketsStructureSense.pdf` | 11 (62,489) | `542636edecf4` | Theba, N. M., Pournara, C., & Takker, S. (2024). Simplifying algebraic expressions with brackets: Insights into Grade 10 learners’ structure sense through a study of their errors. *Pythagoras*, *45*(1), a783. https://doi.org/10.4102/pythagoras.v45i1.783 \| ERIC: https://files.eric.ed.gov/fulltext/EJ1432429.pdf | Misconceptions |
| **12** | [activities_2021_turan.pdf](papers/activities_2021_turan.pdf) | `12_Turan2021_5EMiddleSchoolMath.pdf` | 19 (57,418) | `23663f957513` | Turan, S., & Matteson, S. M. (2021). Middle school mathematics classrooms practice based on 5E instructional model. *International Journal of Education in Mathematics, Science, and Technology (IJEMST)*, *9*(1), 22–39. https://doi.org/10.46328/ijemst.1041 \| ERIC: https://files.eric.ed.gov/fulltext/EJ1282262.pdf | 5E Fidelity & Pacing |
| **13** | [misconceptions_2019_ulusoy.pdf](papers/misconceptions_2019_ulusoy.pdf) | `13_Ulusoy2019_IntegerExponentsObstacles.pdf` | 19 (84,577) | `12ec41aca688` | Ulusoy, F. (2019). Serious obstacles hindering middle school students’ understanding of integer exponents. *International Journal of Research in Education and Science (IJRES)*, *5*(1), 52–69. https://files.eric.ed.gov/fulltext/EJ1198050.pdf | Misconceptions |
| **14** | [proof_2022_vest.pdf](papers/proof_2022_vest.pdf) | `14_Vest2022_SelfExplanationWorkedExamples.pdf` | 7 (33,770) | `b754beddbcd5` | Vest, N. A., Silla, E. M., Bartel, A. N., Nagashima, T., Aleven, V., & Alibali, M. W. (2022). Self-explanation of worked examples integrated in an Intelligent Tutoring System enhances problem solving and efficiency in algebra. In J. Culbertson, A. Perfors, H. Rabagliati, & V. Ramenzoni (Eds.), *Proceedings of the 44th Annual Conference of the Cognitive Science Society* (pp. 3466–3472). Cognitive Science Society. https://files.eric.ed.gov/fulltext/ED623402.pdf | Proof / Warrants |
| **15** | [proof_2019_yeo.pdf](papers/proof_2019_yeo.pdf) | `15_Yeo2019_FingerTracingWorkedExamples.pdf` | 11 (47,022) | `597e4aec633c` | Yeo, L.-M., & Tzeng, Y.-T. (2019). Tracing effect in the worked examples-based learning: An exploration of individual differences in working memory capacity. *EURASIA Journal of Mathematics, Science and Technology Education*, *15*(10), Article em1760. https://doi.org/10.29333/ejmste/105482 | Tracing & WMC |

---

## ៣. សំយោគភស្តុតាងជាក់ស្ដែង (Empirical Synthesis)

- **មុំទី១ — ការយល់ច្រឡំ និងឧបសគ្គការគិតរបស់សិស្ស (`Ulusoy, 2019`; `Şenay, 2024`; `Theba et al., 2024`; `Olson et al., 2011`; `Booth et al., 2014`)**៖
  1. *ការច្រឡំរូបមន្ត $(a^m)^n$ ជាមួយ $a^m \cdot a^n$ និងការថយក្រោយកម្រិតអរូបី*៖ `Ulusoy (2019)` បានរកឃើញក្នុងសិស្សថ្នាក់ទី៨ ចំនួន `N = 165` (+ សម្ភាសន៍ `n = 12`) ថាជាង `65%` ធ្វើត្រូវតិចជាង `3/10` លំហាត់ ដោយសិស្សបូកនិទស្សន្តពេលបូកគោល (`18.1%` ក្នុង $3^5+3^5+3^5 \to 3^{15}$; `24.8%` ក្នុង $2^4+2^{-2}+2^3 \to 2^9$ ឬ $2^5$), គុណនិទស្សន្តពេលគុណគោលដូចគ្នា (`8.4%` ក្នុង $5^{-2}\cdot 5^4 \to 5^{-8}$ ឬ $5^8$), ចែក/គុណនិទស្សន្តក្នុងផលចែក (`13%` ចែក, `4.2%` គុណ) និង `4%` គុណគោលនឹងនិទស្សន្ត ($a^b = a\cdot b$)។ ចំណែក `Şenay (2024)` (សំយោគ `5` ការសិក្សារួមទាំង `Şenay 2002 N=729` និង `Avcu 2010 N=159` ថ្នាក់ទី៨) បង្ហាញថា **`34%`** ខុសលើការរៀបលំដាប់ $(2^3)^2, 2^{(3^2)}, (2^3)^{-2}$ ដោយបោះបង់ទម្រង់រូបមន្តហើយបង្វិលទៅគណនាដំណើរការគុណដដែលៗ (`process–object reduction`)។
  2. *អារម្មណ៍បំភាន់លីនេអ៊ែរ (`Freshman's Dream`)*៖ `Theba et al. (2024)` (`N = 58` ច្បាប់ចម្លើយពី `N = 155`) រកឃើញថា កន្សោម `2(x+3)^2` មានអត្រាកំហុសខ្ពស់បំផុត **`35/58 (60.3%)`** ដោយសិស្សបំបែកស្វ័យគុណចូលក្នុងផលបូក `2(x^2+9)` (`DL5`, ទន្ទឹមនឹងការច្រឡំក្នុង $(a+b)^n$ ធៀប $(ab)^n$) និងគុណមេគុណខាងក្រៅចូលមុនស្វ័យគុណ `(2x+6)^2` (`BG3F1`)។
  3. *ការភ្លេចមេគុណក្នុង $(ab)^n$ និងដែនកំណត់សញ្ញាដក/វង់ក្រចក*៖ `Booth et al. (2014)` (`N = 565` Algebra I, `35%` ថ្នាក់ទី៧–៨, ពហុធា `N = 418`) បង្ហាញថា កំហុសសញ្ញាដក (`M = 1.96`, ខ្ពស់បំផុតទូទៅ; ទាយទុក្ខលំបាកប្រឡងចុងឆ្នាំថ្នាក់ទី៨ $r = -.19, p < .001$), កំហុសអថេរ/និទស្សន្ត (`~1.75` កំហុស/សិស្សលើពហុធា) និងកំហុសបំបែកមិនគ្រប់តួ (`~0.80` កំហុស/សិស្ស, ទស្សន៍ទាយពិន្ទុចុងឆ្នាំ $\beta = -.10, -.09, p < .05; R^2 = .216$) កើតឡើងជាប្រចាំ — ដូចគ្នានឹងសិស្សសរសេរ $(3xy^2)^3 = 3x^3y^6$។ បន្ថែមលើនេះ `Olson et al. (2011)` (`N = 904`, សម្ភាសន៍ `n = 19`) រកឃើញ `6/19` នាក់ថា *"វង់ក្រចកគ្មានន័យ"* លើ `(-17)^8` vs `-17^8` និងមានតែ `2/19` អានត្រូវ `-9^{3/2}` ជាចំនួនផ្ទុយបូក (`additive inverse`), បញ្ជាក់ពីហានិភ័យនៃ `-2(a^{-3}b^5)^2` ក្លាយជា `(-2)^2`។
  4. *ស្វ័យគុណសូន្យ និងអវិជ្ជមាន (`Step 2 HW` & `E5`)*៖ `Ulusoy (2019)` រាយការណ៍ថា ក្នុង `-3^0` (`66.1%` ខុស) `30.9%` ឆ្លើយ `1`, `14.5%` ឆ្លើយ `-3`, `6.6%` ឆ្លើយ `0`; ក្នុង `2^{-4}` (`63.6%` ខុស) `23.6%` ឆ្លើយ `-16` និង `13.9%` ឆ្លើយ `+16` ហើយ `16%–20%` ប្ដូរសញ្ញាគោលពេលឃើញនិទស្សន្តដក ឬ `66%` (`Şenay, 2024`) ជំនួសលេខចៃដន្យជំនួសការមើលរចនាសម្ព័ន្ធ $(a^2 > 0)$។

- **មុំទី២ — ពិសោធន៍ផ្ទាល់ដៃ ផ្ទាំងក្រឡា និង `POE` ក្នុងគំរូ `5Es` (`Turan & Matteson, 2021`; `Runisah et al., 2017`; `Gustina et al., 2023`; `Larbi & Mavis, 2016`; `Ellis et al., 2013`)**៖
  - `Turan & Matteson (2021)` (`N = 14` ម៉ោង 45–50 នាទី) រកឃើញថាគ្រូជាប់នៅ `Engage (2.6)` និង `Explore (2.6)` បាត់បង់ `Elaborate (= 0)` ទាំងស្រុងដោយសារអស់ពេល ហើយ `Explain (1.6 / 1.75)` ធ្លាក់ទាបព្រោះគ្រូនិយាយតែម្នាក់ឯង (`Evaluate = 2.0` រុញទៅកិច្ចការផ្ទះ) — បង្ហាញពីភាពចាំបាច់នៃការកំណត់នាទីតឹងរ៉ឹង (`2+9+17+20+≤2 = 50 min`)។
  - `Runisah et al. (2017)` (`N = 173` **ថ្នាក់ទី៨**) បញ្ជាក់ថា `5E + មេតាកូញីទីវ (LCM)` ជួយកើនពិន្ទុខ្ពស់ជាង `5E` ធម្មតា (`g = 0.62` ធៀប `0.49`; មធ្យម `27.30 [68.3%]` ធៀប `22.84 [57.1%]` និង `CL 17.80 [44.5%]`, $\chi^2 = 44.01, p = .000$) តាមរយៈសំណួរ Beeth ទាំង ៣ (*intelligibility, plausibility, wide-applicability*)។
  - `Gustina et al. (2023)` (វិភាគមេតា 70 សំណុំទិន្នន័យ) បង្ហាញប្រសិទ្ធភាព `POE` ក្នុងគណិតវិទ្យា (`RE = 0.67 [0.40, 0.94]`, `N = 80`) លើសវិទ្យាសាស្ត្រធម្មជាតិ (`RE = 0.53`) ជាពិសេសលើលទ្ធផលសិក្សា (`RE = 0.66`)។
  - `Larbi & Mavis (2016)` (`N = 56` **JHS 2 / ថ្នាក់ទី៨**) បញ្ជាក់ថាបន្ទះក្រឡាពិជគណិត (`algebra tiles`) បង្កើនលទ្ធផលខ្ពស់ (`M = 32.16` ធៀប `20.35`, $t(54) = 4.797, p = .000, \eta^2 = 0.298$) និងបំបាត់កំហុសចែកស្វ័យគុណលើផលបូក $(x+4)^2 \neq x^2+16$ (ផ្ទុយផ្ទាល់នឹង $(3b)^2=9b^2$ ធៀប $(2+3)^2 \neq 2^2+3^2$)។ `Ellis et al. (2013)` (ថ្នាក់ទី៨) បង្ហាញការផ្ដុំកត្តាផលគុណតាមជំហានពេលជួយឆ្លងពីការគុណដដែលៗទៅច្បាប់ស្វ័យគុណ $(2^3)^4 = 2^{12}$។

- **មុំទី៣ — ជំនួយកាត់បន្ថយបន្ទុកគិត (`CLT`), សញ្ញា B&W និងការវាយតម្លៃ (`Özcan, 2024`; `Vest et al., 2022`; `Yeo & Tzeng, 2019`; `Ngo et al., 2023`; `Klingbeil et al., 2024`)**៖
  - `Özcan (2024)` (`N = 36`, `WEI4S`: វិភាគលំហាត់គំរូ $\to$ ពន្យល់ខ្លួនឯង $\to$ វិភាគកំហុស $\to$ អនុវត្ត) លើកកម្ពស់ Conceptual Knowledge (`25.74` ធៀប `14.48`, $F(1,36) = 36.95, p < .001$, `53%`), Far Transfer (`6.58` ធៀប `2.06, p < .05`) និងបន្ថយ Intrinsic Load (`18.16 -> 13.32, p < .01`) និង Extraneous Load (`6.47` ធៀប `11.88, p < .001`)។
  - `Vest et al. (2022)` (`N = 167` មធ្យមសិក្សាបឋមភូមិ) បង្ហាញថាការបង្គាប់សិស្សជ្រើសរើសហេតុផលគោលគំនិត (`Conceptual Warrant`) លើលំហាត់ត្រូវនិងខុសបង្កើនពិន្ទុគោលគំនិត ($\beta = 1.23, p = .008$) បន្ថយកំហុស ($\beta = -0.34, p = .004$) និងបន្ថយពេលដោះស្រាយ (`-5.83 s/step, p = .006`)។
  - `Yeo & Tzeng (2019)` (`N = 72`, អាយុ `11–13`) បញ្ជាក់ថា `[tracing]` ជួយសិស្សគ្រប់កម្រិត WMC បង្កើនការផ្ទេរចំណេះ (`M = 3.00` ធៀប `2.31, p = .003, η² = .121`) និងបន្ថយភាពលំបាក (`p < .001`)។
  - `Ngo et al. (2023)` (`N = 528` វិភាគ) បង្ហាញថា វង់ក្រចកសម្គាល់រចនាសម្ព័ន្ធ B&W (`common visual region`, គ្មានទឹកថ្នាំពណ៌) បង្កើនល្បឿនស្ទាត់ (`B = -0.12, p = .002`; កន្សោមកណ្ដាល `M = 3.66` ធៀប `5.17` លំហាត់, `p < .001`) — គាំទ្រការព័ទ្ធ `[3]·[x^1]·[y^2]` និង `[-2][(a^{-3})(b^5)]^2`។
  - `Klingbeil et al. (2024)` (`N = 600` ចម្លើយសរសេរ) បង្ហាញថា ជម្រើសបំភាន់ដែលរចនាតាមកំហុសជាក់ស្ដែង (`92%–97%` concordance) និងប្រើទម្រង់សំណួរច្រើនផ្នែក អាចវាយតម្លៃកំហុសសិស្សបានសុក្រឹតក្នុង 90 វិនាទី។

---

## ៤. ផែនទីបម្លែងចូលក្នុងកិច្ចតែងការ ៥០ នាទី (`2 + 9 + 17 + 20 + ≤2 = 50 min`)

| ជំហាន / 5Es (នាទី) | បញ្ហាភស្តុតាងដែលត្រូវដោះស្រាយ | ការកែលម្អជាក់ស្ដែងក្នុងកញ្ចប់ ៤ ឯកសារ (`_EXP412`) |
|---|---|---|
| **ជំហានទី ១** (`2 min`) | រៀបចំក្រុមប្រកបដោយសណ្ដាប់ធ្នាប់ និងត្រៀមតួនាទីសហការ | រដ្ឋបាលថ្នាក់ និងបែងចែកក្រុម `៣ នាក់/ក្រុម` សម្រាប់សកម្មភាព 1:1 POE និង Proof Relay ៣ តួនាទី (`Role 1–3`) |
| **ជំហានទី ២ — កំណែ & រំលឹក** (`≤3 + 3 = 6 min`) | កំហុសស្វ័យគុណសូន្យ/អវិជ្ជមាន (`Ulusoy, 2019`: `30.9%–66.1%`) និងការគុណស្វ័យគុណគោលដូចគ្នា | កំណែលំហាត់ផ្ទះ (`Book p. 16 ប្រតិបត្តិ ក–ឃ`) ដោយបង្ហាញអន្ទាក់ $y^0=1$ និង $\left(\frac{3yx^9}{-15y^5x^4}\right)^0=1$; រំលឹក $a^n$, $a^{-n}=\frac{1}{a^n}$ ($a\neq 0$), $a^m\cdot a^n=a^{m+n}$ |
| **E1 - Engage** (`3 min`) | ទប់ស្កាត់ការចាប់ផ្ដើមដោយសូត្ររូបមន្តស្ងួត និងភ្ជាប់ការគុណស្ទួន (`Ellis et al., 2013`) | បេសកកម្មពិតពីរ៖ **(១)** អង្គចងចាំកុំព្យូទ័រពង្រីក ៤ តំណាក់កាល $(2^3)^4$ ប៉ុន្មានប៊ីត (ប្រៀបធៀប $2^{12}$ vs $2^7$); **(២)** ក្រាលការ៉ូការ៉េជ្រុង $3b$ ម៉ែត្រ $(3b)^2$ ត្រូវការប៉ុន្មានផ្ទាំង $b^2$ (ប្រៀបធៀប $3b^2$ vs $9b^2$) — សួរយកទស្សន៍ទាយមុន |
| **E2 - Explore** (`11 min`) | ការបូកនិទស្សន្តជំនួសគុណ (`Ulusoy, 2019`; `Şenay, 2024`) និងការបំបែកស្វ័យគុណលើផលបូក (`Theba et al., 2024`; `Larbi & Mavis, 2016`) | **Dual POE លើ `Printable p. 1` មាត្រដ្ឋាន `1:1`** (`Gustina et al., 2023`):<br>• **ស្ថានីយ៍ ១ (Multiplicative Strips)**: កាត់/តម្រៀបបន្ទះក្រដាស $(2^3)^4$ (`4` ក្រុមនៃ `2·2·2`) ធៀប $2^3\cdot 2^4$ (`3+4=7` កត្តា)<br>• **ស្ថានីយ៍ ២ (Area Grid & Rotated Counter-Example)**: ផ្គុំក្រឡា $3b \times 3b = 9b^2$ និងពិសោធន៍ការ៉េបង្វិល (`~140°`) $(2+3)^2 = 25 \neq 2^2+3^2 = 13$ (បង្ហាញផ្នែកបាត់ $2\times(2\times 3)=12$) |
| **E3 - Explain** (`6 min`) | គ្រូបង្រៀនផ្ដាច់មុខ (`Turan & Matteson, 2021`) និងការខ្វះមូលហេតុ/សំអាង (`Runisah et al., 2017`; `Vest et al., 2022`) | សិស្សបង្គុំប្រអប់ `ជាទូទៅ 4.1 & 4.2` (`Book p. 17`) $\to$ តារាង **សម្មតិកម្ម–សន្និដ្ឋាន–វិបាក** (រួមទាំងលក្ខខណ្ឌ $a\neq 0, b\neq 0$ និងច្បាប់បញ្ច្រាស $a^nb^n=(ab)^n$) + ផ្ទាំង **Warrant Bank `①–⑤`** + សំណួរមេតាកូញីទីវ Beeth ទាំង ៣ |
| **E4 - Elaborate** (`10 min`) | បន្ទុកគិតខ្ពស់ និងកំហុសភ្លេចមេគុណ/វង់ក្រចក (`Özcan, 2024`; `Yeo & Tzeng, 2019`; `Ngo et al., 2023`; `Booth et al., 2014`) | លំហាត់គំរូ `4.1` (`p. 17`: $(10^2)^3$, $(a^{-2})^k(a^k)^5$) & `4.2` (`p. 18`: $(3xy^2)^3$, $(b^3)(b^{2k-1})^3$) ប្រើសញ្ញាសម្គាល់ B&W (`[tracing]` ម្រាមដៃ + វង់ក្រចក `[3]·[x^1]·[y^2]`) + **EIA Looking-Back** ចាប់កំហុស $3x^3y^6$ និងពិនិត្យវិសាលភាពស្វ័យគុណ |
| **E5 - Evaluate** (`10 min`) | ការបាត់បង់ `Evaluate` (`Turan & Matteson, 2021`), សញ្ញាដកក្រៅវង់ក្រចក (`Olson et al., 2011`) និងការស្ទង់កំហុសរហ័ស (`Klingbeil et al., 2024`) | • **Relay ៣ តួនាទី (`~6.5 min`)** លើ `ប្រតិបត្តិ` (`p. 17`: $(a^3)^{-2}$, $a(a^4)^5 a^{-6}$ និង `p. 18`: $-2(a^{-3}b^5)^2$, បញ្ជាក់ពុម្ព `p. 18 ខ`) មាន `Pause-Ask / Pause-Review`<br>• **បិទបេសកកម្ម E1 (`~1 min`)**: បញ្ជាក់ $(2^3)^4=2^{12}$ & $(3b)^2=9b^2$<br>• **Exit Ticket `90s` (`~2.5 min`, Foils `A–D`)**: ទម្រង់ខុសគ្នាដកស្រង់ចំកំហុសទាំង ៤ |
| **ជំហានទី ៥ — កិច្ចការផ្ទះ** (`≤2 min`) | ភ្ជាប់ជំនាញប្រើផ្ទាល់និងបញ្ច្រាសនៃច្បាប់ស្វ័យគុណទាំងពីរ | សៀវភៅ `pp. 25–26`: `#2ក` $(4^3)(2^2)$, `#7ង` ភាគយក $(32a^2x^8)^3$, `#8ក, ខ, គ` ($x^{12}, y^{15}, 2^{18}, (2^5)^6$) និងស្វ័យគុណផលគុណបញ្ច្រាស $25^3 \cdot 4^3 = (25\times 4)^3 = 100^3$ |

---

## ៥. ធនាគារហេតុផលស-ខ្មៅ (B&W Warrant Bank `①–⑤`, Print-Safe Standard)

សម្រាប់ប្រើប្រាស់ដូចគ្នា ១០០% នៅក្នុង `LS_Plan_EXP412.tex`, `Teaching_Scenario_EXP412.tex`, `Teaching_Guideline_EXP412.tex` និង `Printable_Materials_EXP412.tex` (ជំនួសការប្រើពណ៌ដោយ `[tracing]` និងវង់ក្រចក `[...]` B&W)៖

- **`①` និយមន័យស្វ័យគុណ & មូលដ្ឋានគុណគោលដូចគ្នា**: $a^n = \underbrace{a\cdot a\cdots a}_{n\text{ កត្តា}}$; $a^m \cdot a^n = a^{m+n}$; $a^0 = 1$ និង $a^{-n} = \frac{1}{a^n}$ ($a \neq 0$)។
- **`②` ច្បាប់ស្វ័យគុណនៃស្វ័យគុណ (`4.1 p. 17`)**: $(a^m)^n = (a^n)^m = a^{m\cdot n}$ (គុណនិទស្សន្តនឹងនិទស្សន្ត មិនមែនបូក $m+n$ ទេ; បើ $m<0$ ឬ $n<0$ ត្រូវ $a \neq 0$)។
- **`③` ច្បាប់ស្វ័យគុណនៃផលគុណ (`4.2 p. 17`)**: $(a\cdot b)^n = a^n \cdot b^n$ (ផ្ដល់និទស្សន្ត $n$ ឱ្យ **គ្រប់កត្តាគុណទាំងអស់** រួមទាំងមេគុណលេខ និងបញ្ច្រាស $a^n b^n = (ab)^n$)។
- **`④` ច្បាប់វិសាលភាពវង់ក្រចក & សញ្ញាដក (`Order & Scope`)**: ស្វ័យគុណគ្របដណ្ដប់តែលើមូលដ្ឋានដែលវង់ក្រចកព័ទ្ធជាប់ផ្ទាល់ (`-2(x)^2 \neq (-2x)^2`; $2(a^{-3}b^5)^2 \neq (2a^{-3}b^5)^2$)។
- **`⑤` អន្ទាក់ហាមបំបែកលើផលបូក (`Anti-Linearity Guard`)**: ស្វ័យគុណ **មិនចែកចាយ** លើផលបូក ឬផលដកឡើយ៖ $(a+b)^n \neq a^n + b^n$ (ឧ. $(2+3)^2 = 25 \neq 2^2 + 3^2 = 13$)។
