"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 
Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
from collections import deque

class Solution:
    # def shortestBridge(self, grid: List[List[int]]) -> int:
    def shortestBridge(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        stack = []
        
        def island(row, col):
            if row not in range(0, ROWS) or col not in range(0, COLS) or grid[row][col] == 0:
                return True
            if (row, col) in visit:
                return False
            visit.add((row, col))
            edge = False
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                edge = island(newRow, newCol) or edge
            if edge:
                stack.append((row, col, 0))
            return edge
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    island(row, col)
                    break
            if grid[row][col] == 1:
                break 
        
        que = deque(stack)

        while que:
            row, col, length = que.popleft()
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if newRow in range(ROWS) and newCol in range(COLS) and (newRow, newCol) not in visit:
                    if grid[newRow][newCol] == 1:
                        return length
                    que.append((newRow, newCol, length + 1))
                    visit.add((newRow, newCol))
            

def main():
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

    solution = Solution()

    result = solution.shortestBridge(grid)
    
    print(result)


if __name__ == "__main__":
    main()