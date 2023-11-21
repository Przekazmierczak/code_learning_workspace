"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        current_min = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            current_min = min(current_min, prices[i])
            current_profit = prices[i] - current_min

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
            

def main():
    prices = [7,1,5,3,6,4]

    solution = Solution()

    result = solution.maxProfit(prices)
    
    print(result)


if __name__ == "__main__":
    main()