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
    PositionMap& pinned_pieces
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

PositionSet Piece::flatting_checkin_pieces(
    PositionMap& checkin_pieces
) {
    PositionSet checking_positions;
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
    PositionSet& attacked_positions,
    PositionMap& checkin_pieces,
    PositionMap& pinned_pieces
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

    } else if (piece == "rook" || piece == "bishop" || piece == "queen") {
        std::vector<std::array<int, 2>> directions;
        if (piece == "rook") {
            directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        } else if (piece == "bishop") {
            directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        } else if (piece == "queen") {
            directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        }

        if (opponent) {
            for (auto direction : directions) {
                int distance = 1;
                PositionSet current_direction;
                bool absolute_pin_check = false;
                std::array<int, 2> pinned_piece;

                while (true) {
                    int new_row = row + distance * direction[0];
                    int new_column = column + distance * direction[1];

                    if (!is_valid_position(new_row, new_column)) {
                        break;
                    }

                    if (board_class.board[new_row][new_column]) {
                        if (board_class.board[new_row][new_column]->player != player && !absolute_pin_check) {
                            pinned_piece = {new_row, new_column};
                            attacked_positions.insert({new_row, new_column});

                            if (board_class.board[new_row][new_column]->piece == "king" && board_class.board[new_row][new_column]->player != player) {
                                checkin_pieces[{row, column}];
                                int next_row = row + (distance + 1) * direction[0];
                                int next_column = column + (distance + 1) * direction[1];
                                if (is_valid_position(next_row, next_column)) {
                                    attacked_positions.insert({next_row, next_column});
                                }
                                break;
                            } else {
                                absolute_pin_check = true;
                            }
                        } else if (board_class.board[new_row][new_column]->player == player && !absolute_pin_check) {
                            attacked_positions.insert({new_row, new_column});
                            break;
                        } else if (absolute_pin_check) {
                            if (board_class.board[new_row][new_column]->piece == "king" && board_class.board[new_row][new_column]->player != player) {
                                pinned_pieces[pinned_piece].insert({row, column});
                                pinned_pieces[pinned_piece].insert(current_direction.begin(), current_direction.end());
                            }
                            break;
                        } else {
                            break;
                        }
                    } else {
                        if (!absolute_pin_check) {
                            attacked_positions.insert({new_row, new_column});
                        }
                        current_direction.insert({new_row, new_column});
                    }
                    distance++;
                }
            }
        } else {
            for (auto direction : directions) {
                int distance = 1;
                while (true) {
                    int new_row = row + distance * direction[0];
                    int new_column = column + distance * direction[1];

                    if (!is_valid_position(new_row, new_column)) {
                        break;
                    }

                    if (board_class.board[new_row][new_column]) {
                        if (board_class.board[new_row][new_column]->player != player) {
                            if ((is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces))) {
                                if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                    result.attacks.push_back({new_row, new_column});
                                }
                            }
                        }
                        break;
                    } else {
                        if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                            if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                result.moves.push_back({new_row, new_column});
                            }
                        }
                    }
                    distance++;
                }
            }
        }
    } else if (piece == "knight" || piece == "king") {
        std::vector<std::array<int, 2>> directions;
        if (piece == "knight") {
            directions = {{2, 1}, {-2, 1}, {2, -1}, {-2, -1}, {1, 2}, {-1, 2}, {1, -2}, {-1, -2}};
        } else if (piece == "king") {
            directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}, {0, -2}, {0, 2}};
        }

        if (opponent) {
            for (auto direction : directions) {
                int new_row = row + direction[0];
                int new_column = column + direction[1];

                if (is_valid_position(new_row, new_column)) {
                    if (piece == "knight") {
                        attacked_positions.insert({new_row, new_column});
                        if (board_class.board[new_row][new_column] && board_class.board[new_row][new_column]->piece == "king" && board_class.board[new_row][new_column]->player != player) {
                            checkin_pieces[{row, column}];
                        }
                    } else if (piece == "king") {
                        if (direction == std::array<int, 2> {0, -2} || direction == std::array<int, 2> {0, 2}) {
                            continue;
                        }
                        attacked_positions.insert({new_row, new_column});
                    }
                }
            }
        } else {
            for (auto direction : directions) {
                int new_row = row + direction[0];
                int new_column = column + direction[1];

                if (is_valid_position(new_row, new_column)) {
                    if (piece == "knight") {
                        if (!board_class.board[new_row][new_column]) {
                            if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                                if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                    result.moves.push_back({new_row, new_column});
                                }
                            }
                        } else if (board_class.board[new_row][new_column]->player != player) {
                            if (is_not_pinned({row, column}, {new_row, new_column}, board_class, pinned_pieces)) {
                                if (checkin_pieces.empty() || checking_positions.count({new_row, new_column})) {
                                    result.attacks.push_back({new_row, new_column});
                                }
                            }
                        }
                    } else if (piece == "king") {
                        if (direction == std::array<int, 2> {0, -2}) {
                            if ((player == "white" && board_class.castling[0] == 'K') || (player == "black" && board_class.castling[2] == 'k')) {
                                if (
                                    checking_positions.empty() &&
                                    !board_class.board[row][1] &&
                                    !board_class.board[row][2] &&
                                    !attacked_positions.count({row, 1}) &&
                                    !attacked_positions.count({row, 2})
                                ) {
                                    result.moves.push_back({new_row, new_column});
                                }
                            }
                        } else if (direction == std::array<int, 2> {0, 2}) {
                                if ((player == "white" && board_class.castling[1] == 'Q') || (player == "black" && board_class.castling[3] == 'q')) {
                                if (
                                    checking_positions.empty() &&
                                    !board_class.board[row][4] &&
                                    !board_class.board[row][5] &&
                                    !board_class.board[row][6] &&
                                    !attacked_positions.count({row, 4}) &&
                                    !attacked_positions.count({row, 5})
                                ) {
                                    result.moves.push_back({new_row, new_column});
                                }
                            }
                        } else if (!board_class.board[new_row][new_column]) {
                            if (!attacked_positions.count({new_row, new_column})) {
                                result.moves.push_back({new_row, new_column});
                            }
                        } else if (board_class.board[new_row][new_column]->player != player) {
                            if (!attacked_positions.count({new_row, new_column})) {
                                result.attacks.push_back({new_row, new_column});
                            }
                        }
                    }
                }
            }
        }
    }
    
    return result;
}