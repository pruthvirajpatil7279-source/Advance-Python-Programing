import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Display dataset
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(df.select_dtypes(include=np.number).mean())

# Visualize customer churn
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Count")
plt.show()

# Histogram
df.select_dtypes(include=np.number).hist(figsize=(10, 8))
plt.show()

# Detect outliers using boxplot
sns.boxplot(x=df['MonthlyCharges'])
plt.title("Monthly Charges Outliers")
plt.show()

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())