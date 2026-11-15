# Research Brief (`_EXP1`): ២.១ សញ្ញាណស្វ័យគុណ

- **Slice**: Algebra Lesson 2 — Sub-section `២.១` (`២.១_សញ្ញាណស្វ័យគុណ`, suffix `_EXP1`)
- **Teaching Context**: Grade 8 Algebra — Lesson 2 (`មេរៀនទី២៖ ស្វ័យគុណ`), Preah Krasang Secondary School (`អនុវិទ្យាល័យព្រះក្រសាំង`), Kampong Svay, Kampong Thom (`New Generation School`, Teacher: `ហុក ប៊ុនថែន`)
- **Scheduled Teaching Date**: Monday, Nov 16, 2026 (`ថ្ងៃចន្ទ ៧កើត ខែកត្តិក ឆ្នាំមមី អដ្ឋស័ក ព.ស. ២៥៧០` | `ថ្ងៃចន្ទ ទី១៦ ខែវិច្ឆិកា ឆ្នាំ២០២៦`)
- **Textbook Source**: MoEYS Grade 8 Mathematics (`Book pp. 13–14, 25` = `PDF pp. 18–19, 30`; prior homework `Book pp. 11–12` = `PDF pp. 16–17`)
- **Verified Open-Access Corpus**: **15 PDFs** (`12` new zero-CAPTCHA Open-Access algebra/exponent papers + `3` foundational verified cognitive/modeling papers), all verified with `PyMuPDF` (`b'%PDF-'`, `> 15 KB`, `7–40` pages, `19,778–112,136` extracted chars) and **100% SHA-256 parity** across `03_...\២.១_សញ្ញាណស្វ័យគុណ\papers\` and `01_...\២.១_សញ្ញាណស្វ័យគុណ\ឯកសារស្រាវជ្រាវយោង_PDF\`.

---

## 1. Textbook Ground-Truth Audit, Verbatim Transcriptions & 4 Mandatory Errata / Alignment Alerts (`Book pp. 13–14, 25`)

Visual inspection of rendered pages `book_p13.png` (`PDF p. 18`), `book_p14.png` (`PDF p. 19`), and `book_p25.png` (`PDF p. 30`) from `សៀវភៅសិក្សាគោល_គណិតវិទ្យា_ថ្នាក់ទី៨_MoEYS.pdf` establishes the verbatim textbook text and **4 mandatory pedagogical fixes / alignment alerts**:

### 1.1 Opening Example & Reading Powers (`Book p. 13` — `1. សញ្ញាណស្វ័យគុណ`)
- **Lesson Objectives Printed on `Book p. 13`**:
  - `• គណនាស្វ័យគុណនៃមួយចំនួន`
  - `• គុណនិងចែកស្វ័យគុណដែលមានគោលដូចគ្នា`
  - `• សរសេរមួយចំនួនក្នុងទម្រង់ស្វ័យគុណ ។`
  *(Note: In this 1-hour / 50-minute slice `២.១`, instruction targets Bullet 1 & Bullet 3 for positive integer exponents $n \in \mathbb{Z}^+$, preparing the conceptual foundation for `២.២` multiplication/division on `pp. 15–16`.)*
- **Verbatim Introductory Example (`Book p. 13`)**:
  - `ឧទាហរណ៍ ៖ សហរដ្ឋអាមេរិចមានអាកាសយានដ្ឋានឯកជនរហូតដល់ជាង 10 000 កន្លែង ។ ចំនួននេះអាចសរសេរបានក្នុងទម្រង់ 10 000 = 10 × 10 × 10 × 10 ឬ 10^4 ។`
  - `10 000 = 10 × 10 × 10 × 10 = 10^4 ដែល ៖`
    - `ចំនួន 10 ហៅថា គោល`
    - `ចំនួន 4 ហៅថា និទស្សន្ត`
    - `ចំនួន 10^4 ហៅថា ស្វ័យគុណ ។`
- **ERRATUM #1 — Reading Powers Header Typo (`Book p. 13`, Line 14)**:
  - **Verbatim Header**: `ស្វ័យគុណ 5^2 , 9^3 , 8^2 និង (4/3)^7 អានដូចខាងក្រោម ៖`
  - **Verbatim Bullets**:
    - `• 5^2 អានថា 5 ស្វ័យគុណ 2 ឬ 5 ការេ`
    - `• 9^3 អានថា 9 ស្វ័យគុណ 3 ឬ 9 គូប`
    - `• 8^4 អានថា 8 ស្វ័យគុណ 4`
    - `• (4/3)^7 អានថា 4/3 ស្វ័យគុណ 7 ។`
  - **Mandatory Fix**: The header erroneously prints **`8^2`** whereas the third bullet reads **`8^4`**. In `E3`, the teacher explicitly directs students to cross out `8^2` on line 14 of `Book p. 13` and write **`8^4`** (plus add convention $a^1 = a$ read as «$a$ ស្វ័យគុណ $1$ ស្មើនឹង $a$ ខ្លួនឯង»).

### 1.2 Definition Box & Domain Error (`Book p. 14` Top — ERRATUM #2)
- **Verbatim Definition Box (`Book p. 14`)**:
  > `និយមន័យ ៖ បើ a ជាចំនួនសនិទាននិង n ជាចំនួនគត់រ៉ឺឡាទីបខុសពីសូន្យ នោះគេបាន`
  > $$\underbrace{a \times a \times a \times \dots \times a}_{n\text{ កត្តា}} = a^n \text{ ។}$$
- **ERRATUM #2 — Mathematical Domain Overreach for $n$**:
  - In Khmer MoEYS terminology, `ចំនួនគត់រ៉ឺឡាទីបខុសពីសូន្យ` denotes $\mathbb{Z}^* = \{\dots, -3, -2, -1, 1, 2, 3, \dots\}$. However, a repeated product of **"$n$ factors" (`n កត្តា`)** is mathematically defined **only for positive integers $n \in \mathbb{Z}^+$ ($n \ge 1$)** (`Sureda & Otero, 2019, pp. 611–612`); one cannot write "$-3$ factors of $a$", and for $n < 0$ the base $a$ must also satisfy $a \neq 0$ ($a^{-n} = \frac{1}{a^n}$, which the textbook itself introduces separately later on `Book pp. 17–19` alongside $a^0 = 1$!).
  - **Mandatory E3 Fix**: Have students annotate `Book p. 14`'s definition box to specify **`n ជាចំនួនគត់វិជ្ជមាន (n ≥ 1)`** for the $n$-factor product definition (with $1$ factor convention $a^1 = a$), while previewing that $n = 0$ and $n < 0$ ($a \neq 0$) will be extended via division patterns in later hours of Lesson 2.

### 1.3 Worked Examples, `សម្គាល់` & `ប្រតិបត្តិ` (`Book p. 14` — ERRATUM #3)
- **Verbatim `លំហាត់គំរូទី 1` (`Book p. 14`)**:
  - Prompt: `សរសេរមួយចំនួនក្នុងទម្រង់ស្វ័យគុណ រួចប្រាប់គោល និងនិទស្សន្តរបស់វា ៖`
  - `ក. 4 × 4 × 4 × 4 × 4 × 4` $\to$ `ចម្លើយ ៖ ក. 4 × 4 × 4 × 4 × 4 × 4 = 4^6 (ចំនួន 6 កត្តា) ដែល 4 ជាគោល និង 6 ជានិទស្សន្ត ។`
  - `ខ.` $\underbrace{a \times a \times a \times \dots \times a}_{2010\text{ កត្តា}}$ $\to$ `ខ.` $\underbrace{a \times a \times a \times \dots \times a}_{2010\text{ កត្តា}} = a^{2010}$ `ដែល a ជាគោល និង 2010 ជានិទស្សន្ត ។`
- **Verbatim `លំហាត់គំរូទី 2` (`Book p. 14`)**:
  - Prompt: `គណនាតម្លៃនៃស្វ័យគុណខាងក្រោម` *(omits closing `។` — restore `។`)*
  - `ក. 2^5 = 2 × 2 × 2 × 2 × 2 = 32`
  - `ខ. (2/3)^3 = (2/3) × (2/3) × (2/3) = 8/27`
  - `គ. (-3)^3 = (-3) × (-3) × (-3) = -27`
  - `ឃ. (-2)^6 = (-2) × (-2) × (-2) × (-2) × (-2) × (-2) = 64 ។` *(Horizontal underbrace beneath the 6 factors in `book_p14.png` has a broken printing gap in the middle.)*
- **Verbatim `សម្គាល់` Box (`Book p. 14`)**:
  - `សម្គាល់ ៖ • (-1)^n = 1 បើ n ជាចំនួនគត់គូ`
  - `• (-1)^n = -1 បើ n ជាចំនួនគត់សេស ។`
- **Verbatim `ប្រតិបត្តិ` (`Book p. 14` Bottom)**:
  - `1. សរសេរកន្សោមខាងក្រោមក្នុងទម្រង់ស្វ័យគុណ` *(omits `។`)*៖ `ក. x · x · x · x · x · x` (`= x^6`) | `ខ.` $\underbrace{y \cdot y \cdot y \cdot y \cdots y}_{2013\text{ កត្តា}}$ (`= y^{2013}`).
  - `2. គណនា ៖ ក. 3^4` (`= 81`) | `ខ. (-1/2)^6` (`= 1/64`) | `គ. (-2)^7` (`= -128`).
- **ERRATUM #3 — Punctuation, Broken Brace, Unexplained Dot `·` & Unwarned Parenthesis Scope in `សម្គាល់`**:
  1. Restore missing `។` on `លំហាត់គំរូទី 2` and `ប្រតិបត្តិ 1`, and draw a clean continuous brace with `6 កត្តា` + **3 sign-pairing arcs** $\overbrace{(-2)\times(-2)}^{+4}\times\overbrace{(-2)\times(-2)}^{+4}\times\overbrace{(-2)\times(-2)}^{+4} = +64$.
  2. Explicitly explain in `E4/E5` that algebra replaces `×` with the center dot **`·`** (`x · x = x × x`) so `×` is never confused with variable letter `x`!
  3. Anchor `សម្គាល់` to the **Parenthesis Lock-Box Rule**: $(-1)^n = +1$ for even $n$ holds **ONLY because the minus sign is locked inside `(-1)`**; without parentheses, $-1^n = -(1^n) = -1$ for *every* $n \ge 1$ (`Ulusoy, 2019, p. 61`).

### 1.4 End-of-Lesson Exercises (`Book p. 25` — ERRATUM / CURRICULUM-GAP ALERT #4)
- **Inspection of `Book p. 25` (`លំហាត់` `#1–#4`)**:
  - `#1` (`ចូរសរសេរផលគុណខាងក្រោមជាស្វ័យគុណ`): `ក. 7×7×7×7×7 = 7^5`; `ខ. (1/2)^4`; `គ. (-0.7)^4`; `ឃ. (-3/7)^5`.
  - `#2` (`ចូរគណនាផលគុណខាងក្រោម`): `ក. 5^3 × 2^5 = 125 × 32 = 4000`; `ខ. (-8^2)(-7^3) = (-64)(-343) = 21 952`; `គ. (-3^4)(-6^3) = (-81)(-216) = 17 496`; `ឃ. (-7)^3 × 12^3 = (-343)(1728) = -592 704`.
  - `#3` (`គណនា`): `ក. (4^3)(-3^2) = 64 × (-9) = -576`; `ខ. (-2)^5 (-5)^2 = (-32)(25) = -800`; `គ. (-2^3)(3^2)(-5^2) = (-8)(9)(-25) = 1800`; `ឃ. (-4)^2 (-1/2)^3 = 16 × (-1/8) = -2`.
  - `#4` (`រកបរិមាត្រចតុកោណកែងចំពោះ b = 3` ដែលបណ្ដោយ $b^3 + 1$ និងទទឹង $b^2 - 1$): $L = 3^3 + 1 = 27 + 1 = 28$, $W = 3^2 - 1 = 9 - 1 = 8 \implies P = 2(28 + 8) = 72$.
