"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_island = 0

        def check_island(row, col, count):
            if row not in range(rows) or col not in range(cols) or grid[row][col] == 0 or (row, col) in visited:
                return count
            
            visited.add((row, col))
            count += 1

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for neighbor in neighbors:
                neigh_row, neigh_col = neighbor
                count = check_island(neigh_row, neigh_col, count)

            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = check_island(row, col, 0)
                    max_island = max(area, max_island)
                    
        return max_island
              

def main():
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

    solution = Solution()

    result = solution.maxAreaOfIsland(grid)
    
    print(result)


if __name__ == "__main__":
    main()