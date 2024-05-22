"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""

class Solution:
    # def numEnclaves(self, grid: List[List[int]]) -> int:
    def numEnclaves(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return (0, True)
            elif grid[row][col] == 0:
                return (0, False)
            grid[row][col] = 0
            count = 0
            edge = False
            for direction in directions:
                currCount, currEdge = dfs(row + direction[0], col + direction[1])
                count += currCount
                edge = edge or currEdge
            count = count + 1 if not edge else 0
            return (count, edge)
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    res += dfs(row, col)[0]
        return res
            

def main():
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

    solution = Solution()

    result = solution.numEnclaves(grid)
    
    print(result)


if __name__ == "__main__":
    main()