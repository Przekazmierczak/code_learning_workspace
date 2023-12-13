"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""

class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
    def solveNQueens(self, n):
        def block_positions(board, row, column):
            new_board = [row[:] for row in board]
            # block row
            for i in range(n):
                if new_board[row][i] == ".":
                    new_board[row][i] = "#"

            # block column
            for i in range(n):
                if new_board[i][column] == ".":
                    new_board[i][column] = "#"

            # block diagonal
            i = 0
            while True:
                if_continue = False
                positions = [(row + i, column + i),
                             (row - i, column - i),
                             (row + i, column - i),
                             (row - i, column + i)]
                
                for position in positions:
                    if 0 <= position[0] < n and 0 <= position[1] < n:
                        if new_board[position[0]][position[1]] == ".":
                            new_board[position[0]][position[1]] = "#"
                        if_continue = True
                i += 1

                if not if_continue: break
            return new_board

        def place_queen(position, board, queens):
            if queens == n:
                result = []
                for i in range(n):
                    joined = "".join(board[i])
                    replaced = joined.replace("#",".")
                    result.append("".join(replaced))

                results.append(result)
                return

            while position // n < n:
                if board[position // n][position % n] == ".":

                    current_row = position // n
                    current_column = position % n

                    current_board = block_positions(board, current_row, current_column)
                    current_board[current_row][current_column] = "Q"

                    place_queen(position + 1, current_board, queens + 1)

                position += 1
            return


        results = []
        board = [["."] * n for _ in range(n)]
        place_queen(0, board, 0)
        return results

def main():
    n = 4

    solution = Solution()

    result = solution.solveNQueens(n)
    
    print(result)


if __name__ == "__main__":
    main()