- **ALERT #4 — Unannounced `(-a^n)` Notation & Homework Curation**:
  - Notice that `Book pp. 13–14` **never** show `-a^n` or `(-a^n)` where the exponent sits *inside* the parentheses (`(-3^2)`, `(-5^2)`, `(-8^2)`, `(-3^4)`), yet `Book p. 25` `#2ខ, #2គ, #3ក, #3គ` test it heavily! Because `(-3^2)` means `-(3^2) = -(3 × 3) = -9` (parentheses wrap the already-negated number `-3^2` solely to separate multiplication factors, NOT to group `-3` as the base!), Grade 8 students who only saw `(-2)^6 = +64` inevitably write `(-3^2) = +9` and `(-5^2) = +25`, reversing the sign of `#3ក` (`+576` instead of `-576`) and `#3គ` (`-1800` instead of `+1800`)!
  - Furthermore, `#2ខ–ឃ` require tedious multi-digit multiplication (`343 × 1728 = 592,704`) with zero added conceptual value.
  - **Mandatory Pedagogical Solution**:
    1. Teach the **Lock-Box Contrast** `(-a)^n` vs. `-a^n` / `(-a^n)` explicitly in **E2 (`POE 2`)**, **E3 (`Warrant ③`)**, **E4 (Worked Comparison Box)**, and **E5 (Diagnostic Card C)**.
    2. Assign curated, conceptually rich, hand-calculable homework from `Book p. 25`: **`#1(ក–ឃ)`, `#3(ក, ខ, ឃ)`** *(with explicit reminder on `#3ក`: `(-3^2) = -(3^2) = -9` vs `#3ខ`: `(-5)^2 = +25`)*, and **`#4`** ($b=3 \implies P=72$, integrating operator precedence `Powers before +/-`).

