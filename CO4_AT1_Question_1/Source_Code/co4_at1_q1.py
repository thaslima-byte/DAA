# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(W, weights, values, n):

    # Create DP table
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            # If current item's weight is less than or equal to capacity
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Driver Code
n = 3

values = [60, 100, 120]
weights = [10, 20, 30]

W = 50

max_profit = knapsack(W, weights, values, n)

print("Number of Items:", n)
print("Profits:", values)
print("Weights:", weights)
print("Truck Capacity:", W)

print("\nMaximum Profit =", max_profit)