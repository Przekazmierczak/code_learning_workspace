"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:

Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""

class Solution:
    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    def countSubIslands(self, grid1, grid2):
        ROWS = len(grid2)
        COLS = len(grid2[0])
        visit = set()
        res = 0
        
        def dfs(row, col):
            if row not in range(ROWS) or col not in range(COLS) or grid2[row][col] == 0 or (row, col) in visit:
                return True
            
            visit.add((row, col))
            
            status = True
            if grid1[row][col] == 0:
                status = False
            status = dfs(row + 1, col) and status
            status = dfs(row - 1, col) and status
            status = dfs(row, col + 1) and status
            status = dfs(row, col - 1) and status
            return status
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid2[row][col] == 1 and (row, col) not in visit:
                    if dfs(row, col):
                        res += 1
        return res
            

def main():
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

    solution = Solution()

    result = solution.countSubIslands(grid1, grid2)
    
    print(result)


if __name__ == "__main__":
    main()