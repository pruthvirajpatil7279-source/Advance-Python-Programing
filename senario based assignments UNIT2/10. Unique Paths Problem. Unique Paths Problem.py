#10. Unique Paths Problem
#Develop a Python program to determine the number of unique paths from the top-left corner to the bottom-right corner of a grid.
#Requirements
#ccept the number of rows and columns.
#Use Dynamic Programming.
#Display the total number of unique paths.


def unique_paths(rows, cols):
    # dp[i][j] will store the number of unique paths to reach cell (i, j)
    dp = [[1] * cols for _ in range(rows)]
    
    # Fill the grid starting from cell (1,1), since row 0 and col 0 are all 1s
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[rows - 1][cols - 1]


# Taking input from user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

result = unique_paths(rows, cols)
print(f"Total number of unique paths: {result}")
print("DONE")


