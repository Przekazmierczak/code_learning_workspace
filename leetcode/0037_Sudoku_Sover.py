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
from collections import deque

class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def backTrack(i, j):
            if i == 9:
                return True

            if j == 8:
                new_i = i + 1
                new_j = 0
            else:
                new_i = i
                new_j = j + 1

            box_id = i // 3 * 3 + j // 3
            
            if board[i][j] != ".":
                return backTrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    if num not in rows[i] and num not in columns[j] and num not in boxes[box_id]:
                        rows[i].add(num)
                        columns[j].add(num)
                        boxes[box_id].add(num)
                        board[i][j] = str(num)

                        if backTrack(new_i, new_j):
                            return True

                        rows[i].remove(num)
                        columns[j].remove(num)
                        boxes[box_id].remove(num)
                        board[i][j] = "."
            
            return False
        
        rows, columns, boxes = [], [], []

        for _ in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].add(num)
                    columns[j].add(num)

                    box_id = i // 3 * 3 + j // 3
                    boxes[box_id].add(num)

        backTrack(0, 0)

        return board

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