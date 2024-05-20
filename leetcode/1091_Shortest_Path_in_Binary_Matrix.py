"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import deque

class Solution:
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, -1)]
        
        que = deque([(0, 0, 1)])
        
        while que:
            row, col, distance = que.popleft()
            if grid[row][col] == 1:
                continue
            elif row == ROWS - 1 and col == COLS - 1:
                return distance
            grid[row][col] = 1
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if newRow in range(ROWS) and newCol in range(COLS):
                    que.append((newRow, newCol, distance + 1))
        return -1
            

def main():
    grid = [[0,0,0],[1,1,0],[1,1,0]]

    solution = Solution()

    result = solution.shortestPathBinaryMatrix(grid)
    
    print(result)


if __name__ == "__main__":
    main()