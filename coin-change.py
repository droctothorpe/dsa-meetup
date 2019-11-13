def greedy(coins, amount):
    # Guardians
    if amount == 0:
        return 0

    coins = sorted(coins)
    coins.reverse()
    count = 0
    for coin in coins:
        while coin <= amount:
            amount -= coin # Refactor to divide?
            count += 1
    return count if amount == 0 else -1


def bottom_up(coins, amount):
    # Guardians
    if amount == 0:
        return 0

    coins = sorted(coins)
    dp = [amount + 1] * (amount + 1) 
    dp[0] = 0
    for i in range(len(dp)): 
        for coin in coins: 
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1


c, a = [1, 2, 5], 11
# c, a = [4, 5], 8 
print(bottom_up(c, a))
