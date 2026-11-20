import numpy as np

# Create a 1D array
arr = np.arange(1, 11)
print("Original Array:", arr)

# Slicing operations
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])

# Statistical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 5
print("Array after Broadcasting:", arr)