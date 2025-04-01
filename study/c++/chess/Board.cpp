#include "Board.h"
#include "Piece.h"

Board::Board() {
    turn = "white";
    castling = "KQkq";
    enpassant = {NULL, NULL};
    board = create_board ();
}

std::array<std::array<std::unique_ptr<Piece>, 8>, 8> Board::create_board () {
    std::array<std::array<char, 8>, 8> simplify_board = {{
        {'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'},
        {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
        {'r', 'n', 'b', 'k', 'q', 'b', 'n', 'r'}
    }};

    std::array<std::array<std::unique_ptr<Piece>, 8>, 8> board;

    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            if (simplify_board[row][col] != ' ') {
                board[row][col] = std::make_unique<Piece>(simplify_board[row][col], row, col);
            }
        }
    }

    return board;
}

void Board::add_moves() {
    std::array<std::array<Piece::Result, 8>, 8> possible_moves;
    std::unordered_set<std::array<int, 2>, PositionHash> attacked_positions;
    std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>, PositionHash>, PositionHash> checkin_pieces;
    std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>, PositionHash>, PositionHash> pinned_pieces;
    bool end = true;
    std::string winner;

    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            if (board[row][col] && board[row][col]->player != turn) {
                possible_moves[row][col] = board[row][col]->check_piece_possible_moves(*this, attacked_positions, checkin_pieces, pinned_pieces);
            }
        }
    }

    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            if (board[row][col] && board[row][col]->player == turn) {
                possible_moves[row][col] = board[row][col]->check_piece_possible_moves(*this, attacked_positions, checkin_pieces, pinned_pieces);

                if (end) {
                    Piece::Result curr_res = possible_moves[row][col];
                    if (curr_res.moves.size() || curr_res.attacks.size()) {
                        end = false;
                    }
                }
            }
        }
    }
    // std::cout << possible_moves[5][1].attacks[1][0] << " " << possible_moves[5][1].attacks[1][1] << std::endl;

    // for (auto attacked_position : attacked_positions) {
    //     std::cout << attacked_position[0] << " " << attacked_position[1] << std::endl;
    // }

}

void Board::print_board() {
    for (int row = 0; row < ROWS; row++) {
        std::cout << row + 1 << " ";
        for (int col = 0; col < COLS; col++) {
            if (board[row][col]) {
                std::cout << "[" << board[row][col]->symbol << "]";
            } else {
                std::cout << "[ ]";
            }
        }
        std::cout << std::endl;
    }
    std::cout << "   a  b  c  d  e  f  g  h " << std::endl;
}