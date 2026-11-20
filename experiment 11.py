import pandas as pd
import numpy as np

# Create a Pandas Series with 10 random numbers
data = np.random.randint(1, 100, 10)
s = pd.Series(data)

# Display Series
print("Pandas Series:")
print(s)

# Indexing
print("\nFirst Element:", s[0])

# Data Cleaning
print("\nCheck Missing Values:")
print(s.isnull())

# Statistical Operations
print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Maximum:", s.max())
print("Minimum:", s.min())