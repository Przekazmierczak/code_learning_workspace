"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque

class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
    def orangesRotting(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        # rotten = set()
        queue = deque([])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        while queue:
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                positions = [(curr_row + 1, curr_col), (curr_row - 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1)]
                for position in positions:
                    pos_row, pos_col = position
                    if pos_row in range(ROWS) and pos_col in range(COLS) and grid[pos_row][pos_col] == 1:
                        queue.append((pos_row, pos_col))
                        grid[pos_row][pos_col] = 2
            count += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1

        return count - 1
       
        
    
def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    solution = Solution()

    result = solution.orangesRotting(grid)
    
    print(result)


if __name__ == "__main__":
    main()