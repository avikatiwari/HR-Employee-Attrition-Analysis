HR Employee Attrition Analysis

A data analytics project exploring employee attrition using Python,
SQL, Excel, and Power BI.

📌 Project Overview

Employee attrition is an important HR analytics problem because
understanding who leaves, where attrition is concentrated, and which
employee characteristics are associated with attrition can help
organizations investigate workforce patterns and make better-informed HR
decisions.

This project analyzes the IBM HR Employee Attrition dataset,
downloaded from Kaggle, using a multi-tool analytics workflow:

Python → data cleaning, exploratory data analysis (EDA), and
statistical exploration

SQL (MySQL) → structured business-question analysis

Excel → dataset storage and working copy

Power BI → planned interactive dashboards and visualizations

The project is being developed progressively, with additional SQL
questions and dashboard analysis to be added as the analysis expands.

🎯 Project Objectives

The main objectives of this project are to:

Clean and prepare the HR dataset for analysis.

Explore employee and workforce characteristics.

Analyze patterns associated with employee attrition.

Answer practical HR-related questions using SQL.

Compare employee groups using attrition rates.

Identify roles and employee segments with higher numbers of
attrition cases.

Build interactive visualizations and dashboards in Power BI.

Present the analysis in a clear, portfolio-ready format.

🗂️ Dataset

Dataset: IBM HR Employee Attrition dataset
Source: Kaggle

The dataset contains employee-level information covering demographic,
job, compensation, satisfaction, involvement, travel, and
attrition-related attributes.

Important fields used in the analysis

Some of the fields used across the Python and SQL analysis include:

Age

Gender

Department

JobRole

MonthlyIncome

PercentSalaryHike

Attrition

DistanceFromHome

BusinessTravel

JobSatisfaction

JobInvolvement

JobLevel

OverTime

MaritalStatus

Education

EducationField

EnvironmentSatisfaction

WorkLifeBalance

YearsAtCompany

TotalWorkingYears

YearsInCurrentRole

YearsSinceLastPromotion

YearsWithCurrManager

NumCompaniesWorked

TrainingTimesLastYear

🧹 Data Cleaning --- Python

The initial data-cleaning stage was completed using Python and
Pandas.

The workflow included:

Loading the Excel dataset with Pandas

Inspecting the dataset shape and columns

Checking for missing/null values

Checking duplicate records

Reviewing data types and dataset information

Generating descriptive statistics

Removing columns that were not required for the analysis

Columns removed during cleaning

The following columns were removed because they did not contribute
meaningful analytical information for this project:

EmployeeCount

Over18

StandardHours

EmployeeNumber

The cleaned dataset was then used for exploratory analysis.

📊 Exploratory Data Analysis --- Python

Python was used to explore how different employee characteristics relate
to attrition.

Categorical analysis

Attrition was explored across variables such as:

Gender

Department

Job Role

Business Travel

Marital Status

Education Field

Job Level

Overtime

Education

Environment Satisfaction

Job Satisfaction

Work-Life Balance

Stock Option Level

Numerical analysis

Numerical variables were also compared across employees who stayed and
employees who left, including:

Age

Monthly Income

Daily Rate

Hourly Rate

Monthly Rate

Distance From Home

Total Working Years

Years at Company

Years in Current Role

Years Since Last Promotion

Years With Current Manager

Training Times Last Year

Number of Companies Worked

Percent Salary Hike

The Python analysis is available in:

HR_Attrition_Data_Analysis.py

🗄️ SQL Analysis --- MySQL

After the Python cleaning and EDA stage, the original Kaggle/Excel
dataset was imported into MySQL for structured querying.

The SQL analysis currently contains 9 business questions (Q1--Q9).

Questions currently completed

Q1 --- Monthly Income

Which employees have a MonthlyIncome below 5,000?

Q2 --- Salary Hike

Which employees have a PercentSalaryHike greater than 10%?

Q3 --- Female Attrition

How many female employees have left the company?

Q4 --- Male Attrition

How many male employees have left the company?

Q5 --- Distance From Home

Among female employees who left the company, which employee(s) have the
greatest DistanceFromHome?

Q6 --- Job Role With Highest Attrition

Which JobRole has the highest number of employees who left the
company?

Q7 --- Business Travel

Among employees in the JobRole with the highest attrition, how does
BusinessTravel relate to employee attrition?

Q8 --- Satisfaction & Involvement

