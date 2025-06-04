import numpy as np
import random
import os
import re

class Board:
    def __init__(self, turn):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = turn if turn == 1 else -1
        self.turn = turn
        self.avaiable = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.winner = 0

    def print_board(self):
        print(f"1  {self.print_O_X(self.board[0][0])} | {self.print_O_X(self.board[0][1])} | {self.print_O_X(self.board[0][2])}")
        print(f"   ---------")
        print(f"2  {self.print_O_X(self.board[1][0])} | {self.print_O_X(self.board[1][1])} | {self.print_O_X(self.board[1][2])}")
        print(f"   ---------")
        print(f"3  {self.print_O_X(self.board[2][0])} | {self.print_O_X(self.board[2][1])} | {self.print_O_X(self.board[2][2])}")
        print("   a   b   c")

    def print_winner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board()
        if (self.winner == 1):
            print("Player won!")
        else:
            print("Computer won!")

    def player_turn(self):
        move = input("Choose position: ")

        pattern1 = r'^[1-3][a-c]$'
        pattern2 = r'^[a-c][1-3]$'

        while True:
            if re.match(pattern1, move):
                row, col = board.get_move(move[0], move[1])
                if (row, col) in self.avaiable:
                    break
            if re.match(pattern2, move):
                row, col = board.get_move(move[1], move[0])
                if (row, col) in self.avaiable:
                    break
            print("Wrong input")
            move = input("Choose position: ")

        self.avaiable.remove((row, col))
        self.board[row][col] = 1

        self.winner = self.check_for_winner()
    
    def get_move(self, input_row, input_col):
        row = int(input_row) - 1
        
        mapp = {'a': 0, 'b': 1, 'c': 2}
        if input_col in mapp:
            col = mapp[input_col]
        else:
            raise

        return row, col

    def computer_turn(self):
        print("Simulating...")

        # First move always random
        if len(self.avaiable) == 9:
            move = random.choice(list(self.avaiable))
            self.board[move[0]][move[1]] = -1
            self.avaiable.remove(move)
            return

        curr_best_rating = 2
        for move in self.avaiable.copy():
            # Simulate the move
            self.avaiable.remove(move)
            self.board[move[0]][move[1]] = -1

            curr = self.minimax(False)
            # Undo simulated move
            self.avaiable.add(move)
            self.board[move[0]][move[1]] = 0

            if curr < curr_best_rating:
                curr_best_rating = curr
                curr_best_move = move

            if curr_best_rating == -1:
                break

        # Make the move
        self.board[curr_best_move[0]][curr_best_move[1]] = -1
        self.avaiable.remove(curr_best_move)
        self.winner = self.check_for_winner()

    def minimax(self, is_computer):
        winner = self.check_for_winner()
        if winner or not self.avaiable: 
            return winner

        res = 2 if is_computer else -2

        for move in self.avaiable.copy():
            # Simulate the move
            self.avaiable.remove(move)

            if is_computer:
                self.board[move[0]][move[1]] = -1
                res = min(res, self.minimax(False))
            else:
                self.board[move[0]][move[1]] = 1
                res = max(res, self.minimax(True))

            # Undo simulated move
            self.avaiable.add(move)
            self.board[move[0]][move[1]] = 0
        
        return res

    def check_for_winner(self):
        # Check rows
        for row in range(3):
            sum = self.board[row][0] + self.board[row][1] + self.board[row][2]
            if sum == 3: return 1
            if sum == -3: return -1

        # Check columns
        for col in range(3):
            sum = self.board[0][col] + self.board[1][col] + self.board[2][col]
            if sum == 3: return 1
            if sum == -3: return -1
        
        # Check diagonals
        sum = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if sum == 3: return 1
        if sum == -3: return -1

        sum = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if sum == 3: return 1
        if sum == -3: return -1

        return 0

    def print_O_X(self, value):
        if value == self.player:
            return "X"
        elif value == -self.player:
            return "O"
        else:
            return " "
    
    def simulate(self):
        while board.avaiable:
            board.print_board()
            if board.turn:
                board.player_turn()

                if (board.winner):
                    board.print_winner()
                    break
                
                board.turn = 0

                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                board.computer_turn()

                if (board.winner):
                    board.print_winner()
                    break

                board.turn = 1

            os.system('cls' if os.name == 'nt' else 'clear')

        if not self.winner:
            board.print_board()
            print("Its a draw!")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    pattern1 = r'^[1-2]$'

    turn = input("Who starts? 1. Player 2. Computer: ")
    while (not re.match(pattern1, turn)):
        print("Wrong input")
        turn = input("Who starts? 1. Player 2. Computer: ")

    turn = int(turn)
    turn = 0 if turn == 2 else turn

    board = Board(turn)

    os.system('cls' if os.name == 'nt' else 'clear')
    board.simulate()