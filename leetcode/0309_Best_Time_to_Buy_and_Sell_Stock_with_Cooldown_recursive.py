"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        memo = {}
        def operations(index, stock):
            if index >= len(prices):
                return 0
            
            if (index, stock) in memo:
                return memo[(index, stock)]
            
            if stock:
                result = max(prices[index] + operations(index + 2, False), operations(index + 1, True))
            else:
                result =  max(-prices[index] + operations(index + 1, True), operations(index + 1, False))
            
            memo[(index, stock)] = result
            return result
            
        return operations(0, False)
    
def main():
    prices = [1,2,3,0,2]

    solution = Solution()

    result = solution.maxProfit(prices)
    
    print(result)


if __name__ == "__main__":
    main()