Is the attrition rate higher among employees with JobSatisfaction and
JobInvolvement below 3 compared with other employees?

For this analysis, a CASE expression was used to create two employee
groups:

Low Satisfaction & Low Involvement
Other Employees

Attrition was converted into a binary indicator:

Yes → 1
No  → 0

The AVG() of this indicator was then used to calculate the attrition
rate.

Q9 --- Older Employees in the Highest-Attrition Role

Among employees who left the company, which employees are above 35 years
old and belong to the JobRole with the highest attrition?

🧠 SQL Concepts Practiced

This project has been used to practice practical SQL concepts including:

SELECT

WHERE

COUNT()

MAX()

AVG()

CASE

GROUP BY

ORDER BY

LIMIT

Subqueries

Aggregate functions

Conditional aggregation

Calculating rates from binary indicators

The SQL file is:

01_HR_Attrition_Analysis.sql

Additional SQL questions will be added as the project progresses.

📈 Power BI --- Dashboard & Visualization

The next major stage of the project is Power BI.

The dashboard phase will transform the analysis into interactive
visualizations that make the major HR patterns easier to explore.

Planned dashboard areas

Potential dashboard components include:

Overall employee count

Overall attrition count

Overall attrition rate

Attrition by gender

Attrition by department

Attrition by job role

Attrition by business travel

Attrition by overtime

Attrition by job satisfaction

Attrition by job involvement

Attrition by age group

Attrition by monthly income

Attrition by distance from home

Attrition by years at company

Attrition by job level

Interactive filters/slicers

The exact dashboard design will be finalized after the remaining SQL
analysis and visualization requirements are completed.

🔄 Project Workflow

The overall workflow for this project is:

Kaggle Dataset
      ↓
Excel
      ↓
Python / Pandas
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
MySQL
      ↓
Business Questions & SQL Analysis
      ↓
Power BI
      ↓
Interactive Dashboards & Visualizations
      ↓
Insights & Final Presentation

Python and SQL are being used as complementary parts of the analysis
rather than as replacements for each other.

📁 Repository Structure

HR-Employee-Attrition-Analysis/
│
├── data/
│   └── IBM_HR_Attrition_Project.xlsx
│
├── 01_HR_Attrition_Analysis.sql
│
├── HR_Attrition_Data_Analysis.py
│
└── README.md

File descriptions

File                                   Purpose

data/IBM_HR_Attrition_Project.xlsx   Working dataset

01_HR_Attrition_Analysis.sql         MySQL analysis and business
questions

HR_Attrition_Data_Analysis.py        Python data cleaning and EDA

README.md                            Project documentation

🛠️ Tools & Technologies

Tool           Purpose

Python     Data cleaning and exploratory analysis
Pandas     Data manipulation and analysis
MySQL      SQL-based business analysis
Excel      Dataset storage and preparation
Power BI   Interactive dashboards and visualization
GitHub     Version control and project portfolio

🚧 Current Project Status

Completed

Dataset downloaded from Kaggle

Dataset stored in Excel

Data cleaning completed in Python

Data quality checks performed

Exploratory data analysis completed in Python

SQL database/table prepared

SQL questions Q1--Q9 completed

SQL file added to GitHub

Python analysis added to GitHub

Dataset added to GitHub

In Progress / Next Steps

Add remaining SQL business questions

Finalize SQL analysis

Build Power BI dashboard

Add interactive visualizations

Identify and document key findings

Add dashboard screenshots to the README

Finalize project presentation

🔍 Key Analytical Direction

Rather than treating the project as only a data-cleaning exercise, the
analysis is being developed as a complete data analytics workflow:

Clean → Explore → Query → Visualize → Interpret

The goal is to understand employee attrition from multiple perspectives
and then communicate the findings through an interactive dashboard.

📌 Future Improvements

As the project develops, additional analysis may include:

More SQL business questions

Deeper employee segmentation

Additional attrition-rate comparisons

Power BI calculated measures

Interactive slicers and drill-downs

Dashboard-level KPIs

Data-driven HR insights

Final recommendations based on the observed patterns

👩‍💻 Project Author

Avika

This project is part of a practical learning portfolio focused on
developing skills in:

Python → SQL → Power BI → Data Analytics

⭐ Project Status

Currently under development --- Python cleaning & EDA and SQL analysis
(Q1--Q9) completed; Power BI dashboard and additional SQL analysis are
the next stages.
