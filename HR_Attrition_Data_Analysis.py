#%% Import Libraries
import os 
os.getcwd()
os.listdir()
import pandas as pd

#%%  Load Dataset
df= pd.read_excel(r"C:\Users\VIVEK TIWARI\OneDrive\Desktop\IBM_HR_Attrition_Project.xlsx")
print(df)

#%%  Understand Dataset
print(df.isnull().sum())
print(df.shape)
print(df.columns)

#%%  Data Cleaning
#deleting unnecessary columns
df= df.drop(columns=["EmployeeCount", "Over18", "StandardHours","EmployeeNumber"])
print(df)
print(df.duplicated().sum())
df.info()
pd.set_option("display.max_columns", None)
print(df.describe())

#%%
# Exploratory Data Analysis (EDA)

#============================================================
# Attrition Distribution
#============================================================

# Business Question:
# How many employees have left the company?

print(df["Attrition"].value_counts())

# Percentage Distribution

print(df["Attrition"].value_counts(normalize=True) * 100)


#============================================================
# Gender Distribution
#============================================================

# Business Question:
# Is the workforce balanced between Male and Female employees?

print(df["Gender"].value_counts())

# Percentage Distribution

print(df["Gender"].value_counts(normalize=True) * 100)

#============================================================
# Department Distribution
#============================================================

# Business Question:
# Which department has the highest number of employees?

print(df["Department"].value_counts())

# Percentage Distribution

print(df["Department"].value_counts(normalize=True) * 100)

#============================================================
# Job Role Distribution
#============================================================

# Business Question:
# Which Job Role has the highest number of employees?

print(df["JobRole"].value_counts())

# Percentage Distribution

print(df["JobRole"].value_counts(normalize=True) * 100)

#============================================================
# Business Travel Distribution
#============================================================

# Business Question:
# Which type of business travel is most common?

print(df["BusinessTravel"].value_counts())

# Percentage Distribution

print(df["BusinessTravel"].value_counts(normalize=True) * 100)

#============================================================
# Marital Status Distribution
#============================================================

# Business Question:
# What is the marital status distribution of employees?

print(df["MaritalStatus"].value_counts())

# Percentage Distribution

print(df["MaritalStatus"].value_counts(normalize=True) * 100)

#============================================================
# Education Field Distribution
#============================================================

# Business Question:
# Which education background do employees belong to?

print(df["EducationField"].value_counts())

# Percentage Distribution

print(df["EducationField"].value_counts(normalize=True) * 100)

#============================================================
# Job Level Distribution
#============================================================

# Business Question:
# How are employees distributed across job levels?

print(df["JobLevel"].value_counts())

# Percentage Distribution

print(df["JobLevel"].value_counts(normalize=True) * 100)


#============================================================
# OverTime Distribution
#============================================================

# Business Question:
# How many employees work overtime?

print(df["OverTime"].value_counts())

# Percentage Distribution

print(df["OverTime"].value_counts(normalize=True) * 100)


#============================================================
# Education Distribution
#============================================================

# Business Question:
# What is the education level of employees?

print(df["Education"].value_counts())

# Percentage Distribution

print(df["Education"].value_counts(normalize=True) * 100)


#============================================================
# Environment Satisfaction Distribution
#============================================================

# Business Question:
# How satisfied are employees with their work environment?

print(df["EnvironmentSatisfaction"].value_counts())

# Percentage Distribution

print(df["EnvironmentSatisfaction"].value_counts(normalize=True) * 100)


#============================================================
# Job Satisfaction Distribution
#============================================================

# Business Question:
# What is the overall job satisfaction level?

print(df["JobSatisfaction"].value_counts())

# Percentage Distribution

print(df["JobSatisfaction"].value_counts(normalize=True) * 100)


#============================================================
# Work Life Balance Distribution
#============================================================

# Business Question:
# How do employees rate their work-life balance?

print(df["WorkLifeBalance"].value_counts())

# Percentage Distribution

print(df["WorkLifeBalance"].value_counts(normalize=True) * 100)

#%%
# Attrition Analysis

#============================================================
# Attrition vs Gender
#============================================================

# Business Question:
# Does gender have any impact on employee attrition?

print(pd.crosstab(df["Gender"], df["Attrition"]))

