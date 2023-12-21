"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from functools import lru_cache

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount):
        result = [float("inf")]
        @lru_cache(None)
        def change(used, coins_sum):
            if coins_sum == amount:
                result[0] = min(result[0], used)
                return
            
            if coins_sum > amount:
                return
            
            for coin in coins:
                change(used + 1, coins_sum + coin)
            
        change(0, 0)

        return result[0] if result[0] != float("inf") else -1

def main():
    coins = [186,419,83,408]
    amount = 6249

    solution = Solution()

    result = solution.coinChange(coins, amount)
    
    print(result)


if __name__ == "__main__":
    main()