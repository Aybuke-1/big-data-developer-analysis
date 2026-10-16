# Global Software Developer Ecosystem: Learning Pathways, AI Adoption & Career Trends

## 📌 Project Overview
This big data analytics project investigates how software learning methods, programming language proficiencies, and artificial intelligence (AI) adoption impact developer careers and global compensation. 


* **Data Source:** [Stack Overflow Annual Developer Survey (Kaggle)](https://www.kaggle.com/datasets/berkayalan/stack-overflow-annual-developer-survey-2024) (65,437 initial responses)

---

## 🛠️ Technologies & Methodology
* **Language & Libraries:** Python (Pandas, Matplotlib, Seaborn)
* **Data Cleaning & Transformation:**
  * Selected 9 key analytical columns (`EdLevel`, `LearnCode`, `YearsCodePro`, `DevType`, `LanguageHaveWorkedWith`, `AISelect`, `RemoteWork`, `Country`, `ConvertedCompYearly`).
  * Removed missing salary records and filtered out non-realistic outliers ($5,000 to $400,000 range).
  * Standardized experience categories into numerical formats.
  * Reduced the dataset to **21,706 clean records** for analysis.

---

## 📊 Key Findings & Visualizations

### 1. How Developers Learn to Code
Online resources (videos, blogs, communities) and books represent the primary learning medium, outranking traditional academic schooling.
<img width="2000" height="1000" alt="grafik1_ogrenme_yontemleri" src="https://github.com/user-attachments/assets/3017ccbb-636e-41a8-9df2-cac51be4287a" />


### 2. Highest Paying Programming Languages
Among the most widely adopted languages, **Bash/Shell, Python, and TypeScript** command the highest median salaries (> $70,000/year).
<img width="2000" height="1000" alt="grafik2_en_cok_kazandiran_diller" src="https://github.com/user-attachments/assets/2ea94a5f-758b-40af-86cb-fe0d43022854" />


### 3. AI Tool Adoption & Salary Dynamics
Developers actively integrating AI tools into their workflows represent the rapidly emerging tech standard, while senior non-adopters maintain high current baseline compensation.
<img width="1600" height="1000" alt="grafik3_ai_kullanimi_ve_maas" src="https://github.com/user-attachments/assets/f4fdb95b-6876-4e31-a4ce-3ba637651a78" />


---

## 📁 Repository Structure
* `proje.py`: End-to-end Python script for data cleaning, transformation, and automated visualization.
* `temiz_veri.csv`: Cleaned dataset (21,706 rows) ready for Power BI dashboard integration.
* `grafik*.png`: Exported analytical charts.
