/*
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 
Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
*/

#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

class Solution {
public:
    std::array<std::pair<int, int>, 8> neighbors = {{{0, 1}, {0, -1}, {1, 1}, {1 , -1}, {1, 0}, {-1, -1}, {-1, 1}, {-1, 0}}};
    
    int check(int row, int col, std::vector<std::vector<int>>& board) {
        int live = 0;
        int curr_row;
        int curr_col;
        
        for (auto& neigh : neighbors) {
            curr_row = row + neigh.first;
            curr_col = col + neigh.second;
            if (curr_row >= 0 && curr_row < board.size() && curr_col >= 0 && curr_col < board[0].size()) {
                if (board[curr_row][curr_col] == 1 || board[curr_row][curr_col] == 2) {
                    live++;
                }
            }
        }
        return live;
    }
    
    void gameOfLife(std::vector<std::vector<int>>& board) {
        int live;
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                live = check(row, col, board);
                if (board[row][col] == 1) {
                    if ((live < 2) || (live > 3)) {
                        board[row][col] = 2;
                    }
                } else {
                    if (live == 3) {
                        board[row][col] = 3;
                    }
                }
            }
        }
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                if (board[row][col] == 2) board[row][col] = 0;
                else if (board[row][col] == 3) board[row][col] = 1;
            }
        }
    }
};