"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    def islandPerimeter(self, grid):
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(1, 0), (-1, 0),(0, 1), (0, -1)]
        
        for row in range(ROWS):
            for col in range(COLS):
                
                if grid[row][col]:
                    for neighbor in neighbors:
                        new_row, new_col = neighbor
                        neigh_row = new_row + row
                        neigh_col = new_col + col
                        
                        if neigh_row not in range(ROWS) or not neigh_col in range(COLS) or not grid[neigh_row][neigh_col]:
                            res += 1
        
        return res
            

def main():
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

    solution = Solution()

    result = solution.islandPerimeter(grid)
    
    print(result)


if __name__ == "__main__":
    main()