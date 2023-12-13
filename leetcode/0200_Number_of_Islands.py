"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        def add_visited(row, column):
            if 0 <= row < height and 0 <= column < length and grid[row][column] == "1" and (row, column) not in visited:
                visited.add((row, column))
                add_visited(row + 1, column)
                add_visited(row - 1, column)
                add_visited(row, column + 1)
                add_visited(row, column - 1)
            return
        
        visited = set()
        count = 0
        
        height = len(grid)
        length = len(grid[0])
        
        for row in range(height):
            for column in range(length):
                if grid[row][column] == "1" and (row,column) not in visited:
                    count += 1
                    add_visited(row, column)
        
        return count

def main():
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]

    solution = Solution()

    result = solution.numIslands(grid)
    
    print(result)


if __name__ == "__main__":
    main()