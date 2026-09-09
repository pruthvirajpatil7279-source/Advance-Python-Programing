#DYNAMIC PROGRAMMING CONCEPT
def climb_stairs(n):
    # Base cases: 0 or 1 stair has only 1 way to climb
    if n <= 1:
        return 1
    
    # dp[i] will store the number of ways to reach step i
    dp = [0] * (n + 1)
    dp[0] = 1  # 1 way to stay at the ground (do nothing)
    dp[1] = 1  # 1 way to reach step 1 (single 1-step)
    
    # Fill the dp array from step 2 up to step n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# Taking input from user
stairs = int(input("Enter the number of stairs: "))
result = climb_stairs(stairs)
print(f"Total number of distinct ways to climb {stairs} stairs: {result}")
print("THANK YOU")
