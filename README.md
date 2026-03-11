# Employee Workload Analytics & Productivity Insight System

## Project Overview

The Employee Workload Analytics & Productivity Insight System is a data analytics project designed to analyze employee datasets and generate insights about workforce performance and productivity. The system processes employee information such as age, experience, education level, department, and performance scores to identify trends and patterns.

This project uses Python-based data analysis and visualization tools to transform raw employee data into meaningful insights that help organizations evaluate employee productivity and make better data-driven decisions.

---

## Objectives

* Analyze employee workload and performance using data analytics.
* Identify patterns related to experience, department, and productivity.
* Visualize employee performance using charts and graphs.
* Provide an interactive analytics dashboard for exploring employee data.

---

## Features

* Upload employee datasets in **CSV, Excel, or JSON** format.
* Automatic dataset analysis and statistical summary.
* Identification of numeric and categorical features.
* Data visualization using charts and graphs.
* Department-wise performance analysis.
* Correlation heatmap for feature relationships.
* Interactive **Streamlit dashboard** for exploring employee data.

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit
* Scikit-learn
* NumPy

---

## Project Structure

```
Employee-Workload-Analytics-System
│
├── data
│   ├── combined_employee_dataset.csv
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── dashboard
│   └── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Install the required libraries using:

pip install -r requirements.txt

---

## How to Run the Project

1. Open the terminal in the project folder.

2. Navigate to the dashboard folder:

cd dashboard

3. Run the Streamlit application:

streamlit run dashboard.py

4. After running the command, the dashboard will open automatically in your browser.

If it does not open automatically, go to:

http://localhost:8501

---

## Dataset

The project uses employee datasets containing attributes such as:

* Age
* Years of Experience
* Education Level
* Department
* Performance Score
* Performance Category

These datasets are used to analyze employee productivity and workforce performance.

---

## Results

The system generates insights including:

* Employee performance distribution
* Department-wise productivity comparison
* Experience vs performance analysis
* Correlation between employee attributes
* Visual analytics dashboard

---

## Future Improvements

* Integration with real-time employee databases.
* Advanced machine learning models for improved predictions.
* More interactive dashboard features.
* Role-based access system for HR managers.

---

## Conclusion

The Employee Workload Analytics & Productivity Insight System demonstrates how data analytics and visualization techniques can be applied to human resource management. By analyzing employee data and presenting it through an interactive dashboard, organizations can better understand workforce productivity and make informed decisions.

---

## Author

Ashok Kumar Chapa
