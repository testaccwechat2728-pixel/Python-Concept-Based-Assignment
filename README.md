# EduTrack: Smart Student Attendance & Performance Analytics System

**PCET's Pimpri Chinchwad University (PCU), Sate Maval, Pune**  
**Department:** Computer Science & Engineering (AI & ML)  
**Academic Year:** 2026 – 2027 | **Semester:** III | **Record No.:** ACAD/R/26  
**Assignment Category:** Major Defaulters (21% – 50% Attendance)  
**Task 3:** Concept-Based Assignment — *Create a simple Python application, upload it to GitHub, and submit a 3–4 page report.*  

📄 **[View Full 3-Page Markdown Report (REPORT.md)](./REPORT.md)**  
📥 **[Download Printable 3-Page PDF Report (Concept_Assignment_Report.pdf)](./Concept_Assignment_Report.pdf)**  

---

## Overview

**EduTrack** is a modular, object-oriented Python application designed to solve the real-life academic problem of student attendance tracking, defaulter categorization, and GPA analytics in universities.

### Key Features
- **Object-Oriented Modeling:** `Student` and `AttendanceRecord` classes with encapsulated state and `@property` calculations.
- **Automated Defaulters Identification:** Automatically categorizes students into:
  - **Critical Defaulters:** `< 20%`
  - **Major Defaulters:** `21% – 50%`
  - **Moderate Defaulters:** `50% – 75%`
  - **Eligible / Regular:** `>= 75%`
- **Performance Analytics:** Cohort attendance average, class GPA calculation, and remedial task allocations.
- **Persistent Storage:** JSON database storage (`students_db.json`) and automated CSV spreadsheet export (`students_export.csv`).
- **Robust Exception Handling:** Guards against invalid user input, invalid score bounds (0–100), and missing file exceptions.

---

## Project Structure

```
Python-Concept-Based-Assignment/
│
├── models.py                   # Data models (Student, AttendanceRecord)
├── analytics.py                # Statistical analytics & defaulters classification
├── storage.py                  # JSON persistence & CSV export
├── app.py                      # Main menu application & automated demo
│
├── students_db.json            # JSON database storing student records
├── students_export.csv         # Generated CSV spreadsheet
│
├── code_models.png             # Syntax-highlighted photo of models.py
├── code_analytics.png          # Syntax-highlighted photo of analytics.py
├── code_app.png                # Syntax-highlighted photo of app.py
├── output_screenshot.png       # Photo of verified execution output
│
├── output.txt                  # Terminal execution log
├── REPORT.md                   # Complete 3-page submission report
├── Concept_Assignment_Report.pdf # Printable 3-page official PDF report
└── README.md                   # Repository guide
```

---

## Application Screenshots

### 1. Data Models (`models.py`)
![models.py Code Photo](code_models.png)

### 2. Execution & Defaulter Categorization Output
![Terminal Execution Output](output_screenshot.png)

---

## How to Run

1. Clone or download the repository:
   ```bash
   git clone https://github.com/testaccwechat2728-pixel/Python-Concept-Based-Assignment.git
   cd Python-Concept-Based-Assignment
   ```

2. Run the automated demonstration:
   ```bash
   python app.py --demo
   ```

3. Or run the interactive menu:
   ```bash
   python app.py
   ```
