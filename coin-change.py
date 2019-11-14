def greedy_subtract(coins, amount):
    # Guardians
    if amount == 0:
        return 0

    coins = sorted(coins)
    coins.reverse()
    count = 0
    for coin in coins:
        while coin <= amount:
            amount -= coin
            count += 1
    return count if amount == 0 else -1


def greedy_divide(coins, amount):
    # Guardians
    if amount == 0:
        return 0

    coins = sorted(coins)
    coins.reverse()
    count = 0
    for coin in coins:
        quotient = int(amount / coin)
        count += quotient
        amount -= quotient * coin
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


def top_down(coins, amount):
    min_coins = amount
    if amount == 0:
        return 0 
    if amount in coins:
        return 1
    for coin in coins:
        if coin <= amount:
            num_coins = 1 + top_down(coins, amount - coin)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def recursive(coins, amount):
    min_coins = amount
    if amount in coins:
        return 1  # base case
    else:
        for coin in [coin for coin in coins if coin <= amount]:
            num_coins = 1 + recursive(coins, amount - coin)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


c, a = [1, 2, 5], 11
# c, a = [1, 2, 3], 5
c, a = [6, 5], 8
c, a = [100, 1], 107
print(recursive(c, a))