---

## 2. Curated Open-Access Evidence Corpus (`15` Verified PDFs, `100%` SHA-256 Parity)

| # | Filename | Pp | Chars | SHA-256 (12) | APA 7th In-Text Keys | Complete APA 7th Reference & Verified OA URL / DOI |
|---:|---|---:|---:|---|---|---|
| **01** | `01_Ulusoy2019_MiddleSchoolIntegerExponentsObstacles.pdf` | 19 | 84,574 | `12ec41aca688` | `Ulusoy (2019)` / `(Ulusoy, 2019)` | Ulusoy, F. (2019). Serious obstacles in middle school students' learning of integer exponents. *International Journal of Research in Education and Science*, *5*(1), 52–69. `https://files.eric.ed.gov/fulltext/EJ1198050.pdf` |
| **02** | `02_Moru2022_Grade8AlgebraExponentErrors.pdf` | 15 | 59,929 | `434b6537cc34` | `Moru & Mathunya (2022)` / `(Moru & Mathunya, 2022)` | Moru, E. K., & Mathunya, M. (2022). Error analysis in learning of grade 8 algebra. *Journal of Research and Advances in Mathematics Education*, *7*(3), 130–144. `https://doi.org/10.23917/jramathedu.v7i3.16784` |
| **03** | `03_Sureda2019_FromPowersToExponentialFunction.pdf` | 7 | 19,778 | `51096576ee52` | `Sureda & Otero (2019)` / `(Sureda & Otero, 2019)` | Sureda, P., & Otero, R. (2019). From the powers to the exponential function. *International Electronic Journal of Mathematics Education*, *14*(3), 611–617. `https://doi.org/10.29333/iejme/5774` |
| **04** | `04_DeBock2003_IllusionOfLinearity8thGrade.pdf` | 23 | 71,345 | `abfb11e92901` | `De Bock et al. (2003)` / `(De Bock et al., 2003)` | De Bock, D., Verschaffel, L., Janssens, D., Van Dooren, W., & Claes, K. (2003). Do realistic contexts and graphical representations always have a beneficial impact on students' performance? Negative evidence from a study on modelling non-linear geometry problems. *Learning and Instruction*, *13*(4), 441–463. `https://doi.org/10.1016/S0959-4752(02)00040-3` |
| **05** | `05_Siller2023_ModellingExponentialGrowthClassroom.pdf` | 17 | 71,863 | `e1d899b2ba7a` | `Siller et al. (2023)` / `(Siller et al., 2023)` | Siller, H.-S., Elschenbroich, H.-J., & Greefrath, G. (2023). Mathematical modelling of exponential growth as a rich learning environment for mathematics classrooms. *ZDM – Mathematics Education*, *55*(1), 17–33. `https://doi.org/10.1007/s11858-022-01433-8` |
| **06** | `06_CastilloGarsow2013_ModelingExponentialGrowth.pdf` | 17 | 44,843 | `7ceaf4e64120` | `Castillo-Garsow (2013)` / `(Castillo-Garsow, 2013)` | Castillo-Garsow, C. (2013). The role of multiple modeling perspectives in students' learning of exponential growth. *Mathematical Biosciences and Engineering*, *10*(5–6), 1437–1453. `https://doi.org/10.3934/mbe.2013.10.1437` |
| **07** | `07_Theba2024_BracketsStructureSenseAlgebraErrors.pdf` | 11 | 62,489 | `542636edecf4` | `Theba et al. (2024)` / `(Theba et al., 2024)` | Theba, N. M., Pournara, C., & Takker, S. (2024). Exploring learners' errors with brackets using structure sense in secondary school algebra. *Pythagoras*, *45*(1), Article a783. `https://doi.org/10.4102/pythagoras.v45i1.783` |
| **08** | `08_Bye2024_PerceivingPrecedenceOrderOfOperations.pdf` | 23 | 94,205 | `32e687fe3155` | `Bye et al. (2024)` / `(Bye et al., 2024)` | Bye, J. K., Chan, J. Y.-C., Closser, A. H., Lee, J.-E., Shaw, S. T., & Ottmar, E. R. (2024). Perceiving precedence: How structure and visual cues shape algebraic syntax. *Journal of Numerical Cognition*, *10*, Article e14103. `https://doi.org/10.5964/jnc.14103` |
| **09** | `09_Tabak2019_Grade678OrderOfOperationsMisconceptions.pdf` | 11 | 40,367 | `d76d1f2554b2` | `Tabak (2019)` / `(Tabak, 2019)` | Tabak, S. (2019). 6th, 7th and 8th grade students' misconceptions about the order of operations. *International Journal of Educational Methodology*, *5*(3), 363–373. `https://doi.org/10.12973/ijem.5.3.363` |
| **10** | `10_AliRahman2017_DevelopingSkillsOrderOfOperations.pdf` | 11 | 40,622 | `c418d1f8fa7a` | `Ali Rahman et al. (2017)` / `(Ali Rahman et al., 2017)` | Ali Rahman, E. S., Shahrill, M., Abbas, N. A., & Tan, A. (2017). Developing students' mathematical skills involving order of operations. *International Journal of Research in Education and Science*, *3*(2), 373–382. `https://doi.org/10.21890/ijres.327896` |
| **11** | `11_Lee2020_FractionGroupingMisconceptions.pdf` | 12 | 41,858 | `9f38afd7d49c` | `Lee & Boyadzhiev (2020)` / `(Lee & Boyadzhiev, 2020)` | Lee, H.-J., & Boyadzhiev, I. (2020). Underprepared college students' understanding of rational numbers: Misconceptions on fraction operations and grouping symbols. *International Electronic Journal of Mathematics Education*, *15*(3), Article em0583. `https://doi.org/10.29333/iejme/7835` |
| **12** | `12_Booth2014_PersistentErrorsAlgebraicProblemSolving.pdf` | 14 | 59,945 | `c785589fbec5` | `Booth et al. (2014)` / `(Booth et al., 2014)` | Booth, J. L., Barbieri, C., Eyer, F., & Paré-Blagoev, E. J. (2014). Persistent and pernicious errors in algebraic problem solving. *Journal of Problem Solving*, *7*(1), 10–23. `https://doi.org/10.7771/1932-6246.1161` |
| **13** | `13_Booth2013_CorrectVsIncorrectExamplesAlgebra8th.pdf` | 40 | 72,387 | `92640e3acd42` | `Booth et al. (2013)` / `(Booth et al., 2013)` | Booth, J. L., Lange, K. E., Koedinger, K. R., & Newton, K. J. (2013). Using example problems to improve student learning in algebra: Differentiating between correct and incorrect examples. *Learning and Instruction*, *25*, 24–34. `https://files.eric.ed.gov/fulltext/ED543090.pdf` |
| **14** | `14_Yeo2019_FingerTracingWorkedExamples.pdf` | 11 | 47,022 | `35bbdae4f34c` | `Yeo & Tzeng (2019)` / `(Yeo & Tzeng, 2019)` | Yeo, L.-M., & Tzeng, Y.-T. (2019). Tracing effect in the worked examples-based learning: An exploration of individual differences in working memory capacity. *Eurasia Journal of Mathematics, Science and Technology Education*, *15*(10), Article em1760. `https://doi.org/10.29333/ejmste/105482` |
| **15** | `15_Xu2026_HubSpokeCognitiveStructure.pdf` | 20 | 112,136 | `dbe74af0c6ff` | `Xu et al. (2026)` / `(Xu et al., 2026)` | Xu, Z., Zou, Y., Jin, C., & Li, L. (2026). Help students construct a hub-and-spoke cognitive structure: A key pathway to reduce burden and improve quality in mathematics classroom teaching. *Frontiers in Psychology*, *17*, Article 1974303. `https://doi.org/10.3389/fpsyg.2026.1974303` |

