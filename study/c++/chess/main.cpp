#include "Board.h"
#include "Piece.h"

#include "unordered_map"
#include "tuple"

int main() {
    Board class_board;

    auto board = class_board.create_board();

    std::cout << board[0][3]->piece << std::endl;
    std::cout << class_board.turn << std::endl;

    class_board.print_board();

    class_board.add_moves();

    return 0;
}