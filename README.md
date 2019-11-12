# dsa

# The Coin Change Problem
https://leetcode.com/problems/coin-change/

> You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

### Example
```python
coins = 1, 2, 5
amount = 11
```

The left hand column corresponds to the coin denominations. Each row corresponds to an amount. The values where the rows and columns intersect indicate how many coins of the corresponding denominations are required to reach the desired value. 
| COIN | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
|------|---|---|---|---|---|---|---|---|---|---|----|----|
| 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
| 2, 1 | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 |
| 5, 2, 1 | 0 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2 | 3 |

The above matrix illustrates the underlying principle, but the actual implementation relies on an array instead of a matrix. This is made possible by a reoccuring invocation of the `min` function.

The array is initialized with a length of `amount + 1`, 12 in this case. The extra element is required for the 0 column/value/index.

The remaining elements are set to `amount + 1`, 12, because that sets us up for the subsequent `min` invocations.

The resulting array looks like this:
```python
[0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
```

Here it is with explicit indexes:
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|----|----|
| 0 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |

Now comes the tricky part. 

There's are two nested loops:
```python
for index in range(array + 1):
  for coin in coins:
      if coin <= index>:
          min(array[index], array[index - coin] + 1)
```

The third line is particularly perplexing. Let's walk through a few iterations. 

| Code | Explanation |
|------|-------------|
| `for index in range(array + 1)` | index = 0 |
| `for coin in coins` | coin = 1 |
| `if coin <= index` | 1 is greater than 0 so we do not update the value at the 0th index; this holds true for all three denominations |
| `for index in range(array + 1)` | index = 1 (we've completed our first inner loop and are now iterating the outer loop) |
| `for coin in coins` | coin = 1 |
| `if coin <= index` | `1 <= 1` is true |
| `min(array[index], array[index - coin] + 1`) | Continued below for improved readability. |

```python
array[index]
= array[1]
= 12

array[index - coin] + 1
= array[1 - 1] + 1
= array[0] + 1 
= 0 + 1
= 1
```

Thus, `min(array[index], array[index - coin] + 1)` boils down to `min(12, 1)`. 1 is less than zero so we update the value at the first index to 1. 



We start with index 0. 

For each index/column, iterate through the coins, started from smallest to largest. 

As each column gets processed, the `min` function is called with two inputs:

1) A look up 


