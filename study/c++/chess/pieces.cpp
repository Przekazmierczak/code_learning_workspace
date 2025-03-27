#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <memory>

class Piece {
    public:
        const int ROWS = 8;
        const int COLS = 8;
        char symbol;
        int row;
        int column;
        std::string piece;
        std::string player;

        std::unordered_map<char, std::unordered_map<std::string, std::string>> legend = {
            {'R', {{"piece", "rook"}, {"player", "white"}}},
            {'N', {{"piece", "knight"}, {"player", "white"}}},
            {'B', {{"piece", "bishop"}, {"player", "white"}}},
            {'K', {{"piece", "king"}, {"player", "white"}}},
            {'Q', {{"piece", "queen"}, {"player", "white"}}},
            {'P', {{"piece", "pawn"}, {"player", "white"}}},
            {'r', {{"piece", "rook"}, {"player", "black"}}},
            {'n', {{"piece", "knight"}, {"player", "black"}}},
            {'b', {{"piece", "bishop"}, {"player", "black"}}},
            {'k', {{"piece", "king"}, {"player", "black"}}},
            {'q', {{"piece", "queen"}, {"player", "black"}}},
            {'p', {{"piece", "pawn"}, {"player", "black"}}}
        };

        Piece(char input_symbol, int input_row, int input_column) {
            symbol = input_symbol;
            row = input_row;
            column = input_column;

            auto piece = legend[input_symbol]["piece"];
            auto player = legend[input_symbol]["player"];
        }

        struct Result {
            std::vector<std::array<int, 2>> moves;
            std::vector<std::array<int, 2>> attacks;
            bool promotion = false;
        };

        bool is_valid_position(int row, int column) {
            return row >= 0 && row < ROWS && column >= 0 && column < COLS;
        }

        bool is_not_pinned(
            std::array<int, 2> piece_position,
            std::array<int, 2> move,
            Board& board_class,
            std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>>>& pinned_pieces
        ) {
            return (player != board_class.turn || !pinned_pieces.count(piece_position) || (pinned_pieces.count(piece_position) && pinned_pieces[piece_position].count(move)));
        }

        std::unordered_set<std::array<int, 2>> flatting_checkin_pieces(std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>>>& checkin_pieces) {
            std::unordered_set<std::array<int, 2>> checking_positions;

            if (checking_positions.size() == 1) {
                for (auto key : checkin_pieces) {
                    checking_positions.insert(key.first);
                    for (auto value : key.second) {
                        checking_positions.insert(value);
                    }
                }
            }
            return checking_positions;
        }

        Result check_piece_possible_moves (
            Board& board_class,
            std::unordered_set<std::array<int, 2>>& attacked_positions,
            std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>>>& checkin_pieces,
            std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>>>& pinned_pieces
        ) {
            Result result;

            bool opponent = (player == board_class.turn) ? false : true;

            auto checking_positions = flatting_checkin_pieces(checkin_pieces);

            if (piece == "Pawn") {
                int direction_by_colour = player == "white" ? 1: -1;

                std::vector<std::array<int, 2>> directions = {{direction_by_colour, 0}};

                if ((player == "white" && row == 1) || (player == "black" && row == 6)) {
                    directions.push_back({direction_by_colour * 2, 0});
                }

                if ((player == "white" && row == 6) || (player == "black" && row == 1)){
                    result.promotion = true;
                }

                if (opponent) {
                    directions = {{direction_by_colour, 1}, {direction_by_colour, -1}};
                    for (auto direction : directions) {
                        int new_row = row + direction[0];
                        int new_column = row + direction[1];

                        if (is_valid_position(new_row, new_column) && board_class.board[new_row][new_column] && board_class.board[new_row][new_column]->player != player) {
                            result.moves.push_back({new_row, new_column});
                            if (board_class.board[new_row][new_column]->piece == "king") {
                                checkin_pieces[{row, column}];
                            }
                        }
                        
                        if (is_valid_position(new_row, new_column)) {
                            attacked_positions.insert({new_row, new_column});
                        }
                    }
                }

                else {
                    bool can_move_second_time = true;
                    for (auto direction : directions) {
                        int new_row = row + direction[0];
                        int new_column = row + direction[1];

                        if (is_valid_position(new_row, new_column) && !board_class.board[new_row][new_column] && can_move_second_time) {
                            if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                                if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                    result.moves.push_back({new_row, new_column});
                                }
                            }
                        } else {
                            can_move_second_time = false;
                        }
                    }

                    directions = {{direction_by_colour, 1}, {direction_by_colour, -1}};
                    for (auto direction : directions) {
                        int new_row = row + direction[0];
                        int new_column = row + direction[1];

                        if (is_valid_position(new_row, new_column) && board_class.board[new_row][new_column] && board_class.board[new_row][new_column]->player != player) {
                            if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                                if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                    result.attacks.push_back({new_row, new_column});
                                }
                            }
                        }

