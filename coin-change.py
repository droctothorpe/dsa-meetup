import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def greedy(coins, amount):
    coins = sorted(coins)
    coins.reverse()
    count = 0
    for coin in coins:
        while coin <= amount:
            amount -= coin
            count += 1
    return count if amount == 0 else -1


def bottom(coins, amount):
    memo = [amount + 1] * (amount + 1)
    memo[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            while amount >= coin:
                memo[i] = min(memo[i], memo[i - coin] + 1)


    return memo


c, a = [1, 2, 5], 11
# c, a = [3, 4], 2
print(bottom(c, a))

""""

amount: 1
coin: 1















def greedy(coins, amount):
    # Guardians
    if amount == 0:
        return 0
    coins = sorted(coins)
    coins.reverse()
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    if amount != 0:
        return 0
    return count






def dp(coins, amount):
    # Guardians
    if amount == 0:
        return 0

    coins = sorted(coins)
    lut = [amount + 1] * (amount + 1)
    lut[0] = 0
    for i in range(len(lut)):
        for coin in coins:
            if coin <= i:
                lut[i] = min(lut[i], lut[i - coin] + 1)
    return lut[amount] if lut[amount] <= amount else -1
"""
