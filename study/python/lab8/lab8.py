import numpy as np
import random
import os
import re

class Board:
    def __init__(self, turn):
        self.board = np.zeros((3, 3), dtype=int)
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
        move = input("Wybierz pole: ")
        pattern = r'^[a-c][1-3]$'
        while (not re.match(pattern, move)):
            print("Wrong input")
            move = input("Wybierz pole: ")

        row = int(move[1]) - 1
        
        mapp = {'a': 0, 'b': 1, 'c': 2}
        if move[0] in mapp:
            col = mapp[move[0]]
        else:
            raise
        self.avaiable.discard((row, col))
        self.board[row][col] = 1

        self.winner = self.check_for_winner()

    def computer_turn(self):
        row, col = random.choice(list(self.avaiable))
        self.avaiable.discard((row, col))
        self.board[row][col] = -1

    def check_for_winner(self):
        for row in range(3):
            sum = self.board[row][0] + self.board[row][1] + self.board[row][2]
            if sum == 3: return 1
            if sum == -3: return -1

        for col in range(3):
            sum = self.board[0][col] + self.board[1][col] + self.board[2][col]
            if sum == 3: return 1
            if sum == -3: return -1
        
        sum = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if sum == 3: return 1
        if sum == -3: return -1

        sum = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if sum == 3: return 1
        if sum == -3: return -1

        return 0

    def print_O_X(self, value):
        if value == 1:
            return "X"
        elif value == -1:
            return "O"
        else:
            return " "


if __name__ == "__main__":
    board = Board(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    board.print_board()
    # turn = int(input("Kto zaczyna? 1. Gracz 2. Komputer"))

    while board.avaiable:
        board.player_turn()

        if (board.winner):
            board.print_winner()
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        board.print_board()
        board.computer_turn()

        if (board.winner):
            board.print_winner()
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        board.print_board()