                        if (is_valid_position(new_row, new_column) && std::array<int, 2>{new_row, new_column} == board_class.enpassant) {
                            if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                                if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                    result.attacks.push_back({new_row, new_column});
                                }
                            }
                        }
                    }
                }

                for (auto direction : directions) {
                    std::cout << direction[0] << "\n";
                    std::cout << direction[1] << "\n";
                }

                std::cout <<"promotion:" << result.promotion << "\n";
            }

            return result;
        }
};

class Board {
    public:
        const int ROWS = 8;
        const int COLS = 8;
        
        std::string turn;
        std::string castling;
        std::array<int, 2> enpassant;

        std::array<std::array<std::unique_ptr<Piece>, 8>, 8> board;


        std::array<std::array<std::unique_ptr<Piece>, 8>, 8> create_board () {
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
        // std::array<std::array<Piece, 8>, 8> create_board (std::array<std::array<char, 8>, 8>simplify_board) {

        // }
        
        Board() {
            turn = "white";
            castling = "KQkq";
            enpassant = {NULL, NULL};
            board = create_board ();
        }

        void print_board() {
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
};



int main() {
    // Piece piece("Pawn", "white", 1, 3);

    // std::vector<std::tuple<std::string, std::string, std::array<int, 2>>> board = {
    //     {"pawn", "white", {1, 0}}, {"pawn", "white", {2, 4}}, {"pawn", "white", {1, 6}},
    //     {"pawn", "black", {6, 3}}, {"pawn", "black", {5, 4}}, {"pawn", "black", {6, 7}},
    //     {"rook", "white", {0, 0}}, {"rook", "white", {5, 7}}, {"rook", "black", {7, 0}}, {"rook", "black", {7, 4}},
    //     {"knight", "white", {2, 0}}, {"knight", "white", {6, 4}}, {"knight", "black", {7, 1}}, {"knight", "black", {5, 5}},
    //     {"bishop", "white", {4, 1}}, {"bishop", "black", {7, 2}}, {"queen", "white", {4, 3}},
    //     {"king", "white", {0, 4}}, {"king", "black", {7, 3}}
    // };

    // Piece::Result result = piece.check_piece_possible_moves(board, "white");

    Board class_board;

    auto board = class_board.create_board();

    std::cout << board[0][3]->piece << std::endl;
    std::cout << class_board.turn << std::endl;

    class_board.print_board();

    return 0;
}


// std::cout << "1 [R][N][B][Q][K][B][N][R]" << "\n";
// std::cout << "2 [P][P][P][P][P][P][P][P]" << "\n";
// std::cout << "3 [ ][ ][ ][ ][ ][ ][ ][ ]" << "\n";
// std::cout << "4 [ ][ ][ ][ ][ ][ ][ ][ ]" << "\n";
// std::cout << "5 [ ][ ][ ][ ][ ][ ][ ][ ]" << "\n";
// std::cout << "6 [ ][ ][ ][ ][ ][ ][ ][ ]" << "\n";
// std::cout << "7 [p][p][p][p][p][p][p][p]" << "\n";
// std::cout << "8 [r][n][b][q][k][b][n][r]" << "\n";
// std::cout << "   a  b  c  d  e  f  g  h " << "\n";