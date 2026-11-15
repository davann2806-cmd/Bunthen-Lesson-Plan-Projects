# Research Brief & 7-Hour Curriculum Roadmap: Grade 8 Lesson 13 (`មេរៀនទី១៣ ៖ ចតុកោណ`)

- **School Context**: `អនុវិទ្យាល័យព្រះក្រសាំង` (Preah Krasang Lower Secondary School, Kampong Svay, Kampong Thom) — **No-LCD / No-Projector Classroom**, **B&W Student Guided-Inquiry Worksheet (`សន្លឹកកិច្ចការសិស្ស`)** as primary instructional medium (zero cut-out craft prep).
- **Textbook Scope**: MoEYS Grade 8 Mathematics (`សៀវភៅសិក្សាគោល គណិតវិទ្យា ថ្នាក់ទី៨`), Lesson 13 (`ចតុកោណ`), Book pp. 169–186 (PDF pp. 174–191), including all theorems, worked examples (`លំហាត់គំរូ`), guided practice (`ប្រតិបត្តិ`), and end-of-lesson exercises (`លំហាត់` #1–#14).
- **Deliverables per 50-Minute Hour**:
  1. `LS_Plan_<Code>.tex` / `.pdf` (50-min 5Es Lesson Plan with MoEYS 3-domain objectives & `>=90%` page fill)
  2. `Worksheet_<Code>.tex` / `.pdf` (2-page A4 B&W Guided-Inquiry Student Worksheet packed `>=90%`, placed alongside `LS_Plan` and mirrored in `02_មេរៀន/.../សន្លឹកកិច្ចការ/`).

---

## 1. Worldwide Evidence-Based Pedagogical Methods Selected for Each Sub-Lesson (No-LCD, Worksheet-Based)

1. **Hour 1 (`១. ប្រភេទនៃចតុកោណ` — `QUAD1`)**:
   - **Selected Method**: **Van Hiele Level 2 $\to$ 3 Diagnostic Property-Matrix & Inclusive Hierarchy Mapping** (*តារាងវិភាគលក្ខណៈ Van Hiele និងមែកធាងឋានានុក្រមរួមបញ្ចូល*).
   - **Empirical Basis**: De Villiers (1994) and Fujita (2012) demonstrated that secondary students worldwide suffer from the **Prototype Phenomenon** (e.g., rejecting a $45^\circ$-tilted square as a rectangle, or using exclusive definitions where squares are excluded from rectangles/rhombuses). Guiding students to measure parallel/equal/right-angle attributes directly on rotated B&W worksheet figures before filling an Inclusive Property Matrix reliably bridges Van Hiele Level 2 (Analysis) to Level 3 (Informal Deduction).
2. **Hour 2 (`២.១.១ លក្ខណៈប្រលេឡូក្រាម៖ ទ្រឹស្ដីបទទី១–៣` — `PARA1`)**:
   - **Selected Method**: **Auxiliary Diagonal Decomposition + Faded Flow-to-Table Proof Scaffolding** (*ការបំបែកតាមអង្កត់ទ្រូងជំនួយ និងតារាងសម្រាយបញ្ជាក់បន្ថយជំនួយជាជំហាន*).
   - **Empirical Basis**: Miyazaki, Fujita, & Jones (2017) and Anwar et al. (2023) showed that Grade 8 learners struggle to connect *singular propositions* ($OA=OC$) with *universal warrants* (`ម-ជ-ម`). Pairing empirical measurement + a **POE Diagonal-Equality Trap** ($AC \neq BD$ in oblique parallelograms!) with a Faded Proof Table and Warrant Bank `①–⑤` builds structural proof fluency without slides.
3. **Hour 3 (`២.១.២ លក្ខណៈសម្គាល់ប្រលេឡូក្រាម៖ ទ្រឹស្ដីបទទី៤–៧` — `PARA2`)**:
   - **Selected Method**: **Lakatosian Counter-Example Refutation & Minimal-Sufficiency Triage** (*វិធីបដិសេធដោយឧទាហរណ៍ផ្ទុយ និងការផ្ទៀងផ្ទាត់លក្ខខណ្ឌគ្រប់គ្រាន់អប្បបរមា*).
   - **Empirical Basis**: Zaslavsky & Shir (2005) and Palatnik & Sigler (2018) found that students routinely conflate "1 pair parallel + the *other* pair congruent" with Theorem 6 ("*same* pair parallel AND congruent"). Printing a 1:1 **Isosceles Trapezoid Counter-Example** directly on the worksheet forces cognitive conflict and cements the exact sufficiency conditions of Theorems 4–7.
4. **Hour 4 (`២.២ លក្ខណៈចតុកោណកែង` — `RECT1`)**:
   - **Selected Method**: **Duval Overlapping-Triangle Dimensional Deconstruction (`[tracing]`) + Carpenter's Diagonal Check** (*ការបំបែកត្រីកោណត្រួតគ្នាតាម Duval និងបន្ទាត់ផ្ទៀងអង្កត់ទ្រូងជាងឈើ*).
   - **Empirical Basis**: Duval (2006) established that overlapping triangles ($\triangle ADC$ and $\triangle BDC$ sharing $DC$) create a major visual bottleneck in Grade 8 proof writing. Having students trace and separate the two right triangles side-by-side on the worksheet, plus testing why $AC=BD$ alone fails without the parallelogram condition (isosceles trapezoid trap), resolves visual entanglement.
5. **Hour 5 (`២.៣ លក្ខណៈចតុកោណស្មើ` — `RHOM1`)**:
   - **Selected Method**: **Contrastive Case Comparison (Rhombus vs. Kite & Rectangle) + Fold-Axis Symmetry Inquiry** (*ការប្រៀបធៀបករណីផ្ទុយ ចតុកោណស្មើ-ខ្លែង-ចតុកោណកែង និងអ័ក្សឆ្លុះអង្កត់ទ្រូង*).
   - **Empirical Basis**: Rittle-Johnson & Star (2007) and Fujita (2012) show side-by-side contrastive cases on paper worksheets sharply separate properties that students overgeneralize: (a) a kite has $AC \perp BD$ without bisecting both diagonals, and (b) a rectangle's diagonals do NOT bisect corner angles whereas a rhombus's diagonals DO.
6. **Hour 6 (`២.៤ លក្ខណៈការេ និងទ្រឹស្ដីបទចំណុចកណ្ដាល` — `SQMID1`)**:
   - **Selected Method**: **Polya Auxiliary Segment-Doubling ("180° Point-Reflection Completion") Heuristic** (*យុទ្ធវិធីបន្ថែមអង្កត់ទ្វេដងបង្គ្រប់ប្រលេឡូក្រាម និងចតុកោណកែង*).
   - **Empirical Basis**: Palatnik & Sigler (2018, 2021) and Polya (1945) identify auxiliary construction as the hardest creative leap in school geometry. Explicitly teaching the unified **"See $\frac{1}{2}$ $\to$ Double the Segment"** heuristic on worksheet diagrams unlocks both Triangle Midsegment ($DE \to DF$) and Right-Triangle Median ($BO \to BD$) proofs simultaneously.
7. **Hour 7 (`២.៥ លក្ខណៈចតុកោណព្នាយ` — `TRAP1`)**:
   - **Selected Method**: **Structured Problem Reduction via Dual Auxiliary Lines (Leg-Translation vs. Triangle-Completion)** (*វិធីបង្រួមបញ្ហាតាមបន្ទាត់ជំនួយពីរជម្រើស*).
   - **Empirical Basis**: Japanese Structured Problem Solving (*Neriage*, Stigler & Hiebert, 1999; Palatnik & Sigler, 2018) shows that comparing `គូស DE ∥ BC` (reducing trapezoid to parallelogram + isosceles triangle) with `បន្លាយ CE ជួប BA ត្រង់ G` (reducing trapezoid midsegment to triangle midsegment) builds deep deductive transfer.

---

## 2. 7-Hour Partition & Continuity Map (`ធរណីមាត្រ_មេរៀនទី១៣_ចតុកោណ`)

| Hour | Folder & Code | Date (Lunar / Solar) | Book Pages & Errata Noted | Model Ex., Practice & Homework |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `១_ប្រភេទនៃចតុកោណ` (`QUAD1`) | `២កើត ខែមិគសិរ ២៥៧០`<br>`១១ ធ្នូ ២០២៦` (Fri) | pp. 169–170 (fixes p. 169 `ចតុកោណកោណកែង` $\to$ `ចតុកោណកែង`) | Definitions + Hierarchy tree (`ទំនាក់ទំនងនៃប្រភេទចតុកោណ`); Worksheet classification & rotated-prototype tasks; **HW**: Classification & construction prep (`#6ក` p. 185 + hierarchy table). |
| **2** | `២.១.១_លក្ខណៈប្រលេឡូក្រាម_ទ្រឹស្ដីបទទី១ដល់ទី៣` (`PARA1`) | `៣កើត ខែមិគសិរ ២៥៧០`<br>`១២ ធ្នូ ២០២៦` (Sat) | pp. 170–171, p. 185 | Thm 1 ($\triangle ADC \cong \triangle ABC$, corollary opp. sides/angles), Thm 2 ($\angle A+\angle B=180^\circ$), Thm 3 (center $O$); **E4/E5**: Ex. `#2` & `#4` (p. 185); **HW**: Ex. `#5`, `#6ក`, `#7` (p. 185). |
| **3** | `២.១.២_លក្ខណៈសម្គាល់ប្រលេឡូក្រាម_ទ្រឹស្ដីបទទី៤ដល់ទី៧` (`PARA2`) | `៥កើត ខែមិគសិរ ២៥៧០`<br>`១៤ ធ្នូ ២០២៦` (Mon) | pp. 171–174, p. 185 (cleans p. 173 Thm 7 phrasing) | Thms 4–7 + Isosceles Trapezoid mixed-pair counterexample; **E4**: `លំហាត់គំរូ` ($ABEF, EFDC$, pp. 173–174); **E5**: `ប្រតិបត្តិ` ($ABDC$, p. 174); **HW**: Ex. `#3` (ក, ខ) & `#6ខ` (p. 185). |
| **4** | `២.២_លក្ខណៈចតុកោណកែង` (`RECT1`) | `៦កើត ខែមិគសិរ ២៥៧០`<br>`១៥ ធ្នូ ២០២៦` (Tue) | pp. 174–176, p. 186 (notes p. 174 wrong intro figure & p. 175 redundant `AD=BC`) | Thms 1–3 ($90^\circ$ angles, $AC=BD$, converse); **E4**: `លំហាត់គំរូ` ($BHQR$ & $MP+MQ=BH$, p. 176); **E5**: `ប្រតិបត្តិ` ($\angle CAD=\angle BDA$, p. 176); **HW**: Ex. `#9` (p. 186) + rectangle diagonal calculation. |
| **5** | `២.៣_លក្ខណៈចតុកោណស្មើ` (`RHOM1`) | `៧កើត ខែមិគសិរ ២៥៧០`<br>`១៦ ធ្នូ ២០២៦` (Wed) | pp. 176–179, pp. 185–186 | Thms 1–4 (4 equal sides, $AC\perp BD$, converse, angle bisectors); **E4**: `លំហាត់គំរូ` ($AOBI$ rhombus, pp. 178–179); **E5**: `ប្រតិបត្តិ` ($\angle DAB, \angle BDC = 60^\circ$, p. 179); **HW**: Ex. `#1` (p. 185), `#12`, `#13`, `#14` (p. 186). |
| **6** | `២.៤_លក្ខណៈការេ_និងទ្រឹស្ដីបទចំណុចកណ្ដាល` (`SQMID1`) | `៨កើត ខែមិគសិរ ២៥៧០`<br>`១៧ ធ្នូ ២០២៦` (Thu) | pp. 179–181, p. 186 | Square's 7 properties; Midsegment Thms 1–2 ($DE \parallel BC, DE=\frac{1}{2}BC$); Right-$\triangle$ Median Thms 3–4 ($BO=\frac{1}{2}AC$); **E4/E5**: Algebraic midsegment & right-median tasks; **HW**: Ex. `#8` (p. 186) + right-triangle median & square diagonal tasks. |
| **7** | `២.៥_លក្ខណៈចតុកោណព្នាយ` (`TRAP1`) | `៩កើត ខែមិគសិរ ២៥៧០`<br>`១៨ ធ្នូ ២០២៦` (Fri) | pp. 181–184, p. 186 | Isosceles trapezoid Thms 1–2 ($\angle A=\angle B$, $AC=DB$); Trapezoid midsegment Thms 3–4 ($EF=\frac{1}{2}(AB+DC)$, collinearity $E,G,H,F$); **E4**: `លំហាត់គំរូ` ($O,H,G$ collinear, p. 184); **E5/HW**: Ex. `#10` (ក, ខ) & `#11` (p. 186). |

---

## 3. Core APA 7th References
- Anwar, L., Mali, M., & Goedhart, M. J. (2023). Learning trajectory of geometry proof construction: Studying the emerging understanding of the structure of proof. *Eurasia Journal of Mathematics, Science and Technology Education*, 19(4), em2246. https://doi.org/10.29333/ejmste/13160
- De Villiers, M. (1994). The role and function of a hierarchical classification of quadrilaterals. *For the Learning of Mathematics*, 14(1), 11–18.
- Duval, R. (2006). A cognitive analysis of problems of comprehension in a learning of mathematics. *Educational Studies in Mathematics*, 61(1–2), 103–131. https://doi.org/10.1007/s10649-006-0400-z
- Fujita, T. (2012). Learners' level of understanding of the inclusion relations of quadrilaterals and prototype phenomenon. *The Journal of Mathematical Behavior*, 31(1), 60–72. https://doi.org/10.1016/j.jmathb.2011.08.003
- Miyazaki, M., Fujita, T., & Jones, K. (2017). Students' understanding of the structure of deductive proof. *Educational Studies in Mathematics*, 94(2), 223–239. https://doi.org/10.1007/s10649-016-9720-9
- Palatnik, A., & Sigler, A. (2019). Focusing attention on auxiliary lines when introduced into geometric problems. *International Journal of Mathematical Education in Science and Technology*, 50(8), 1208–1223. https://doi.org/10.1080/0020739X.2018.1527407
- Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? *Journal of Educational Psychology*, 99(3), 561–574. https://doi.org/10.1037/0022-0663.99.3.561
- Zaslavsky, O., & Shir, K. (2005). Students' conceptions of a mathematical definition. *Journal for Research in Mathematics Education*, 36(4), 317–346.
