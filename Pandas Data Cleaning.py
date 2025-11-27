import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



file="https://raw.githubusercontent.com/swapnilsaurav/projects/refs/heads/main/Data%20Cleaning%20for%20HR%20Analytics%20v1.csv"
df = pd.read_csv(file)

# Load updated dataset (line No.8-9 )
# Step 1: Remove duplicates (line No.22)
# Step 2: Handle missing or invalid data(line No.25-36)
# Step 3: Treat Outliers(line No.39-43)
# Step 4: Visualizations(line No.45-72)
# 1. Age Distribution(line No.45-50)
# 2. Salary Distribution(line No.52-56)
# 3. Department Counts(line No.58-63)
# 4. Join Date Trend(line No.65-72)


df = df.drop_duplicates()


df["Name"] = df["Name"].fillna("Unknown")
df["Email"] = df["Email"].replace(["unknown", "not_an_email"], np.nan)
df["Email"] = df["Email"].fillna(method="bfill")
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
df["Age"] = df["Age"].apply(lambda x: x if 18 <= x <= 70 else np.nan)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = pd.to_numeric(df["Salary"], errors='coerce')
df["Salary"] = df["Salary"].apply(lambda x: x if x >= 0 else np.nan)
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors='coerce')
df["Department"] = df["Department"].fillna("Not Specified")
df["Remarks"] = df["Remarks"].replace("", np.nan).fillna("No Remarks")


Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
df["Salary"] = np.clip(df["Salary"], lower_bound, upper_bound)

plt.figure(figsize=(8, 4))
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 4))
sns.boxplot(x=df["Salary"])
plt.title("Salary Distribution with Outliers Treated")
plt.xlabel("Salary")
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(y="Department", data=df, order=df["Department"].value_counts().index)
plt.title("Employees per Department")
plt.xlabel("Count")
plt.ylabel("Department")
plt.show()

plt.figure(figsize=(10, 4))
df["JoinYear"] = df["JoinDate"].dt.year
sns.countplot(x="JoinYear", data=df.sort_values("JoinYear"))
plt.title("Employee Joining Trend by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
