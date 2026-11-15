---
name: latex
description: >-
  Write, edit, debug, and compile Khmer and Mathematics LaTeX (XeLaTeX) textbooks,
  lessons, and exercise sets. Covers Khmer OS font configurations, tcolorbox
  environments (DIF, MaG, modelex, practex, thinkex, myexamp, solbox), tkz-tab
  variation/sign tables, pgfplots/TikZ function graphs, and fast vs. full compilation workflows.
---

# LaTeX (XeLaTeX) Skill for Khmer Mathematics Textbooks

Use this skill whenever writing, editing, formatting, or compiling `.tex` files in this project.

## 1. Engine & Compilation Workflow

This project uses **XeLaTeX** (`xelatex`) with UTF-8 encoding and SyncTeX enabled.

### Fast vs. Full Compilation (`functions.tex`)
In `functions.tex`, three boolean flags control compilation speed:
- `\onlyprelessonfalse` / `\onlyprelessontrue`: Compile only `lessons/01_pre_exercises.tex`.
- `\fulllessonfalse` / `\fulllessontrue`: When `false`, compiles only the active segment of `lessons/02_lesson.tex` for ~1s fast preview. When `true`, compiles the full lesson.
- `\fullbookfalse` / `\fullbooktrue`: When `true`, compiles the cover, preface, TOC, pre-exercises, full lesson, and all exercise files (`exercises/ex_01.tex` to `ex_15.tex`).

### Running Compilation
- **Fast compile (default):**
  ```powershell
  .\compile.bat
  ```
- **Full compile (Cover + 2 passes for TOC & bookmarks):**
  ```powershell
  .\compile.bat full
  ```

---

## 2. Fonts & Khmer Numbering Rules

- **Main Text Font:** `Khmer OS Battambang` (`\kv`)
- **Heading / Title Fonts:** `Khmer OS Muol Light` (`\KCT`, `\KML`), `Khmer OS Muol` (`\KM`), `Khmer OS Bokor` (`\kb`)
- **Math Font:** `STIX Two Math` and `STIX Two Text` (scaled by `\fscale`)
- **CRITICAL RULE FOR TIKZ / TKZ-TAB:**
  Never redefine `\@arabic` globally to Khmer numerals (`\@khmernum`), because `pgfmath` and `tkz-tab` rely on Arabic numerals internally for calculations. Only override display macros such as `\thepage`, `\thesection`, `\thesubsection`, etc.

### Enumerate Keys (`enumitem`)
- `\begin{enumerate}[k]` — Circled Khmer consonant labels (`ក`, `ខ`, `គ`, ...) in `primary` color.
- `\begin{enumerate}[1]`, `[a]`, `[A]`, `[i]`, `[I]` — Roman/Arabic labels using `Times New Roman` (`\en`).
- Add `2` to options (e.g., `\begin{enumerate}[k, 2]`) for a 2-column list (`multicols`).

---

## 3. Color Palette

All boxes, plots, and tables use the unified palette defined in `functions.tex`:
- `primary` (`#1F3A5F`): Deep navy for headings, frames, main curves, and labels.
- `textgray` (`#4A5160`): Secondary text.
- `rulegray` (`#BCC2CA`): Hairlines, grids, and dividers.
- `panel` (`#F3F4F6`): Light gray box background.
- `brick` (`#9C3B3B`): Muted red accent for asymptotes and key points.
- `slate` (`#6B7480`): Muted gray for secondary plot lines/tangents.

---

## 4. Custom `tcolorbox` Environments

### Concept & Theory Boxes
- **Definition Box (`DIF`):**
  ```latex
  \begin{DIF}
  % Definition content here
  \end{DIF}
  ```
- **General Rule / Summary Box (`MaG`):**
  ```latex
  \begin{MaG}
  % General formula or property here
  \end{MaG}
  ```
- **Titled Note Box (`mybox`):**
  ```latex
  \begin{mybox}{ចំណាំ}
  % Note content here
  \end{mybox}
  ```

### Exercise & Solution Boxes
All structured exercise boxes take `[tag]{topic}{instruction}` and support `\tcblower` to separate the problem statement from the solution (`ដំណោះស្រាយ`):
- **Worked Example (`modelex` - Style D):**
  ```latex
  \begin{modelex}[កម្រិតមូលដ្ឋាន]{ចំណងជើងប្រធានបទ}{សេចក្ដីណែនាំលំហាត់}
  % Problem statement
  \tcblower
  % Solution steps
  \end{modelex}
  ```
- **Practice Exercise (`practex` - Style B):**
  ```latex
  \begin{practex}[អនុវត្តន៍]{ប្រធានបទ}{សេចក្ដីណែនាំ}
  % Problem
  \tcblower
  % Solution
  \end{practex}
  ```
- **Critical Thinking Exercise (`thinkex` - Style C):**
  ```latex
  \begin{thinkex}[ត្រិះរិះ]{ប្រធានបទ}{សេចក្ដីណែនាំ}
  % Problem
  \tcblower
  % Solution
  \end{thinkex}
  ```
- **Generic Exercise (`myexamp`):** Same arguments `[tag]{topic}{instruction}`, used across `exercises/ex_*.tex`.
- **Standalone Solution Box (`solbox` or `mym`):** Used when the solution is placed in a separate box from the problem.

---

## 5. Variation Tables (`tkz-tab`) & Graphs (`pgfplots` / `TikZ`)

- **Variation & Sign Tables (`tkz-tab`):**
  - Pre-configured with `primary` navy lines and `panel`/`rulegray` backgrounds.
  - Ensure `tkzTabInit` column widths (`lgt`, `espcl`) fit within the A5 page width (`twoside` geometry).
- **Function Graphs (`pgfplots` / `TikZ`):**
  - Use `primary` (or `teal`) for main function curves $C_f$.
  - Use `brick` (or `red`/`blue`, which map to `brick`) with `dashed` style for vertical, horizontal, or oblique asymptotes.
  - Keep dimensions compact for A5 paper so plots do not cause overfull `\vbox` or page breaks inside unbreakable blocks.
