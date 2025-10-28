import pandas as pd

# Load a CSV file (replace with your own)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

# View first few rows
print(df.head())

# Select specific columns
age_sex = df[["age", "sex"]]
print(age_sex.head())

# Filter rows
adults = df[df["age"] > 18]
print(adults.head())

# Group and summarize
print(df.groupby("sex")["age"].mean())
