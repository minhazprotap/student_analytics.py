# 📊 Student Performance Analytics CLI

A modular, menu-driven command-line tool built in pure Python to process, analyze, and report student academic performance metrics. 

## 📖 The Story Behind the Project

As I prepare to launch my **MSc in Data Science** journey, my primary goal was to build a bulletproof foundation in core computer science and Python fundamentals before relying on high-level data libraries (like Pandas or NumPy).

Instead of passively watching tutorials, I designed and built this application from scratch. It solves a mini data-pipeline problem: taking raw user inputs, modeling data with optimal structures, processing statistical summaries, and running conditional searches—all through clean, defensive Python logic.

---

## 🛠️ Key Concepts & Python Skills Applied

* **Data Modeling (`Dicts`, `Lists`, `Tuples`):** Designed a dynamic data architecture using nested dictionaries to map student entities to score lists, returning immutable analysis results as tuples.
* **Algorithmic Searching & Filtering:** Implemented custom algorithms using `for` loops to perform extreme-value searches (finding the top performer) and threshold filtering.
* **Defensive Programming:** Applied input validation and `try-except` blocks inside continuous `while` loops to prevent application crashes from invalid user entries.
* **Modular Code Architecture:** Structured functionality into single-responsibility functions with standard docstrings and clean execution flow via a `main()` entry point.

---

## ⚡ Features

1. **Add / Update Records:** Safely collect student names and multiple exam scores with built-in numerical validation.
2. **Class Performance Report:** Calculate totals, averages, letter grades, and pass/fail statuses formatted cleanly in columns.
3. **Top Performer Search:** Analyze class-wide data to dynamically isolate the highest scoring student.
4. **Target Threshold Filtering:** Query records to filter and retrieve students exceeding a target grade threshold.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/student-performance-analytics.git](https://github.com/YOUR_USERNAME/student-performance-analytics.git)
