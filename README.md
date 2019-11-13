# DSA

# The Coin Change Problem
https://leetcode.com/problems/coin-change/

> You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

### Example
```python
coins = 1, 2, 5
amount = 11
```
### Explanatory Matrix
| COIN | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
|------|---|---|---|---|---|---|---|---|---|---|----|----|
| 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
| 2, 1 | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 |
| 5, 2, 1 | 0 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2 | 3 |

The left hand column corresponds to the coin denominations. Each row corresponds to an amount. The values where the rows and columns intersect indicate how many coins of the corresponding denominations are required to reach the desired amount. 

### A Bottom-Up Dynamic Solution

The explanatory matrix illustrates the underlying principle, but this ensuing implementation relies on an array instead of a matrix. This is made possible by a reoccuring invocation of the `min` function.

The array is initialized with a length of `amount + 1`, which is 12 in this case. The extra element is required for the 0 column/amount/index. The remaining elements are initialized to `amount + 1`, i.e. 12.

In the word's of Leonid Vulakh: "For you, this is infinity." Since no value will ever reach or exceed 12, it will never be returned in the ensuing `min` invocations. 0 and -1 do not work as initialization values, because they will always be the minimum. `None` doesn't work because it cannot be compared to an integer. 

The resulting initialization array looks like this:
```python
[0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
```

Here it is with explicit indexes:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |

Now comes the tricky part. There are two nested loops:
```python
for index in range(array + 1):
  for coin in coins:
      if coin <= index>:
          min(array[index], array[index - coin] + 1)
```

The third line is deceptively complex. The best way to wrap your head around it is to walk through the iterations. Let's do that together.

| Code | Explanation |
|------|-------------|
| `for index in range(array + 1)` | index = 0 |
| `for coin in coins` | coin = 1 |
| `if coin <= index` | `1 <= 0` is false so we do not update the value at the 0th index; this holds true for all three denominations |
| `for index in range(array + 1)` | index = 1 (we've completed our first inner loop and are now iterating the outer loop) |
| `for coin in coins` | coin = 1 |
| `if coin <= index` | `1 <= 1` is true |
| `min(array[index], array[index - coin] + 1`) | Continued below for improved readability. |

```python
min(array[index], array[index - coin] + 1`)
= min(array[1], array[1-1] + 1)
= min(12, array[0] + 1)
= min(12, 0 + 1)
= min(12, 1)
= 1
```

`min(array[index], array[index - coin] + 1)` boils down to `min(12, 1)`. Since `1 < 12` (in other news, the sky is blue), we update the value at the first index to 1. 

The updated array looks like this:
```python
[0, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
```

Let's walk through another iteration. 

| Code | Explanation |
|------|-------------|
| `for index in range(array + 1)` | index = 2 |
| `for coin in coins` | coin = 1 |
| `if coin <= index` | `1 <= 2` is true |
| `min(array[index], array[index - coin] + 1`) | Continued below for improved readability. |

```python
min(array[2], array[2-1] + 1)
= min(12, array[1] + 1)
= min(12, 1 + 1)
= min(12, 2)
= 2
```

We update the value at the 2nd index to 2. If we continue through the next iteration (index = 3), the array winds up looking like this:
```python
[0, 1, 2, 3, 12, 12, 12, 12, 12, 12, 12, 12]
```
Things get a little bit more complicated at the 4th index. Let's walk through it. 

| Code | Explanation |
|------|-------------|
| `for index in range(array + 1)` | index = 4 |
| `for coin in coins` | coin = 1 |
| `if coin <= index` | `1 <= 4` is true |
| `min(array[index], array[index - coin] + 1`) | `min(12, 4)` = 4 |
| `for coin in coins` | coin = 4 |
| `min(array[index], array[index - coin] + 1`) | Continued below for improved readability. |
```python
min(array[index], array[index - coin] + 1)
= min(array[4], array[4 - 4] + 1)
= min(4, array[0] + 1)
= min(4, 0 + 1)
= min(4, 1)
= 1
```
Thus, by iterating the inner loop (`for coin in coins`) and invoking `min`, the algorithm determines that there is a more efficient way to get the amount 4, i.e. with 1 x four coin instead of 4 x one coins.

The updated array looks like this:
```python
[0, 1, 2, 3, 4, 12, 12, 12, 12, 12, 12, 12]
```

When we complete the remaining iterations, the completed array looks like this:
```python
[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
```

Once the array is complete, all we have to do is return `array[amount]` to look up the minimum amount of coins required to get to the specified amount. 

The full return statement looks like this:
```python
return dp[amount] if dp[amount] <= amount else -1
```
The `if dp[amount] <= amount else -1` is required in case no amount of coins can create the specified amount, which would indicate that the denominations are not canonical.

### Complexity
#### Time
O((amount + 1) * coins) since we have to iterate through the array, which has a length of amount + 1, and, at each index, we have to iterate through the coins. The + 1 is a constant factor so it can be ignored, and coins is essentially n (technically, n is coins + 1 (for the amount), but that's a constant factor too), so this can be rewritten as O(amount * n)
#### Space
0(amount + 1) since the memoization array requires that many elements. 

### Code
```python
def bottom_up(coins, amount):
    coins = sorted(coins)
    dp = [amount + 1] * (amount + 1) 
    dp[0] = 0
    for i in range(len(dp)): 
        for coin in coins: 
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1
```

### To Do:
* Walk through greedy method
* Walk through top-down approach