---

## 3. Three-Lens Empirical & Didactical Synthesis

### Lens 1 — Cognitive Obstacles: Multiplicative Trap ($a^n = a\cdot n$), Additive Conflation ($a+a=a^2$) & Role Reversal ($a^n = n^a$)
- **`Ulusoy (2019)`** tested $N = 165$ Grade 8 students across 10 exponent items and conducted clinical interviews with 12 students: only **`3.5%`** answered all items correctly (`p. 56`). While `73.3%` evaluated $2^4 = 16$, **`4%` ($n = 7$)** multiplied base by exponent ($2^4 = 2 \cdot 4 = 8$, $2^6 = 2 \cdot 6 = 12$, `pp. 57, 59`) and **`6.7%` ($n = 11$)** reversed base and exponent ($2^6 = 6 \cdot 6 = 36$, $3^5 = 5 \cdot 5 \cdot 5 = 125$, `pp. 57, 59`).
- **`Moru & Mathunya (2022)`** analyzed $N = 95$ Grade 8 algebra scripts and found **`47.4%` ($45/95$)** committed persistent exponent errors (`Table 2, p. 137`): **`63.2%` ($60/95$)** wrote $d + d = d^2$ (conflating repeated addition $2d$ with repeated multiplication $d \cdot d = d^2$), **`47.4%`** wrote $y^4 + y^4 = y^8$, and **`10.5%–45.3%`** substituted arbitrary numbers for algebraic letters (`Table 5, p. 139`). Similarly, **`Ali Rahman et al. (2017, p. 379)`** documented middle-schoolers computing $1^2 = 1 + 1 = 2$.
- **`De Bock et al. (2003)`** ($N = 313$ including $152$ Grade 8 students + $N = 165$ replication) showed Grade 8 accuracy plunging from `95%` on linear proportional tasks to **`23%`** on non-linear tasks (`F(1,302) = 430.64, p < .01`), with `95%` of errors caused by the *illusion of linearity* (`pp. 451–452`). When asked how many paper layers result from 6 folds, students instinctively predict $2 \times 6 = 12$ instead of $2^6 = 64$.
- **`Sureda & Otero (2019, pp. 611–612)`** demonstrate epistemologically that exponential notation must be built in strict domain stages—first $n \in \mathbb{N}^+$ ($x^1 = x, x^{n+1} = x^n \cdot x$ as $n$ repeated factors) before extending to $x^0 = 1$ and $x^{-n} = 1/x^n$ ($x \neq 0$)—directly justifying **Erratum #2** on `Book p. 14`.

