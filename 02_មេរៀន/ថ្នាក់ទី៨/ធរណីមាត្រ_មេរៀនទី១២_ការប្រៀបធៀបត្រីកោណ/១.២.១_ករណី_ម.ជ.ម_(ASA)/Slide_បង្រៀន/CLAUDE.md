# Project Goal

Create a LaTeX file for a presentation slide that generally looks similar to slides used in PowerPoint.

## General Animation & Slide Design Rule:
- **Number of Frames & Slide Count**: Regarding how many frames each slide contains for step animations, or whether a content section should span 1, 2, or 3 slides, Claude has full autonomy to decide what is optimal to ensure the presentation is flawless, well-paced, clear, and engaging for students.

## Slide Structure & Commands:

### 1. `/slide1`: Title Slide
- Teacher's name
- Lesson title
- School name: Preah Sisowath High School (វិទ្យាល័យព្រះស៊ីសុវត្ថិ)

### 2. `/slide2`: Homework Review (Old Lesson)
- Problem: Check whether two given triangles are congruent (STR and DEF).
- Shows triangles with SAS non-congruence (included angles are not equal).
- Sequential step animation.

### 3. `/slide3`: Angle Construction with Protractor
- 5 steps of constructing an angle using a protractor (50° angle).
- Identical visual elements matching the lesson plan.
- Sequential step animation.

### 4. `/slide4`: Position of Alternate Interior Angles (ទីតាំងមុំឆ្លាស់ក្នុង)
- Two parallel lines cut by a transversal.
- Identification of both pairs of alternate interior angles with callouts.

### 5. `/slide5`: Equality of Alternate Interior Angles (លក្ខណៈមុំឆ្លាស់ក្នុង)
- Shows that alternate interior angles have equal measures (60° and 120°).
- Conclusion: មុំឆ្លាស់ក្នុងមានរង្វាស់ប៉ុនគ្នា។

### 6. `/slide6`: Angles Adjacent to a Side (មុំជាប់ជ្រុង)
- Triangle ABC: side AB, adjacent angles Â and B̂, opposite angle Ĉ.
- Explaining angles adjacent to side AB.

### 7. `/slide7`: New Lesson - ASA Condition (ករណី ម.ជ.ម)
- Question: Constructing two triangles with 1 equal side and 2 adjacent equal angles.
- Overlay/superposition animation of ΔA'B'C' onto ΔABC.
- Theorem: ត្រីកោណពីរស្មើគ្នា កាលណាវាមានជ្រុងមួយប៉ុនគ្នា និងមុំពីរនៅចុងសងខាងនៃជ្រុងនោះប៉ុនគ្នារៀងគ្នា។
- Claude decides 1, 2, or 3 slides.

### 8. `/slide8`: Consequences of ASA (វិបាក នៃករណី ម.ជ.ម)
- Table comparing Hypothesis, Conclusion (ΔABC ≅ ΔA'B'C'), and Consequences (AC = A'C', BC = B'C', ∠C = ∠C').

### 9. `/slide9`: Model Problem (លំហាត់គំរូ)
- Given segments AB and CD intersecting at E, EA = EB, AD || CB.
- Proving ΔAED ≅ ΔBEC by ASA, and deducing ED = EC.

### 10. `/slide10`: Practice Exercise (លំហាត់ប្រតិបត្តិ)
- In given figure, ∠ABC = ∠AED and AB = AE.
- Proving ΔABC ≅ ΔAED (shared angle A) and deducing AD = AC.

### 11. `/slide11`: Homework Assignment (កិច្ចការផ្ទះ + បណ្ដាំផ្ញើ)
- Triangle ABC with AB < AC, angle bisector AD, E on AC with ∠ADE = ∠ADB, ED extended to K.
- Questions: Proving ΔABD ≅ ΔAED (BD = ED, ∠ABD = ∠AED) and ΔKBD ≅ ΔCED (KD = CD, KB = CE).

---

# គោលដៅគម្រោង

បង្កើត file LaTeX មួយ ដែលជា file សម្រាប់ធ្វើ slide presentation ដែលមានលក្ខណៈទូទៅមើលទៅស្រដៀងនឹង slide ដែលប្រើនៅ PowerPoint។

## គោលការណ៍រួមសម្រាប់ Animation, ចំនួន Frame និងចំនួន Slide៖
- **ចំនួន Frame និងចំនួន Slide**៖ ចំពោះចំនួន frame ក្នុងមួយ slide ឬចំនួន slide (១ slide, ២ slide ឬ ៣ slide) សម្រាប់ផ្នែកមេរៀននីមួយៗ គឺទុកឱ្យ Claude ជាអ្នកសម្រេចចិត្តដោយសេរី ថាតើត្រូវរៀបចំយ៉ាងណាដើម្បីឱ្យការបង្ហាញមានភាពល្អឥតខ្ចោះ ច្បាស់លាស់ និងទាក់ទាញចំណាប់អារម្មណ៍សិស្សខ្លាំងបំផុត។

## រចនាសម្ព័ន្ធ Slide និង Commands ទាំងអស់៖
- **`/slide1`** ៖ Slide ចំណងជើងមេរៀន ឈ្មោះគ្រូ និងវិទ្យាល័យព្រះស៊ីសុវត្ថិ
- **`/slide2`** ៖ កំណែកិច្ចការផ្ទះចាស់ (ត្រីកោណ STR និង DEF មិនប៉ុនគ្នា)
- **`/slide3`** ៖ របៀបសង់មុំ 50° ដោយប្រើរ៉ាប់ទ័រ ទាំង ៥ ជំហាន
- **`/slide4`** ៖ ទីតាំង និងលក្ខណៈ: មុំឆ្លាស់ក្នុង (ព្រួញចង្អុលបង្ហាញទាំង ២ គូ)
- **`/slide5`** ៖ លក្ខណៈមុំឆ្លាស់ក្នុងប៉ុនគ្នា (Â₁ = B̂₁ = 60°, Â₂ = B̂₂ = 120°)
- **`/slide6`** ៖ មុំជាប់ជ្រុង នៃត្រីកោណ (ជ្រុង AB, មុំ Â, មុំ B̂, មុំ Ĉ)
- **`/slide7`** ៖ មេរៀនថ្មី ករណី ម.ជ.ម (សំណួរ, រូបភាព, Animation រំកិលរូបត្រួតស៊ីគ្នា, ទ្រឹស្ដីបទ)
- **`/slide8`** ៖ វិបាកនៃករណី ម.ជ.ម (តារាង សមតិកម្ម សន្និដ្ឋាន វិបាក)
- **`/slide9`** ៖ លំហាត់គំរូ (ក. ប្រៀបធៀប ΔAED និង ΔBEC, ខ. ទាញបញ្ជាក់ ED = EC)
- **`/slide10`** ៖ លំហាត់ប្រតិបត្តិ (បង្ហាញថា ΔABC ≅ ΔAED និង AD = AC)
- **`/slide11`** ៖ កិច្ចការផ្ទះថ្មី + បណ្ដាំផ្ញើ (ត្រីកោណ ABC ពុះមុំ AD, បន្លាយ ED ជួប K)
