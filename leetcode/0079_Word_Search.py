"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        row_len = len(board)
        column_len = len(board[0])
        word_len = len(word)
        possibilities = []
        for row in range(0, row_len):
            for column in range(0, column_len):
                possibilities.append((row, column))

        def check(board, possibilities, word, word_pointer, status):
            if word_pointer == word_len:
                return True

            for element in possibilities:
                row, column = element
                if board[row][column] == word[word_pointer]:
                    previous_board = board[row][column]
                    board[row][column] = "_"
                    new_possibilities = []
                    if row != 0:
                        new_possibilities.append((row - 1, column))
                    if row != row_len - 1:
                        new_possibilities.append((row + 1, column))
                    if column != 0:
                        new_possibilities.append((row, column - 1))
                    if column != column_len - 1:
                        new_possibilities.append((row, column + 1))
                    status = check(board, new_possibilities, word, word_pointer + 1, status)
                    board[row][column] = previous_board

            return status
        
        return check(board, possibilities, word, 0, False)


def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "AS"

    solution = Solution()

    result = solution.exist(board, word)
    
    print(result)


if __name__ == "__main__":
    main()