"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

class Solution:
    # def closedIsland(self, grid: List[List[int]]) -> int:
    def closedIsland(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()
        
        def dfs(row, col):
            if row not in range(ROWS) or col not in range(COLS):
                return False
            elif grid[row][col] == 1 or (row, col) in visit:
                return True
            visit.add((row, col))
            island = True
            for direction in directions:
                ifIsland = dfs(row + direction[0], col + direction[1])
                island = island and ifIsland

            return island
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 and (row, col) not in visit:
                    if dfs(row, col):
                        res += 1
        return res
            

def main():
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]

    solution = Solution()

    result = solution.closedIsland(grid)
    
    print(result)


if __name__ == "__main__":
    main()