### Lens 2 — Negative Bases, Parenthesis Lock-Boxes, Fractional Bases & Operator Precedence
- **`Booth et al. (2014)`** ($N = 327\text{–}485$ Algebra I students on Grade-8-aligned items) proved that **negative sign errors are the #1 most frequent persistent error** (`M = 1.96` vs. `0.21–0.80` for all other error classes, `F(3.12, 1367.99) = 317.31, p < .001, \eta_p^2 = .42`, `pp. 17–18`) and significantly depress end-of-year mathematics achievement (`R^2 = .216, F = 7.27, p < .001`, `Table 7, p. 18`).
- **`Ulusoy (2019, pp. 57, 61)`** revealed that **`30.9%` ($n = 51$)** of Grade 8 students treated $-3^0 = (-3)^0 = 1$ by ignoring missing parentheses, and interview transcripts showed students overgeneralizing *"even exponent makes negative positive"* to claim **$-2^4 = (-2)^4 = +16$** (`p. 61`).
- **`Theba et al. (2024)`** ($N = 155$ secondary scripts, $n = 58$ fine-grained coded across 11 schools) traced bracket and unary-minus errors to weak *surface vs. systemic structure sense* (failing to *"look before doing"*, `pp. 4, 6–9`) and recommended **paired surface-structure contrast tasks** (`Figure 9, p. 10`)—such as placing **`(-2)^6` vs. `-2^6`** and **`(4^3)(-3^2)` vs. `(4^3)(-3)^2`** side by side.
- **`Bye et al. (2024)`** ($N = 837$ middle schoolers) found learners are **`3.28×` more likely (`OR = 3.28, p < .001, Table 3, p. 15`)** to make precedence errors when the leftmost symbol (such as unary `-` in `-3^2` or `+` in $b^3 + 1$) cannot be evaluated first, and that perceiving equivalent bracketed forms (`-(3^2)`) predicts lower error rates (`r = -.22, p < .001, p. 12`). Complementarily, **`Tabak (2019)`** ($N = 240$, $n = 82$ Grade 8) found `76%–85%` failed multi-operation items due to left-to-right habits (`pp. 366, 368`), while **`Ali Rahman et al. (2017)`** ($N = 21$) showed that a visual **Hierarchy-of-Operators Triangle** (`Powers` at apex $\to \times/\div \to +/-$, `p. 375`) more than doubled test scores from `M = 6.14` to `M = 13.43` (`p < .001, Table 2, p. 378`).
- **`Lee & Boyadzhiev (2020)`** ($41$ items, mean accuracy `47%`, `p. 4`) documented students splitting numerator and denominator independently and ignoring grouping symbols (`pp. 6, 8`), explaining why Grade 8 students write $(\frac{2}{3})^3 = \frac{2^3}{3} = \frac{8}{3}$ instead of $\frac{8}{27}$ or drop sign/denominator powers in $(-\frac{1}{2})^6 = \frac{1}{64}$.

