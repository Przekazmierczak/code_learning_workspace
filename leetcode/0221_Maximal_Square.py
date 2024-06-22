"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""

class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    def maximalSquare(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "1":
                    dp[row + 1][col + 1] = min(dp[row][col], dp[row + 1][col], dp[row][col + 1]) + 1
                    res = max(res, dp[row + 1][col + 1])
        return res ** 2
            

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    solution = Solution()

    result = solution.maximalSquare(matrix)
    
    print(result)


if __name__ == "__main__":
    main()