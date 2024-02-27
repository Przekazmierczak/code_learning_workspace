"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    # def arrangeCoins(self, n: int) -> int:
    def arrangeCoins(self, n):
        res = 0
        curr_sum = 0
        while True:
            res += 1
            curr_sum += res
            if n < curr_sum:
                return res - 1
            

def main():
    n = 5

    solution = Solution()

    result = solution.arrangeCoins(n)
    
    print(result)


if __name__ == "__main__":
    main()