### Lens 3 — Hands-On Doubling Models, Contrasting Incorrect Examples, Finger `[tracing]` & Hub-and-Spoke Schema
- **`Siller et al. (2023, pp. 17, 20, 26)`** and **`Castillo-Garsow (2013, Figure 1, p. 1440)`** establish paper-folding / discrete geometric doubling ($+1$ fold step $\leftrightarrow \times 2$ layer factor: $2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32, 2^6=64$) as a high-impact *Grundvorstellung* that physically shatters the $2 \times 6 = 12$ linear illusion in under 6 minutes.
- **`Booth et al. (2013)`** (`Exp. 1 N = 134, p < .05`; `Exp. 2 N = 64` Grade 8 students) proved that explaining **incorrect worked examples alongside correct ones** significantly improves conceptual learning and cuts Grade 8 encoding errors nearly in half (`3.67` $\to$ `1.90`, `p < .05, Table 3, PDF p. 39`)—grounding our E2 Lock-Box Trap, E4 Side-by-Side Comparison, and E5 Diagnostic Cards `A–D`.
- **`Yeo & Tzeng (2019)`** ($N = 72$, ages 11–13) demonstrated that instructing learners to perform **finger `[tracing]`** on worked examples significantly improves transfer performance (`M = 3.00` vs. `2.31, F(1,68) = 9.38, p = .003, \eta^2 = .121`) and reduces cognitive load (`p < .001, PDF pp. 7–8`). Students trace: (i) the underbrace counting $n$ factors, (ii) the **Lock-Box rectangle** around `(-2)` or `(2/3)` to see what is repeated, and (iii) **sign-pairing arcs** $\overbrace{(-2)(-2)}^{+4}$ to see whether a lone `(-)` remains!
- **`Xu et al. (2026)`** ($N = 60$) showed that organizing rules into a **Hub-and-Spoke cognitive structure** (`p < .001, PDF pp. 5, 9, 13, 16`) dramatically improves conceptual clarity (`2.57 \to 3.88`) and flexible application (`2.56 \to 4.32`), motivating our central Hub $a^n$ connected to 5 monochrome Warrant Spokes `①–⑤`.

---

## 4. Actionable 50-Minute 5Es Lesson Plan Blueprint (`2 + 9 + 17 + 20 + ≤2 min`)

- **Anti-Boredom Classroom Persona (`GEMINI.md` §2)**: **«ក្រុមអ្នកស៊ើបអង្កេតកូដស្វ័យគុណ និងបន្ទះបត់ទ្វេដង»** (*Exponent Code Investigators & Doubling-Fold Squad*).

