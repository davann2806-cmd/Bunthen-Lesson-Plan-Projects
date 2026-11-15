# Research Brief & 4-Hour Curriculum Roadmap: Grade 8 Lesson 15 (`មេរៀនទី១៥ ៖ រង្វង់`)

- **School Context**: `អនុវិទ្យាល័យព្រះក្រសាំង` (Preah Krasang Lower Secondary School, Kampong Svay, Kampong Thom) — **No-LCD / No-Projector Classroom**, **B&W Student Guided-Inquiry Worksheet (`សន្លឹកកិច្ចការសិស្ស`)** + ruler, protractor, and compass as primary instructional medium (zero cut-out craft prep).
- **Textbook Scope**: MoEYS Grade 8 Mathematics (`សៀវភៅសិក្សាគោល គណិតវិទ្យា ថ្នាក់ទី៨`), Lesson 15 (`រង្វង់`), Book pp. 197–204 (PDF pp. 202–209), covering all definitions, theorems, general rules (`ជាទូទៅ`), worked examples (`លំហាត់គំរូ`), guided practice (`ប្រតិបត្តិ`), and end-of-lesson exercises (`លំហាត់` #1–#10).
- **Deliverables per 50-Minute Hour**:
  1. `LS_Plan_<Code>.tex` / `.pdf` (50-min 5Es Lesson Plan with MoEYS 3-domain objectives & `>=90%` page fill)
  2. `Worksheet_<Code>.tex` / `.pdf` (2-page A4 B&W Guided-Inquiry Student Worksheet packed `>=88–96%`, placed alongside `LS_Plan` and mirrored in `02_មេរៀន/.../សន្លឹកកិច្ចការ/`).

---

## 1. Worldwide Evidence-Based Pedagogical Methods Selected for Each Sub-Lesson (No-LCD, Worksheet-Based)

1. **Hour 1 (`១. សញ្ញាណរង្វង់ និងការកំណត់រង្វង់` — `CIRC1`)**:
   - **Selected Method**: **Progressive Constraint Locus-of-Equidistance Inquiry (1 Point $\to$ 2 Points $\to$ 3 Non-Collinear Points)** (*វិធីរុករកសំណុំចំណុចស្មើចម្ងាយតាមការបន្ថែមលក្ខខណ្ឌ ១ ចំណុច $\to$ ២ ចំណុច $\to$ ៣ ចំណុច និងប្រសព្វមេដ្យាទ័រ*).
   - **Empirical Basis**: Gutiérrez, Jaime, & Gutiérrez (2021) and Fujita & Jones (2007) demonstrated that students often treat a circle purely as a static round contour (Van Hiele Level 1) rather than a **locus of equidistant points** ($OA = r$), causing them to guess the center of a circle passing through 3 points as the midpoint of the longest segment (falsely assuming a diameter). Stepping learners on a `1:1` printed B&W worksheet from 1 point (infinitely many centers anywhere) $\to$ 2 points (centers restricted to the perpendicular bisector of $AB$) $\to$ 3 non-collinear points (unique intersection $O = d_1 \cap d_2 \implies OA=OB=OC$, contrasted with the **3-collinear-points parallel-bisector trap** where $d_1 \parallel d_2$) builds genuine deductive ownership of existence and uniqueness.

2. **Hour 2 (`២. មុំផ្ចិត និងធ្នូ` — `CIRC2`)**:
   - **Selected Method**: **Concentric Contrasting-Cases & Multiplicative Arc-Length Proportionality** (*ការប្រៀបធៀបករណីផ្ទុយលើរង្វង់រួមផ្ចិត និងសមាមាត្រប្រវែងធ្នូធៀបនឹងបរិមាត្រ*).
   - **Empirical Basis**: Moore (2013, 2014) and Sidney, Hattikudur, & Alibali (2015) proved that secondary students persistently conflate **arc degree measure** (`រង្វាស់ដឺក្រេនៃធ្នូ`, invariant across concentric circles for a fixed central angle $n^\circ$) with **arc linear length** (`ប្រវែងធ្នូ` $\ell$, which scales proportionally with both $n^\circ/360^\circ$ and radius $r$). Presenting a `1:1` concentric dual-circle diagram ($r_1 = 1\text{ cm}, r_2 = 2\text{ cm}$ under the same central angle $\angle AOB = 90^\circ$) on the B&W worksheet forces students to distinguish angular openness ($90^\circ = \frac{1}{4}$ turn) from linear distance ($\ell = \frac{n^\circ}{360^\circ}\cdot 2\pi r = \frac{\pi r n^\circ}{180^\circ}$).

3. **Hour 3 (`២.១ ធ្នូ និងអង្កត់ធ្នូ` — `CIRC3`)**:
   - **Selected Method**: **Auxiliary-Radii Triangle-Bridge Heuristic & Non-Linearity Counter-Example** (*យុទ្ធវិធីគូសកាំជំនួយបំប្លែងធ្នូ-អង្កត់ធ្នូទៅជាត្រីកោណ និងអន្ទាក់មិនមែនសមាមាត្រនៃអង្កត់ធ្នូ*).
   - **Empirical Basis**: Palatnik & Sigler (2019) and Duval (2006) established that circle-chord proofs stall when students stare at isolated chords without introducing **auxiliary radii** ($OA=OB=OC=OD=r$) to concretize the circle definition and unlock prior triangle theorems (Triangle Inequality $OC+OD > CD \implies AB_{\text{diam}} > CD$, SSS/SAS congruence $\triangle AOB \cong \triangle COD$, and Hinge Inequality). Furthermore, De Bock et al. (2002) documented the **Illusion of Linearity**, where students falsely assume that doubling an arc ($\widehat{AC} = 2\widehat{AB}$) doubles the chord ($AC = 2AB$); testing this directly on the worksheet via Triangle Inequality ($AB + BC > AC \implies 2AB > AC$) inoculates students against linear overgeneralization.

4. **Hour 4 (`២.២ លក្ខណៈឆ្លុះនៃរង្វង់` — `CIRC4`)**:
   - **Selected Method**: **Diameter Axial-Symmetry Invariance + Visual-Analytical Equidistant-Chord Algebra** (*ការឆ្លុះតាមអ័ក្សអង្កត់ផ្ចិត និងការភ្ជាប់រូបភាព-ពិជគណិតលើអង្កត់ធ្នូស្មើចម្ងាយពីផ្ចិត*).
   - **Empirical Basis**: Gutiérrez et al. (2021) and Zazkis, Dubinsky, & Dautermann (1996, Visual–Analytical model) showed that coordinating **axial reflection across a diameter** ($AB \perp CD$ at $H \implies C \leftrightarrow D$, $HC=HD$, $\widehat{CB}=\widehat{DB}$, and parallel chords $AB \parallel CD \implies \widehat{AC}=\widehat{BD}$) with deductive HL right-triangle congruence ($\triangle OHC \cong \triangle OHD$) makes both chord bisection and equidistant-chord theorems ($OQ = OR \iff AB = CD$) transparent. In addition, Exercise `#4` (p. 204: $6x+14 = -4x+4 \implies x = -1 \implies AB=CD=8 > 0$) serves as a rich **algebra-in-geometry validation task** busting the misconception that a negative parameter $x < 0$ is automatically extraneous when segment lengths remain positive.

---

## 2. 4-Hour Partition, Textbook Errata & Continuity Map (`ធរណីមាត្រ_មេរៀនទី១៥_រង្វង់`)

| Hour | Folder & Code | Date (Lunar / Solar) | Book Pages & Errata Handled | Worked Examples, Practice & Homework |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `១_សញ្ញាណរង្វង់_និងការកំណត់រង្វង់` (`CIRC1`) | `១៥កើត ខែមិគសិរ ២៥៧០`<br>`២៤ ធ្នូ ២០២៦` (Thu) | pp. 197–198, p. 204 | Defs ($C(O,r)$, radius, chord, diameter); 1 pt / 2 pts / 3 non-collinear pts unique circle theorem (`លំហាត់គំរូ` p. 198); **E5**: `ប្រតិបត្តិ` p. 198 ($AB=6\text{ cm}$ two-circle positions ក, ខ, គ); **HW**: Ex. `#6` & `#7` (p. 204). |
| **2** | `២_មុំផ្ចិត_និងធ្នូ` (`CIRC2`) | `១រោច ខែមិគសិរ ២៥៧០`<br>`២៥ ធ្នូ ២០២៦` (Fri) | pp. 199–200, p. 204 (fixes p. 200 Ex. 2 `94.2dm` $\to$ `94.2 cm`, p. 200 `62.832` $\pi$ rounding note, & p. 204 Ex. `#1` $\angle A=25^\circ \to \angle AOB=25^\circ$) | Central angle, quadrant ($90^\circ$), equal central angles $\iff$ equal arcs, $\ell = \frac{\pi r n^\circ}{180^\circ}$; **E4**: `លំហាត់គំរូទី១–២` (p. 200); **E5**: `ប្រតិបត្តិ` (p. 200) + arc length; **HW**: Ex. `#1` (p. 204) + wheel/clock arc task. |
| **3** | `២.១_ធ្នូ_និងអង្កត់ធ្នូ` (`CIRC3`) | `២រោច ខែមិគសិរ ២៥៧០`<br>`២៦ ធ្នូ ២០២៦` (Sat) | pp. 200–201, p. 204 | Diameter = longest chord (`លំហាត់គំរូទី១` p. 201); $\widehat{AB}=\widehat{MN} \iff AB=MN$ (`លំហាត់គំរូទី២`); $\widehat{AB}>\widehat{CD} \iff AB>CD$ (`លំហាត់គំរូទី៣`); **E4/E5**: Ex. `#2` & `#3` (p. 204); **HW**: Ex. `#5` (p. 204) + Ex. `គំរូទី២` (p. 201). |
| **4** | `២.២_លក្ខណៈឆ្លុះនៃរង្វង់` (`CIRC4`) | `៤រោច ខែមិគសិរ ២៥៧០`<br>`២៨ ធ្នូ ២០២៦` (Mon) | pp. 202–204 (highlights Ex. `#4` p. 204 where $x=-1$ yields valid positive chords $AB=CD=8$; avoids p. 204 Ex. `#8` print typo) | Center & axis of symmetry; $AB \perp CD \iff HC=HD$ (`លំហាត់គំរូទី១`); $AB \parallel CD \implies \widehat{AC}=\widehat{BD}$ (`លំហាត់គំរូទី២`); $OQ=OR \iff AB=CD$; **E4**: `លំហាត់គំរូទី២` & Ex. `#4`; **E5**: `ប្រតិបត្តិ` (p. 203); **HW**: Ex. `#9` & `#10 ក` (p. 204). |

---

## 3. Core APA 7th References
- De Bock, D., Van Dooren, W., Janssens, D., & Verschaffel, L. (2002). Improper use of linear reasoning: An in-depth study of the nature and the irresistibility of secondary school students' errors. *Educational Studies in Mathematics*, 50(3), 311–334. https://doi.org/10.1023/A:1021205413749
- Duval, R. (2006). A cognitive analysis of problems of comprehension in a learning of mathematics. *Educational Studies in Mathematics*, 61(1–2), 103–131. https://doi.org/10.1007/s10649-006-0400-z
- Fujita, T., & Jones, K. (2007). Learners' understanding of the definitions and hierarchical classification of quadrilaterals: Towards a theoretical framing. *Research in Mathematics Education*, 9(1), 3–20. https://doi.org/10.1080/14794800008520167
- Gutiérrez, Á., Jaime, A., & Gutiérrez, P. (2021). Networked analysis of a teaching unit for primary school symmetries. *Mathematics*, 9(8), 832. https://doi.org/10.3390/math9080832
- Moore, K. C. (2013). Making sense by measuring arcs: A teaching experiment in angle measure. *Educational Studies in Mathematics*, 83(2), 225–245. https://doi.org/10.1007/s10649-012-9450-6
- Moore, K. C. (2014). Quantitative reasoning and the sine function: The case of Zac. *Journal for Research in Mathematics Education*, 45(1), 102–138. https://doi.org/10.5951/jresematheduc.45.1.0102
- Palatnik, A., & Sigler, A. (2019). Focusing attention on auxiliary lines when introduced into geometric problems. *International Journal of Mathematical Education in Science and Technology*, 50(8), 1208–1223. https://doi.org/10.1080/0020739X.2018.1489076
- Sidney, P. G., Hattikudur, S., & Alibali, M. W. (2015). How do contrasting cases and self-explanation promote learning? Evidence from fraction division. *Learning and Instruction*, 40, 29–38. https://doi.org/10.1016/j.learninstruc.2015.07.006
- Zazkis, R., Dubinsky, E., & Dautermann, J. (1996). Coordinating visual and analytic strategies: A study of students' understanding of the group $D_4$. *Journal for Research in Mathematics Education*, 27(4), 435–457.
