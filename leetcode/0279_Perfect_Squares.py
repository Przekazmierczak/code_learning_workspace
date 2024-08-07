"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 104
"""

class Solution:
    # def numSquares(self, n: int) -> int:
    def numSquares(self, n):
        array = []
        for i in range(1, n + 1):
            num = i * i
            if num <= n:
                array.append(num)
            else:
                break
        
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            for a in array:
                if i - a >= 0:
                    dp[i] = min(dp[i - a] + 1, dp[i])
                    
        return dp[i]
            

def main():
    n = 12

    solution = Solution()

    result = solution.numSquares(n)
    
    print(result)


if __name__ == "__main__":
    main()