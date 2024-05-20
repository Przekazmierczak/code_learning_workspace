"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.
The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import deque

class Solution:
    # def maxDistance(self, grid: List[List[int]]) -> int:
    def maxDistance(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        que = deque([])
        res = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    que.append((row, col))
        
        while que:
            row, col = que.popleft()
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if newRow in range(ROWS) and newCol in range(COLS) and grid[newRow][newCol] == 0:
                    grid[newRow][newCol] = grid[row][col] + 1
                    res = max(grid[newRow][newCol], res)
                    que.append((newRow, newCol))
        return res - 1
            

def main():
    grid = [[1,0,1],[0,0,0],[1,0,1]]

    solution = Solution()

    result = solution.maxDistance(grid)
    
    print(result)


if __name__ == "__main__":
    main()