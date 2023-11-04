"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    board[row][column] = {1,2,3,4,5,6,7,8,9}
                else:
                    board[row][column] = {int(board[row][column])}

        if_solve = float("inf")
        while if_solve != 81:
            for row in range(9):
                for column in range(9):

                    if len(board[row][column]) != 1:
                        for check_row in range(9):
                            if check_row != row and len(board[check_row][column]) == 1:
                                board[row][column] -= board[check_row][column]

                    if len(board[row][column]) != 1:
                        for check_column in range(9):
                            if check_column != column and len(board[row][check_column]) == 1:
                                board[row][column] -= board[row][check_column]

                    for i in range(3):
                            for j in range(3):
                                check_row = ((row // 3) * 3) + i
                                check_column = ((column // 3) * 3) + j
                                
                                if check_row != row and check_column != column and len(board[check_row][check_column]) == 1:
                                    board[row][column] -= board[check_row][check_column]
            
            if_solve = 0
            for row in range(9):
                for column in range(9):
                    if_solve += len(board[row][column])
            
            if if_solve == 81:
                for row in range(9):
                    for column in range(9):
                        board[row][column] = str(board[row][column].pop())

        print(board)



def main():
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    solution = Solution()

    result = solution.solveSudoku(board)
    
    print(result)


if __name__ == "__main__":
    main()