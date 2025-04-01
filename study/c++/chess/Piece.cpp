#include "Board.h"
#include "Piece.h"

Piece::Piece(
    char input_symbol,
    int input_row,
    int input_column
) {
    symbol = input_symbol;
    row = input_row;
    column = input_column;

    piece = legend[input_symbol]["piece"];
    player = legend[input_symbol]["player"];
}

bool Piece::is_valid_position(int row, int column) {
    return row >= 0 && row < ROWS && column >= 0 && column < COLS;
}

bool Piece::is_not_pinned(
    std::array<int, 2> piece_position,
    std::array<int, 2> move,
    Board& board_class,
    std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>, PositionHash>, PositionHash>& pinned_pieces
) {
    return (
        player != board_class.turn ||
        !pinned_pieces.count(piece_position) ||
        (
            pinned_pieces.count(piece_position) &&
            pinned_pieces[piece_position].count(move)
        )
    );
}

std::unordered_set<std::array<int, 2>, PositionHash> Piece::flatting_checkin_pieces(
    std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>, PositionHash>, PositionHash>& checkin_pieces
) {
    std::unordered_set<std::array<int, 2>, PositionHash> checking_positions;

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

Piece::Result Piece::check_piece_possible_moves (
    Board& board_class,
    std::unordered_set<std::array<int, 2>, PositionHash>& attacked_positions,
    std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>, PositionHash>, PositionHash>& checkin_pieces,
    std::unordered_map<std::array<int, 2>, std::unordered_set<std::array<int, 2>, PositionHash>, PositionHash>& pinned_pieces
) {
    Result result;

    bool opponent = (player == board_class.turn) ? false : true;

    auto checking_positions = flatting_checkin_pieces(checkin_pieces);

    if (piece == "pawn") {
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
                int new_column = column + direction[1];

                if (
                    is_valid_position(new_row, new_column) &&
                    board_class.board[new_row][new_column] &&
                    board_class.board[new_row][new_column]->player != player
                ) {
                    result.moves.push_back({new_row, new_column});
                    if (board_class.board[new_row][new_column]->piece == "king") {
                        checkin_pieces[{row, column}];
                    }
                }
                
                if (is_valid_position(new_row, new_column)) {
                    attacked_positions.insert({new_row, new_column});
                }
            }
        } else {
            bool can_move_second_time = true;
            for (auto direction : directions) {
                int new_row = row + direction[0];
                int new_column = column + direction[1];

                if (
                    is_valid_position(new_row, new_column) &&
                    !board_class.board[new_row][new_column] &&
                    can_move_second_time
                ) {
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
                int new_column = column + direction[1];

                if (
                    is_valid_position(new_row, new_column) &&
                    board_class.board[new_row][new_column] &&
                    board_class.board[new_row][new_column]->player != player
                ) {
                    if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                        if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                            result.attacks.push_back({new_row, new_column});
                        }
                    }
                }

                if (
                    is_valid_position(new_row, new_column) &&
                    std::array<int, 2>{new_row, new_column} == board_class.enpassant
                ) {
                    if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                        if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                            result.attacks.push_back({new_row, new_column});
                        }
                    }
                }
            }
        }
    }
    
    return result;
}