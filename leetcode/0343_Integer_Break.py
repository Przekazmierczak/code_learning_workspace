"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 x 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 x 3 x 4 = 36.

Constraints:

2 <= n <= 58
"""

class Solution:
    # def integerBreak(self, n: int) -> int:
    def integerBreak(self, n):
        dp = [0] * n
        for i in range(n):
            res = 0
            for j in range(0, (i // 2) + 1):
                res = max(dp[j] * dp[i - j - 1], res)
            if i + 1 == n:
                return res
            dp[i] = max(res, i + 1)
            

def main():
    n = 10

    solution = Solution()

    result = solution.integerBreak(n)
    
    print(result)


if __name__ == "__main__":
    main()