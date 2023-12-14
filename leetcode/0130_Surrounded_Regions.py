"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 
Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
class Solution:
#     def solve(self, board: List[List[str]]) -> None:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        
        def dfs(row, col):
            if row in range(ROWS) and col in range(COLS) and (row, col) not in visited and board[row][col] == "O":
                visited.add((row, col))
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
         
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"
        
        return board

    
def main():
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    solution = Solution()

    result = solution.solve(board)
    
    print(result)


if __name__ == "__main__":
    main()