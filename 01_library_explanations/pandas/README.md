🧩 1. pandas

The foundation of almost all data analysis in Python.

What it does:
Helps you read, clean, manipulate, and analyze data easily.
Think of it as a super powerful Excel inside Python.

• You’ll use it to:

• Read .csv or .xlsx files

• Filter data, handle missing values

• Calculate statistics like averages, counts, etc.

• Prepare data for visualization or modeling


Example:

import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())

print(df['type'].value_counts())
