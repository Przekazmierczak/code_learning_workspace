"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""

class Solution:
    # def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        modulo = 10 ** 9 + 7
        memo = {}
        def dfs(row, col, move):
            if move > maxMove:
                return 0
            if row < 0 or row == m or col < 0 or col == n:
                return 1
            if (row, col, move) in memo:
                return memo[(row, col, move)]
            
            memo[(row, col, move)] = dfs(row - 1, col, move + 1) + dfs(row + 1, col, move + 1) + dfs(row, col - 1, move + 1) + dfs(row, col + 1, move + 1)
            return memo[(row, col, move)]
        return dfs(startRow, startColumn, 0) % modulo
            

def main():
    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0

    solution = Solution()

    result = solution.findPaths(m, n, maxMove, startRow, startColumn)
    
    print(result)


if __name__ == "__main__":
    main()