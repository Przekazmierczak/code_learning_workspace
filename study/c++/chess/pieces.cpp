#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <tuple>

class Piece {
    public:
        const int ROWS = 8;
        const int COLS = 8;
        std::string piece;
        std::string player;
        int row;
        int column;

        Piece(std::string input_piece, std::string input_player, int input_row, int input_column) {
            piece = input_piece;
            player = input_player;
            row = input_row;
            column = input_column;
        }

        struct Result {
            std::vector<std::string> moves;
            std::vector<std::string> attacks;
            bool promotion = false;
        };

        bool is_valid_position (int row, int column) {
            return row >= 0 && row < ROWS && column >= 0 && column < COLS;
        }

        Result check_piece_possible_moves (std::vector<std::tuple<std::string, std::string, std::array<int, 2>>> board, std::string turn) {
            Result result;

            bool opponent = true;

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
                    for (auto direction: directions) {
                        int new_row = row + direction[0];
                        int new_column = row + direction[1];

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
        std::string enpassant;
        
};



int main() {
    Piece piece("Pawn", "white", 1, 3);

    std::vector<std::tuple<std::string, std::string, std::array<int, 2>>> board = {
        {"pawn", "white", {1, 0}}, {"pawn", "white", {2, 4}}, {"pawn", "white", {1, 6}},
        {"pawn", "black", {6, 3}}, {"pawn", "black", {5, 4}}, {"pawn", "black", {6, 7}},
        {"rook", "white", {0, 0}}, {"rook", "white", {5, 7}}, {"rook", "black", {7, 0}}, {"rook", "black", {7, 4}},
        {"knight", "white", {2, 0}}, {"knight", "white", {6, 4}}, {"knight", "black", {7, 1}}, {"knight", "black", {5, 5}},
        {"bishop", "white", {4, 1}}, {"bishop", "black", {7, 2}}, {"queen", "white", {4, 3}},
        {"king", "white", {0, 4}}, {"king", "black", {7, 3}}
    };

    Piece::Result result = piece.check_piece_possible_moves(board, "white");

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