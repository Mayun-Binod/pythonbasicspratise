def coin_change(coins, amount):
    # Initialize a list with amount + 1 (which is impossible, so treated as infinity)
    dp = [float('inf')] * (amount + 1)
    
    # Base case: to make amount 0, you need 0 coins
    dp[0] = 0
    
    # Fill dp table
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[amount] is still infinity, return -1 (impossible)
    return dp[amount] if dp[amount] != float('inf') else -1

# Test case
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print(result)  # Output: 3
