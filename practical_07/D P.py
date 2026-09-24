def coin_change(coins, amount):
    dp = [0] + [999] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


n = int(input("Enter number of coins: "))

coins = []
for i in range(n):
    coins.append(int(input("Enter coin: ")))

amount = int(input("Enter amount: "))

print("Minimum coins needed:", coin_change(coins, amount))
