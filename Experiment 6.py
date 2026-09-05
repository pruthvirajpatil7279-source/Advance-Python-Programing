#bottom up code :

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack(weights, values, capacity))


#top Down code :

def knapsack(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, capacity):
        if i == n or capacity == 0:
            return 0

        if (i, capacity) in memo:
            return memo[(i, capacity)]

        if weights[i] <= capacity:
            take = values[i] + solve(i + 1, capacity - weights[i])
        else:
            take = 0

        skip = solve(i + 1, capacity)

        memo[(i, capacity)] = max(take, skip)
        return memo[(i, capacity)]

    return solve(0, capacity)


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack(weights, values, capacity))