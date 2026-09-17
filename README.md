<div align="center">

📊 HR Employee Attrition Analysis

Exploring employee attrition through Python, SQL & Data Visualization

Data Cleaning • EDA • Visualization • SQL Analysis

<br>







</div>

📌 About

This project analyzes the IBM HR Employee Attrition dataset to explore patterns related to employee attrition.

The analysis follows a practical data analytics workflow:

Kaggle → Excel → Python → SQL → Visualizations

The project combines Python-based data analysis with SQL business questions to understand the dataset from different perspectives.

🎯 Objectives

Clean and prepare the HR dataset

Perform exploratory data analysis using Python

Explore employee characteristics associated with attrition

Answer practical HR questions using SQL

Create meaningful visualizations from the analysis

Present the findings in a clear and understandable format

🔄 Project Workflow

                    📦 Kaggle Dataset
                           │
                           ▼
                       📗 Excel
                           │
                           ▼
                  🐍 Python + Pandas
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
             🧹 Data Cleaning     🔍 EDA
                                    │
                                    ▼
                              📊 Visualization

                           🗄️ MySQL / SQL
                                    │
                                    ▼
                           Business Questions

🐍 Python Analysis

Python is being used for the data cleaning, exploratory analysis, and visualization stages.

🧹 Data Cleaning

The dataset was inspected and prepared using Pandas.

The cleaning process included:

Checking dataset shape and columns

Checking missing/null values

Checking duplicate records

Reviewing data types

Generating descriptive statistics

Removing unnecessary columns

Removed Columns

EmployeeCount
Over18
StandardHours
EmployeeNumber

🔍 Exploratory Data Analysis

The dataset was explored across different employee attributes.

Categorical Analysis

Gender

Department

Job Role

Business Travel

Marital Status

Education Field

Job Level

Overtime

Job Satisfaction

Environment Satisfaction

Work-Life Balance

Stock Option Level

Numerical Analysis

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

📁 Python file: HR_Attrition_Data_Analysis.py

📊 Data Visualization

The visualization stage will be created using Python based on the cleaned dataset and EDA findings.

Planned visualizations include:

Attrition distribution

Attrition by gender

Attrition by department

Attrition by job role

Attrition by overtime

Attrition by business travel

Attrition by job satisfaction

Attrition by job involvement

Age vs. attrition

Monthly income vs. attrition

Distance from home vs. attrition

Years at company vs. attrition

Visualization Preview

🚧 Coming soon — Python visualizations will be added here.

Once completed, selected charts and key findings will be displayed in this section.

🗄️ SQL Analysis

The dataset was also analyzed using MySQL through a set of practical business questions.

Completed Questions

#

Question / Analysis

Q1

Employees with Monthly Income below 5,000

Q2

Employees with Percent Salary Hike above 10%

Q3

Number of female employees who left

Q4

Number of male employees who left

Q5

Greatest Distance From Home among female employees who left

Q6

Job Role with the highest attrition

Q7

Business Travel and attrition within the highest-attrition Job Role

Q8

Attrition rate for employees with low Job Satisfaction and Job Involvement

Q9

Employees above 35 in the highest-attrition Job Role who left

SQL Concepts Practiced

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
Conditional Aggregation

📁 SQL file: 01_HR_Attrition_Analysis.sql

Additional SQL questions will be added as the project develops.

📈 Key Areas of Analysis

The project focuses on understanding attrition across:

👤 Demographics
   Age • Gender • Education

💼 Job Characteristics
   Department • Job Role • Job Level

💰 Compensation
   Monthly Income • Salary Hike

😊 Employee Experience
   Job Satisfaction • Job Involvement
   Environment Satisfaction • Work-Life Balance

⏱️ Work Conditions
   Overtime • Business Travel

📍 Distance & Experience
   Distance From Home • Years at Company

📁 Repository Structure

HR-Employee-Attrition-Analysis/
│
├── 📂 data/
│   └── IBM_HR_Attrition_Project.xlsx
│
├── 🗄️ 01_HR_Attrition_Analysis.sql
│
├── 🐍 HR_Attrition_Data_Analysis.py
│
└── 📖 README.md

🛠️ Tools Used

Tool

Purpose

🐍 Python

Cleaning, EDA & visualization

🐼 Pandas

Data manipulation & analysis

📊 Matplotlib

Data visualization

🗄️ MySQL

SQL-based analysis

📗 Excel

Dataset storage

🐙 GitHub

Project documentation & version control

🚦 Project Status

Stage

Status

Dataset Collection

✅ Complete

Excel Dataset

✅ Complete

Python Data Cleaning

✅ Complete

Python EDA

✅ Complete

SQL Q1–Q9

✅ Complete

Additional SQL Questions

🔄 In Progress

Python Visualizations

⏳ Next

Final Insights

⏳ Next

🚀 What's Next?

The next stage is to create the Python visualizations and use them to communicate the major patterns found during the analysis.

Additional SQL questions will also be added as the analysis expands.

<div align="center">

👩‍💻 Avika

Data Analytics Project

Python • SQL • Data Visualization

⭐ Built as a practical data analytics portfolio project.

</div>
