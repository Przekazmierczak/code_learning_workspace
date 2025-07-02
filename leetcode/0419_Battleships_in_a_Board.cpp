/*
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
*/

#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

class Solution {
public:
    std::array<std::pair<int,int>, 4> positions = {{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}};
    
    bool valid(int row, int col, std::vector<std::vector<char>>& board) {
        if (row < 0 || row >= board.size()) return false;
        if (col < 0 || col >= board[0].size()) return false;
        return true;
    }

    void dfs(int row, int col, std::vector<std::vector<char>>& board) {
        board[row][col] = '.';
        for (auto& position : positions) {
            if (valid(row + position.first, col + position.second, board) && board[row + position.first][col + position.second] == 'X') {
                dfs(row + position.first, col + position.second, board);
            }
        }
    }
    
    int countBattleships(std::vector<std::vector<char>>& board) {
        int count = 0;
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                if (board[row][col] == 'X') {
                    count++;
                    dfs(row, col, board);
                }
            }
        }
        return count;
    }
};