print(pd.crosstab(
    df["Gender"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs OverTime
#============================================================

# Business Question:
# Does overtime increase employee attrition?

print(pd.crosstab(df["OverTime"], df["Attrition"]))

print(pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Department
#============================================================

# Business Question:
# Which department has the highest attrition rate?

print(pd.crosstab(df["Department"], df["Attrition"]))

print(pd.crosstab(
    df["Department"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Job Role
#============================================================

# Business Question:
# Which job role experiences the highest attrition?

print(pd.crosstab(df["JobRole"], df["Attrition"]))

print(pd.crosstab(
    df["JobRole"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Business Travel
#============================================================

# Business Question:
# Does business travel influence employee attrition?

print(pd.crosstab(df["BusinessTravel"], df["Attrition"]))

print(pd.crosstab(
    df["BusinessTravel"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Marital Status
#============================================================

# Business Question:
# Does marital status affect attrition?

print(pd.crosstab(df["MaritalStatus"], df["Attrition"]))

print(pd.crosstab(
    df["MaritalStatus"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Education Field
#============================================================

# Business Question:
# Which education field has the highest attrition?

print(pd.crosstab(df["EducationField"], df["Attrition"]))

print(pd.crosstab(
    df["EducationField"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Job Level
#============================================================

# Business Question:
# Does job level affect employee attrition?

print(pd.crosstab(df["JobLevel"], df["Attrition"]))

print(pd.crosstab(
    df["JobLevel"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Job Satisfaction
#============================================================

# Business Question:
# Does job satisfaction influence employee attrition?

print(pd.crosstab(df["JobSatisfaction"], df["Attrition"]))

print(pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Environment Satisfaction
#============================================================

# Business Question:
# Does environment satisfaction affect attrition?

print(pd.crosstab(df["EnvironmentSatisfaction"], df["Attrition"]))

print(pd.crosstab(
    df["EnvironmentSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Work Life Balance
#============================================================

# Business Question:
# Does work-life balance influence attrition?

print(pd.crosstab(df["WorkLifeBalance"], df["Attrition"]))

print(pd.crosstab(
    df["WorkLifeBalance"],
    df["Attrition"],
    normalize="index"
) * 100)



#============================================================
# Attrition vs Stock Option Level
#============================================================

# Business Question:
# Do stock options help retain employees?

print(pd.crosstab(df["StockOptionLevel"], df["Attrition"]))

print(pd.crosstab(
    df["StockOptionLevel"],
    df["Attrition"],
    normalize="index"
) * 100)

#%%
# Numerical Analysis

#============================================================
# Age Analysis
#============================================================

# Business Question:
# What is the average age of employees based on attrition?

print(df.groupby("Attrition")["Age"].mean())

print(df.groupby("Attrition")["Age"].median())

print(df.groupby("Attrition")["Age"].min())

print(df.groupby("Attrition")["Age"].max())



#============================================================
# Monthly Income Analysis
#============================================================

# Business Question:
# How does monthly income differ between employees who stayed and left?

print(df.groupby("Attrition")["MonthlyIncome"].mean())

print(df.groupby("Attrition")["MonthlyIncome"].median())

print(df.groupby("Attrition")["MonthlyIncome"].min())

print(df.groupby("Attrition")["MonthlyIncome"].max())



#============================================================
# Daily Rate Analysis
#============================================================

# Business Question:
# Does daily rate differ based on attrition?

print(df.groupby("Attrition")["DailyRate"].mean())



#============================================================
# Hourly Rate Analysis
#============================================================

# Business Question:
# Does hourly rate differ based on attrition?

print(df.groupby("Attrition")["HourlyRate"].mean())



#============================================================
# Monthly Rate Analysis
#============================================================

# Business Question:
# Does monthly rate differ based on attrition?

print(df.groupby("Attrition")["MonthlyRate"].mean())



#============================================================
# Distance From Home Analysis
#============================================================

# Business Question:
# Does distance from home influence attrition?

print(df.groupby("Attrition")["DistanceFromHome"].mean())

print(df.groupby("Attrition")["DistanceFromHome"].median())



#============================================================
# Total Working Years Analysis
#============================================================

# Business Question:
# How many years of experience do employees have?

print(df.groupby("Attrition")["TotalWorkingYears"].mean())

print(df.groupby("Attrition")["TotalWorkingYears"].median())



#============================================================
# Years At Company Analysis
#============================================================

# Business Question:
# Do employees with fewer years at the company leave more?

print(df.groupby("Attrition")["YearsAtCompany"].mean())

print(df.groupby("Attrition")["YearsAtCompany"].median())



#============================================================
# Years In Current Role Analysis
#============================================================

# Business Question:
# Does experience in the current role affect attrition?

print(df.groupby("Attrition")["YearsInCurrentRole"].mean())



#============================================================
# Years Since Last Promotion
#============================================================

# Business Question:
# Does promotion history affect attrition?

print(df.groupby("Attrition")["YearsSinceLastPromotion"].mean())



#============================================================
# Years With Current Manager
#============================================================

# Business Question:
# Does manager relationship duration affect attrition?

print(df.groupby("Attrition")["YearsWithCurrManager"].mean())



#============================================================
# Training Times Last Year
#============================================================

# Business Question:
# Does training frequency impact attrition?

print(df.groupby("Attrition")["TrainingTimesLastYear"].mean())



#============================================================
# Number of Companies Worked
#============================================================

# Business Question:
# Have employees who worked in more companies shown higher attrition?

print(df.groupby("Attrition")["NumCompaniesWorked"].mean())



#============================================================
# Percent Salary Hike
#============================================================

# Business Question:
# Does salary hike impact attrition?

print(df.groupby("Attrition")["PercentSalaryHike"].mean())
