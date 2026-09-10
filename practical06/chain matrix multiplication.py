def coin_change(coins, amount):
    dp = [0] + [999] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


coins = [1, 2, 5]
amount = int(input("Enter amount: "))

print("Minimum coins:", coin_change(coins, amount))
