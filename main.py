"""
Connect-4/main.py

Main script for Connect 4

Author: Nathan "Nathcat" Baines
Date: 13/07/2021
"""

import sys


class Game:  # Stores game data, probably not entirely necessary
    def __init__(self):
        self.current_player_token = "O"

    def turn(self):  # Toggle the current player token
        if self.current_player_token == "X":
            self.current_player_token = "O"
        else:
            self.current_player_token = "X"


class Column:  # Holds the data for a column on the board
    def __init__(self):
        self.rows = [char for char in ' ' * 6]  # Create a column

    def add(self, obj):  # Add obj to the bottom (end) of the column
        for x in range(len(self.rows)):
            if self.rows[x] != ' ':
                if (x - 1) != -1:
                    self.rows[x - 1] = obj
                    return True

                else:
                    print("\n\nCannot add to this column!")
                    return False
            else:
                if self.rows == [char for char in ' ' * 6]:
                    self.rows[len(self.rows) - 1] = obj
                    return True

    def check_win_in_column(self, obj):  # Check if player 'obj' has won in this column
        count = 0
        for x in range(len(self.rows)):
            if self.rows[x] == obj:
                count += 1
            else:
                count = 0

            if count >= 4:
                return True

        return False


def check_win(obj):  # Checks if player 'obj' has won
    # Check for win in columns.
    for column in board:
        result = column.check_win_in_column(obj)
        if result:
            print(f"\n\nPlayer {obj} has won!")
            sys.exit()

    # Check for win in rows.
    # First, compile the rows
    rows = []
    for row_index in range(len(board[0].rows)):
        row = []
        for column_index in range(len(board)):
            row.append(board[column_index].rows[row_index])

        rows.append(row)

    # Now check each row for a win with obj.
    for row in rows:
        count = 0
        for col in row:
            if col == obj:
                count += 1
            else:
                count = 0

            if count >= 4:
                print(f"\n\nPlayer {obj} has won!")
                sys.exit()

    # Check for win in diagonals.
    # First, we need to compile the diagonals
    diagonals = []

    # Iterate backwards through the first row, and get the diagonals
    # coming off of each column, then iterate down the first column, and get the
    # diagonals coming off each row, excluding the first row.

    for col_index in range(len(rows[0]) - 1, -1, -1):
        diagonal = []
        length_of_diagonal = len(rows) - col_index
        for diagonal_index in range(length_of_diagonal):
            diagonal.append(rows[0 + diagonal_index][col_index + diagonal_index])

        diagonals.append(diagonal)

    for row_index in range(len(board[0].rows)):
        diagonal = []
        length_of_diagonal = len(board) - (row_index + 1)
        for diagonal_index in range(length_of_diagonal):
            diagonal.append(board[0 + diagonal_index].rows[row_index + diagonal_index])

        diagonals.append(diagonal)

    # And now that suffering is over and done with, lets check the diagonals
    # for a win.

    # Oh ffs wait it's not over yet, we also need to check the diagonals in the
    # other direction... :(
    # I guess I'll just reverse both iteration statements and hope for the best
    # lol.

    for col_index in range(len(rows[0])):
        diagonal = []
        length_of_diagonal = (len(rows) - 5) + col_index

        if length_of_diagonal == 7:  # IDK it's weird
            length_of_diagonal = 6

        for diagonal_index in range(length_of_diagonal):
            diagonal.append(rows[0 + diagonal_index][col_index - diagonal_index])

        diagonals.append(diagonal)

    for row_index in range(len(board[len(board) - 1].rows) - 1, -1, -1):
        diagonal = []
        length_of_diagonal = len(board) - (row_index + 1)
        for diagonal_index in range(length_of_diagonal):
            diagonal.append(board[(len(board) - 1) - diagonal_index].rows[row_index + diagonal_index])

        diagonals.append(diagonal)

    # Okay I think we're good to go now.

    for diagonal in diagonals:
        count = 0
        for val in diagonal:
            if val == obj:
                count += 1
            else:
                count = 0

            if count >= 4:
                print(f"\n\nPlayer {obj} has won!")
                sys.exit()


def display_board():  # Display the board
    print(" 1 2 3 4 5 6 7")

    for y in range(len(board[0].rows)):
        row = "|"
        for x in range(len(board)):
            row += board[x].rows[y] + "|"

        print(row)

    print("===============")


board = [Column() for x in range(7)]  # Build the board

game = Game()  # Instantiate Game class

response = True  # Stores response from Column.add(), define here so the start
# of the loop doesn't throw an error.

while True:  # Main program loop
    if response:  # If the player's token was added to the column successfully
        game.turn()
        check_win(game.current_player_token)
        print("\n\n")

    print(f"Player {game.current_player_token}'s turn-------------")

    display_board()

    column_choice = int(input("\nEnter column > ")) - 1  # Get the player's
    # choice of column.

    # Attempt to add the player's token to the column they chose
    response = board[column_choice].add(game.current_player_token)

    check_win(game.current_player_token)
