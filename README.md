# Data Structures and Algorithms Meetup

For each problem, create a dedicated subfolder in the `problems` directory. 

The solutions file should include:
* A commented link to the problem on Leetcode at the top of the file.
* Annotations that describe the space and time complexity of each approach. 

For example:
```python
# https://leetcode.com/problems/coin-change/

# Time: O(n)
# Space: O(n)
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
```