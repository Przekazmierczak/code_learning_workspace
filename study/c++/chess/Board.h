#ifndef BOARD_H
#define BOARD_H

#include <iostream>
#include <array>

class Piece;

class Board {
    public:
        const int ROWS = 8;
        const int COLS = 8;
        std::string turn;
        std::string castling;
        std::array<int, 2> enpassant;
        std::array<std::array<std::unique_ptr<Piece>, 8>, 8> board;

        Board();

        std::array<std::array<std::unique_ptr<Piece>, 8>, 8> create_board ();

        void add_moves();
        
        void print_board();
};

#endif