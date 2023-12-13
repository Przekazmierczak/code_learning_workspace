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
        columns = set()
        posit_diags = set()
        negat_diags = set()

        results = []
        queens = []

        def put_queen(row, queens):
            if len(queens) == n:
                current_board = [["."] * n for _ in range(n)]
                for queen in queens:
                    row, column = queen
                    current_board[row][column] = "Q"
                
                result = []
                for i in range(n):
                    result.append("".join(current_board[i]))
                results.append(result)
                return
            
            for column in range(n):
                posit_diag = row + column
                negat_diag = row - column
                if column not in columns and posit_diag not in posit_diags and negat_diag not in negat_diags:
                    queens.append((row, column))
                    columns.add(column)
                    posit_diags.add(posit_diag)
                    negat_diags.add(negat_diag)

                    put_queen(row + 1, queens)

                    queens.pop()
                    columns.remove(column)
                    posit_diags.remove(posit_diag)
                    negat_diags.remove(negat_diag)
        
        put_queen(0, queens)
        return results

def main():
    n = 4

    solution = Solution()

    result = solution.solveNQueens(n)
    
    print(result)


if __name__ == "__main__":
    main()