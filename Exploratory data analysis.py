# ============================================
# EXPLORATORY DATA ANALYSIS (EDA) PROJECT
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# STEP 1: LOAD DATASET
# --------------------------------------------

# Replace with your dataset file name
df = pd.read_csv("student-mat.csv", sep=';')

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# --------------------------------------------
# STEP 2: BASIC INFORMATION
# --------------------------------------------

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# --------------------------------------------
# STEP 3: CHECK MISSING VALUES
# --------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------
# STEP 4: STATISTICAL SUMMARY
# --------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------
# STEP 5: DATA VISUALIZATION
# --------------------------------------------

# Histogram of Final Grades
plt.figure(figsize=(8,5))
plt.hist(df['G3'], bins=10)
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.show()

# --------------------------------------------
# STEP 6: STUDY TIME VS FINAL GRADE
# --------------------------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(x='studytime', y='G3', data=df)
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

# --------------------------------------------
# STEP 7: ABSENCES VS FINAL GRADE
# --------------------------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(x='absences', y='G3', data=df)
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.show()

# --------------------------------------------
# STEP 8: CORRELATION HEATMAP
# --------------------------------------------

# Select only numeric columns
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# --------------------------------------------
# STEP 9: INSIGHTS
# --------------------------------------------

print("\nEDA Completed Successfully!")

print("""
Key Insights:
1. Students with higher study time often score better.
2. More absences may reduce final grades.
3. Correlation heatmap shows relationships between variables.
""")