| Step / Phase | Time | Core Teacher & Student Actions, Textbook Coverage & Research Grounding |
|---|---:|---|
| **ជំហានទី ១** (`រដ្ឋបាលថ្នាក់`) | `2 min` (`00–02`) | Check attendance, form 3-member investigator teams, place `Page 1` lab sheet face-down and 1 thin folding strip (`A4/A5`) on each desk (`Yeo & Tzeng, 2019`). |
| **ជំហានទី ២ក** (`កែកិច្ចការផ្ទះ`) | `3 min` (`02–05`) | Rapid check of Lesson 1 Rational Numbers `Book p. 12 #10ក, #10ច` & `p. 11 #4គ`: highlight sign rule `(-) × (-) = (+)` vs `(-) × (-) × (-) = (-)` and fraction multiplication $\frac{a}{b}\times\frac{c}{d}=\frac{ac}{bd}$ (`Booth et al., 2014`; `Lee & Boyadzhiev, 2020`). |
| **ជំហានទី ២ខ** (`រំលឹកមេរៀនចាស់`) | `3 min` (`05–08`) | Contrast **repeated addition of identical terms** ($4+4+4 = 4 \times 3 = 12$; $x+x+x = 3x$) with **repeated multiplication of identical factors** using `Book p. 13 ឧទាហរណ៍` ($10\,000 = 10 \times 10 \times 10 \times 10$) (`Moru & Mathunya, 2022`). |
| **ជំហានទី ២គ — E1 Engage** | `3 min` (`08–11`) | **Preah Krasang Doubling Challenge**: *(1)* If you fold a sheet of paper in half **6 times**, do you get `12` layers ($2 \times 6$) or `64` layers? *(2)* Do `(-2)^6` and `-2^6` give the same number or opposite numbers? Poll hands & record predictions on left board **without revealing answers** (`De Bock et al., 2003`; `Ulusoy, 2019`). |
| **ជំហានទី ៣ក — E2 Explore** | `11 min` (`11–22`) | **Dual Hands-On POE Lab (`6 min + 5 min`)**:<br>• **Activity 1 (`6'`, POE 1 — Paper-Folding Doubling Table)**: Predict (`P`), fold paper 1 to 5 times (and deduce fold 6) recording layers: $1\to 2$, $2\to 2\times 2=4$, $3\to 8$, $4\to 16$, $5\to 32$, $6\to 64 \neq 12$ (`O`), and explain (`E`) why $2^6 = 64 \neq 2\times 6$ and $a+a=2a \neq a^2$ (`Siller et al., 2023`; `Castillo-Garsow, 2013`; `Moru & Mathunya, 2022`).<br>• **Activity 2 (`5'`, POE 2 — Lock-Box Sign & Fraction Investigation)**: Use `[tracing]` Lock-Boxes and sign-pairing arcs to test `[(-2)]^6 = +64` (3 `+` pairs) vs. `-(2^6) = -64` and `[(-3)]^3 = -27` (1 leftover `-`), plus `[(2/3)]^3 = 8/27` vs. `2^3/3 = 8/3` (`Ulusoy, 2019`; `Theba et al., 2024`; `Lee & Boyadzhiev, 2020`). |
| **ជំហានទី ៣ខ — E3 Explain** | `6 min` (`22–28`) | Synthesize `Book pp. 13–14`:<br>1. Formal terms **គោល (`a`)**, **និទស្សន្ត (`n`)**, **ស្វ័យគុណ (`a^n`)** (`10^4 = 10\,000`) + reading `ការេ`, `គូប`, `(4/3)^7` + **Fix Erratum #1 (`8^2 → 8^4` on p. 13)**.<br>2. Definition $\underbrace{a\times a\times\dots\times a}_{n\text{ កត្តា}} = a^n$ + **Fix Erratum #2 on p. 14 (`n ជាចំនួនគត់វិជ្ជមាន n ≥ 1`, convention $a^1=a$)** (`Sureda & Otero, 2019`).<br>3. `សម្គាល់` $(-1)^n = 1$ ($n$ even) / $-1$ ($n$ odd) locked inside `(-1)` + post **Hub-and-Spoke B&W Warrant Bank `①–⑤`** & Operator Hierarchy Triangle (`Xu et al., 2026`; `Ali Rahman et al., 2017`). |
| **ជំហានទី ៤ក — E4 Elaborate** | `10 min` (`28–38`) | **3-Step Detective Card + `[tracing]`** on `Book p. 14`:<br>• **`លំហាត់គំរូទី 1`**: `ក. 4^6` (គោល $4$, និទស្សន្ត $6$); `ខ. a^{2010}` (គោល $a$, និទស្សន្ត $2010$ — warn against substituting random numbers for $a$, `Moru & Mathunya, 2022`).<br>• **`លំហាត់គំរូទី 2` (Fix Erratum #3)**: `ក. 2^5 = 32`; `ខ. (2/3)^3 = 8/27` (`⑤`); `គ. (-3)^3 = -27` (`③, ④`); `ឃ. (-2)^6 = 64` (clean 6-factor brace + 3 pairing arcs) **paired directly against `-2^6 = -(2^6) = -64` & `(-3^2) = -9`** (`Booth et al., 2013`; `Bye et al., 2024`).<br>• **EIA Looking-Back (30s)**: *"Why do `(-3)^3` and `-3^3` both equal `-27`, whereas `(-2)^6 = +64` and `-2^6 = -64` have opposite signs?"* |
| **ជំហានទី ៤ខ — E5 Evaluate** | `10 min` (`38–48`) | • **3-Role Team Relay (`6.5'`) on `Book p. 14 ប្រតិបត្តិ 1 & 2`**: Role 1 (`Pause-Ask` & Lock-Box `[tracing]`: bridge dot `·` in `1ក x^6`, `1ខ y^{2013}`); Role 2 (Expand & pair signs on `2ក 3^4 = 81`, `2ខ (-1/2)^6 = 1/64`, `2គ (-2)^7 = -128` citing `①–⑤`); Role 3 (`Pause-Review!` & **Close E1 Mission**: 6 folds $= 2^6 = 64$ layers; `(-2)^6 = +64 \neq -2^6 = -64`).<br>• **Diagnostic Foils `A–D` & 60–90s Exit Ticket (`3.5'`)**: Card A (`(-1/2)^6 = 1/64` ✓), Card B (`2^5 = 10` ✗ violates `②`), Card C (`-2^6 = +64` ✗ violates `③`), Card D (`(2/3)^3 = 8/3` ✗ violates `⑤`) + 3-item Exit Ticket (`Booth et al., 2013`). |
| **ជំហានទី ៥** (`កិច្ចការផ្ទះ`) | `≤2 min` (`48–50`) | Assign `Book p. 25`: **`#1(ក–ឃ)`, `#3(ក, ខ, ឃ)`** *(explicit **Alert #4** warning: in `#3ក`, `(-3^2) = -(3^2) = -9`!)*, and **`#4`** ($b=3 \implies L=3^3+1=28, W=3^2-1=8, P=72$); preview `២.២ វិធីគុណស្វ័យគុណ` (`pp. 15–16`). |

---

## 5. Monochrome B&W Hub-and-Spoke Warrant Bank (`①–⑤`) & Planned Printables Architecture

### 5.1 B&W Warrant Bank (`①–⑤`)
- **`①` និយមន័យស្វ័យគុណ ($n \in \mathbb{Z}^+$)**: $\underbrace{a \times a \times \dots \times a}_{n\text{ កត្តា}} = a^n$ ($a$ ជាគោល, $n$ ជានិទស្សន្តគត់វិជ្ជមាន, និងសន្មត $a^1 = a$ មាន $1$ កត្តា)។
- **`②` របាំងប្រឆាំងអន្ទាក់គុណ និងបូក**: $a^n \neq a \times n$ និង $\underbrace{a + a + \dots + a}_{n\text{ តួ}} = n \cdot a \neq a^n$ (ហាមយកគោលគុណនិទស្សន្ត ឬបូកតួដូចគ្នាដាក់ស្វ័យគុណ)។
- **`③` ប្រអប់ចាក់សោគោលអវិជ្ជមាន**: $(-a)^n = \underbrace{(-a)\times\dots\times(-a)}_{n\text{ កត្តា}}$ (សញ្ញាដកជាប់ក្នុងគោល) $\neq -a^n = -(a\times\dots\times a)$ (សញ្ញាដកនៅក្រៅស្វ័យគុណ រួមទាំងទម្រង់ `(-a^n)` លើទំ.២៥)។
- **`④` ច្បាប់ផ្គូផ្គងគូ-សេសលើគោលអវិជ្ជមានក្នុងវង់ក្រចក**: ចំពោះ $a > 0$, $(-a)^n > 0$ បើ $n$ គូ (ផ្គូផ្គងដកគ្រប់គូបាន `+`) និង $(-a)^n < 0$ បើ $n$ សេស (សល់កត្តាដក ១); ពិសេស $(-1)^n = 1$ ($n$ គូ) និង $(-1)^n = -1$ ($n$ សេស)។
- **`⑤` ប្រអប់ចាក់សោប្រភាគ និងអាទិភាពប្រមាណវិធី**: $\left(\frac{a}{b}\right)^n = \frac{a}{b}\times\dots\times\frac{a}{b} = \frac{a^n}{b^n} \neq \frac{a^n}{b}$ ($b \neq 0$); ក្នុងកន្សោមចម្រុះ គណនា **វង់ក្រចក $\to$ ស្វ័យគុណ $\to$ គុណ/ចែក $\to$ បូក/ដក**។

### 5.2 Planned 6-Page B&W `Printable_Materials_EXP1.pdf` Suite (For Subsequent Lesson-Plan Phase)
1. **Page 1 (`1:1 Actual Size 100%` + `5.00 cm` Calibration Bar)**: Folding-Strip Template (`16.00 cm × 3.00 cm` marked with fold lines `F1–F4`) + `POE 1` Layer-Doubling Table ($n=1..6$) + `POE 2` Lock-Box & Sign-Pairing Lab (`(-2)^6` vs `-2^6`, `(-3)^3`, `(2/3)^3` vs `2^3/3`).
2. **Page 2 (`2-up` E4 Worked-Example Detective Cards)**: 3-Step Lock-Box + `[tracing]` scaffold for `លំហាត់គំរូទី 1 (4^6, a^{2010})` & `លំហាត់គំរូទី 2 (2^5, (2/3)^3, (-3)^3, (-2)^6 vs -2^6)` + `EIA Looking-Back 30s`.
3. **Page 3 (`2-up` E5 3-Role Team Relay Sheets)**: `ប្រតិបត្តិ 1 (x^6, y^{2013})` & `ប្រតិបត្តិ 2 (3^4, (-1/2)^6, (-2)^7)` with `Pause-Ask`, `Pause-Review!`, and `E1` Mission Closure.
4. **Page 4 (`1-up` A4 Classroom Anchor Poster)**: Hub-and-Spoke Warrant Bank `①–⑤`, Errata #1–#2 Fixes, Lock-Box Visual Contrast, and Operator Hierarchy Triangle.
5. **Page 5 (`E5` Diagnostic Cards `A–D` + `2-up` 60–90s Exit Tickets)**: 4-Foil check (`A` ✓ `(-1/2)^6=1/64`, `B` ✗ `2^5=10`, `C` ✗ `-2^6=+64`, `D` ✗ `(2/3)^3=8/3`) + 3-question individual Exit Ticket (`(-3)^4` vs `-3^4`, `(-2/5)^3`, `2^4 + 1` vs `2 \times 4 + 1`).
6. **Page 6 (`4-up` Curated Homework Slips — `Book p. 25`)**: `#1(ក–ឃ)`, `#3(ក, ខ, ឃ)` with `Alert #4` box explaining `(-3^2) = -(3^2) = -9`, and `#4` ($b=3$, rectangle perimeter $P = 2[(b^3+1)+(b^2-1)] = 72$).
