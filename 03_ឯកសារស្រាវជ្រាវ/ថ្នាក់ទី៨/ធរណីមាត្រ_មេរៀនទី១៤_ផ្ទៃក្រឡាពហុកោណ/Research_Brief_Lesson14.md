# Research Brief & 4-Hour Curriculum Roadmap: Grade 8 Lesson 14 (`មេរៀនទី១៤ ៖ ផ្ទៃក្រឡាពហុកោណ`)

- **School Context**: `អនុវិទ្យាល័យព្រះក្រសាំង` (Preah Krasang Lower Secondary School, Kampong Svay, Kampong Thom) — **No-LCD / No-Projector Classroom**, **B&W Student Guided-Inquiry Worksheet (`សន្លឹកកិច្ចការសិស្ស`)** as primary instructional medium (unit grids & pre-drawn geometric decompositions on paper — zero scissor craft prep).
- **Textbook Scope**: MoEYS Grade 8 Mathematics (`សៀវភៅសិក្សាគោល គណិតវិទ្យា ថ្នាក់ទី៨`), Lesson 14 (`ផ្ទៃក្រឡាពហុកោណ`), Book pp. 187–196 (PDF pp. 192–201), covering 100% of theory, worked examples (`លំហាត់គំរូ`), guided practice (`ប្រតិបត្តិ`), and end-of-lesson exercises (`លំហាត់` #1–#10).
- **Deliverables per 50-Minute Hour**:
  1. `LS_Plan_<Code>.tex` / `.pdf` (50-min 5Es Lesson Plan with MoEYS 3-domain objectives & `>=90%` page fill)
  2. `Worksheet_<Code>.tex` / `.pdf` (2-page A4 B&W Guided-Inquiry Student Worksheet packed `>=90%`, placed alongside `LS_Plan` and mirrored in `02_មេរៀន/.../សន្លឹកកិច្ចការ/`).

---

## 1. Worldwide Evidence-Based Pedagogical Methods Selected for Each Sub-Lesson (No-LCD, Worksheet-Based)

1. **Hour 1 (`១. ផ្ទៃក្រឡាប្រលេឡូក្រាម` — `AREA1`)**:
   - **Selected Method**: **Unit-Grid Equidecomposability (Cut-Free Visual Translation) & Perpendicular Base-Height Locking** (*ការបំប្លែងរក្សាផ្ទៃលើក្រឡាឯកតា និងការចាក់សោគូបាត-កម្ពស់កែង*).
   - **Empirical Basis**: Kamii & Kysh (2006), Zacharos (2006), and Cavanagh (2008) document that the most persistent secondary misconception worldwide is multiplying base $\times$ slant side ($b \times a$) instead of perpendicular height ($b \times h$), or failing to match an external/second altitude to its corresponding base ($b_1 h_1 = b_2 h_2$). Counting & shading translated right triangles on a printed square grid, paired with a **POE Slant-Frame Collapse Trap** (same sides $8\text{ cm}, 5\text{ cm}$ tilted to different heights) and circling the $90^\circ$ box (`[tracing]`), eliminates the slant-side error.
2. **Hour 2 (`២. ផ្ទៃក្រឡាចតុកោណស្មើ` — `AREA2`)**:
   - **Selected Method**: **Dual-Representation Proof (Circumscribed Bounding-Rectangle Grid vs. Diagonal-Triangle Algebraic Split)** (*វិធីគួបផ្សំប្រអប់ចតុកោណកែងព័ទ្ធជុំវិញ និងការបំបែកត្រីកោណតាមអង្កត់ទ្រូង*).
   - **Empirical Basis**: Gravemeijer (1999, Realistic Mathematics Education) and Duval (2006) show that enclosing a rhombus of diagonals $d, d'$ inside a $d \times d'$ grid rectangle makes the factor $\frac{1}{2}$ visually unforgettable (preventing the $S = d \cdot d'$ omission error), while connecting directly to MoEYS's algebraic proof $S = \frac{1}{2} BD(AO + OC) = \frac{1}{2} d \cdot d'$ and inverse missing-diagonal equations.
3. **Hour 3 (`៣. ផ្ទៃក្រឡាចតុកោណព្នាយ` — `AREA3`)**:
   - **Selected Method**: **Multi-Strategy *Neriage* Comparison on Grid Worksheets (Diagonal-Triangle Split vs. Doubled-Trapezoid Parallelogram)** (*ការប្រៀបធៀបយុទ្ធសាស្ត្រច្រើនផ្លូវបែបជប៉ុន Neriage លើសន្លឹកក្រឡា*).
   - **Empirical Basis**: Manizade & Mason (2014, *Mathematics Teacher*, ERIC `EJ1044118`) classify student derivations of trapezoid area into *Type 1 Decomposing* ($\triangle ADC + \triangle ABC = \frac{1}{2}bh + \frac{1}{2}b'h$, matching p. 192 of the MoEYS textbook) and *Type 2 Composing/Transformational* (doubling into a parallelogram of base $b+b'$, or using midsegment $m = \frac{1}{2}(b+b')$ from Lesson 13.2.5!). Comparing both on the worksheet deepens algebraic equivalence and guards against external-height errors in obtuse trapezoids.
4. **Hour 4 (`៤. លំហាត់សំយោគផ្ទៃក្រឡាពហុកោណបណ្ដុំ និងចំណោទអនុវត្តន៍` — `AREA4`)**:
   - **Selected Method**: **Additive Decomposition vs. Subtractive Enclosing ("Cut-Apart vs. Surround-and-Subtract") Decision Protocol** (*ពិធីការសម្រេចចិត្តបំបែកបូក ទល់នឹងព័ទ្ធដកផ្ទៃទំនេរ*).
   - **Empirical Basis**: Duval (2006) and Rittle-Johnson & Star (2007) demonstrate that strategic flexibility on compound polygons (MoEYS Ex. `#5, #6, #7` pp. 194–196) requires explicitly contrasting when **Additive Splitting** is faster vs. when **Bounding-Rectangle Subtraction** (e.g., Ex. `#5` shaded quadrilateral inside $17 \times 25$ rectangle, or Ex. `#6` corner-cut octagon) saves steps and avoids missing dimensions.

---

## 2. 4-Hour Partition & Continuity Map (`ធរណីមាត្រ_មេរៀនទី១៤_ផ្ទៃក្រឡាពហុកោណ`)

| Hour | Folder & Code | Date (Lunar / Solar) | Book Pages & Errata Noted | Model Ex., Practice & Homework |
| :---: | :--- | :--- | :--- | :--- |
| **8 (14.1)** | `១_ផ្ទៃក្រឡាប្រលេឡូក្រាម` (`AREA1`) | `១០កើត ខែមិគសិរ ២៥៧០`<br>`១៩ ធ្នូ ២០២៦` (Sat) | pp. 187–190, pp. 194, 196 (fixes p. 189 `គំរូ 1ខ` typo `AGF=3.15` $\to$ `AGE=3.15`) | Grid translation, $S=bh$, triangle $S=\frac{1}{2}bh$; **E4**: `លំហាត់គំរូទី 1` ($10x=7\times 9 \Rightarrow x=6.3$, $S_{\triangle AFG}=3.15$) & `គំរូទី 2` ($210\text{ cm}^2$); **E5**: `ប្រតិបត្តិ` ($S=48\text{ cm}^2, x=\frac{16}{3}\text{ cm}$, p. 190); **HW**: Ex. `#1`, `#2ក` (p. 194), `#8`, `#9` (p. 196). |
| **9 (14.2)** | `២_ផ្ទៃក្រឡាចតុកោណស្មើ` (`AREA2`) | `១២កើត ខែមិគសិរ ២៥៧០`<br>`២១ ធ្នូ ២០២៦` (Mon) | pp. 190–191, pp. 194–195 (notes p. 190 `d"` typo & p. 191 `ប្រតិបត្តិ` $120\text{ cm}^2$ vs $240\text{ cm}^2$ / $d=8\text{ cm}$ nuance) | $S=\frac{1}{2}d\times d'$ proof + bounding box; **E4**: `លំហាត់គំរូទី 1` ($91\text{ cm}^2$) & `គំរូទី 2` ($d'=200\text{ mm}$); **E5**: `ប្រតិបត្តិ` p. 191 ($d=8\text{ cm}$ + $240\text{ cm}^2 \Rightarrow \text{side } 17\text{ cm}$ note) & Ex. `#4` p. 194; **HW**: Ex. `#5` (p. 194) & selected rhombus/kite items of `#7` (p. 195). |
| **10 (14.3)** | `៣_ផ្ទៃក្រឡាចតុកោណព្នាយ` (`AREA3`) | `១៣កើត ខែមិគសិរ ២៥៧០`<br>`២២ ធ្នូ ២០២៦` (Tue) | pp. 191–194, p. 196 (fixes p. 192 `គំរូ 1` diagram `cm` $\to$ `m`, p. 193 Fig. 1 duplicate `B` $\to$ `D`, and p. 194 `#3` header `កម្ពស់ (cm^2)` $\to$ `កម្ពស់ (cm)`) | $S=\frac{1}{2}(b+b')\times h$; **E4**: `លំហាត់គំរូទី 1` (farm plots $16\,560$ vs $14\,690\text{ m}^2$) & `គំរូទី 2` ($132\text{ m}^2$); **E5**: `ប្រតិបត្តិ ក, ខ` ($x=14\text{ cm}$; composite $S=1875, P=193$, p. 193); **HW**: Ex. `#2ខ`, `#3` (p. 194), `#10` (p. 196). |
| **11 (14.4)** | `៤_លំហាត់សំយោគផ្ទៃក្រឡាពហុកោណបណ្ដុំ` (`AREA4`) | `១៤កើត ខែមិគសិរ ២៥៧០`<br>`២៣ ធ្នូ ២០២៦` (Wed) | pp. 194–196 (synthesis of compound shaded regions & mixed polygons `#6–#7`) | Additive vs. Subtractive Composite Area Workshop: **E2/E3**: `#6` (top-left & corner-cut octagon/hexagon); **E4**: `#6` L-frame with cutout; **E5**: `#6` shaded chevron & `#7` composite house/trapezoid; **HW**: Remaining items of `#6` & `#7` (pp. 195–196) + preview Lesson 15 Pythagoras. |

---

## 3. Core APA 7th References
- Cavanagh, M. (2008). Area measurement in Year 7: Linear and perpendicular misconceptions. *Australian Mathematics Teacher*, 64(1), 25–30.
- Duval, R. (2006). A cognitive analysis of problems of comprehension in a learning of mathematics. *Educational Studies in Mathematics*, 61(1–2), 103–131. https://doi.org/10.1007/s10649-006-0400-z
- Gravemeijer, K. (1999). How emergent models may foster the constitution of formal mathematics. *Mathematical Thinking and Learning*, 1(2), 155–177.
- Kamii, C., & Kysh, J. (2006). The difficulty of "length $\times$ width": Is a square the unit of measurement? *Journal for Research in Mathematics Education*, 37(2), 105–129.
- Manizade, A. G., & Mason, M. M. (2014). Developing the area of a trapezoid. *Mathematics Teacher*, 107(7), 508–514. (ERIC No. EJ1044118)
- Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? *Journal of Educational Psychology*, 99(3), 561–574.
- Zacharos, K. (2006). Prevailing educational practices for area measurement and students' failure in measuring areas. *The Journal of Mathematical Behavior*, 25(3), 224–239. https://doi.org/10.1016/j.jmathb.2006.09.003
