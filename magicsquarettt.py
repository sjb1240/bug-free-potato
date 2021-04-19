import ttt
import numpy as np
import random as r
import itertools as it

number_of_turns = 0
winner = None
playerSymbol = 'X'
computerSymbol = 'O'
player = 1
computer = 0
magic_dict = {1: 8, 2: 1, 3: 6, 4: 3, 5: 5, 6: 7, 7: 4, 8: 9, 9: 2}
position_dict = {8: [0, 0], 1: [0, 1], 6: [0, 2], 3: [1, 0],
                 5: [1, 1], 7: [1, 2], 4: [2, 0], 9: [2, 1], 2: [2, 2]}
moves_made = 0
player_values = []
computer_values = []
total_guessed = []


def initializeBoard():
    return np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])


def player1():
    global playerSymbol, computerSymbol, player
    who_goes_first = r.randint(0, 1)
    player = who_goes_first
    if who_goes_first == 1:
        computerSymbol = 'X'
        playerSymbol = 'O'
    return player


def updateBoard(board):
    global player_values, computer_values, player, playerSymbol, computerSymbol, position_dict
    for value in player_values:
        row, col = position_dict[value][0], position_dict[value][1]
        board[row][col] = playerSymbol
    for value in computer_values:
        row, col = position_dict[value][0], position_dict[value][1]
        board[row][col] = computerSymbol


def convertMove(position):
    global magic_dict
    return magic_dict[position]


def checkWin(iterable, player):
    global winner
    combinations = list(it.combinations(iterable, 3))
    my_sum = list(map(sum, combinations))
    if 15 not in my_sum:
        return False

    winner = player
    return


def check(guess):
    global total_guessed
    if guess in list(total_guessed):
        # print("That value has been taken already")
        print(False)
        return False
    else:
        print(True)
        return True


def playerMove():
    global player_values, total_guessed, moves_made
    pos = input("\nPlease enter a the spot you would like: (1-9)")
    while not pos.isdigit():
        pos = input("\n Please enter a number between 1 and 9")
    else:
        pos = int(pos)
        while pos not in range(1, 10):
            print("\nPlease enter a number between 1 and 9 (LEVEL 2 OF THE LOOP)")
            pos = input("\n(1-9):")
        else:
            pos = int(pos)
            while not check(pos):
                print('pos:', pos)
                pos = int(input("\nThat spot's taken, try again!"))
            else:
                pos = int(pos)
                print('pos:', pos)
                total_guessed.append(pos)
                player_values.append(convertMove(pos))
                moves_made += 1


def computerMove():
    global computer_values, total_guessed, moves_made
    pos = r.randint(1, 9)
    while not check(pos):
        pos = r.randint(1, 9)
        print("CPU Trying Again")
    else:
        total_guessed.append(pos)
        computer_values.append(convertMove(pos))
    moves_made += 1


def player_turn_sequence(board):
    playerMove()
    updateBoard(board)
    ttt.printBoard(board)


def computer_turn_sequence(board):
    computerMove()
    updateBoard(board)
    ttt.printBoard(board)


def magicSquare():
    global magic_dict, player_values, computer_values, winner, total_guessed
    # magic_square = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    # num_board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # ttt.printBoard(num_board)
    board = initializeBoard()
    ttt.printBoard(board)
    first_move = 0

    if first_move == 1:
        print("\nComputer Goes First")
    else:
        print("\nYou go first")
    while winner is None:
        if moves_made < 3:
            if first_move == 1:
                computer_turn_sequence(board)
                player_turn_sequence(board)
            else:
                player_turn_sequence(board)
                computer_turn_sequence(board)
        elif moves_made <= 9:
            while moves_made >= 3 and moves_made <= 9:
                if first_move == 1:
                    computer_turn_sequence(board)
                    checkWin(computer_values, "computer")

                    player_turn_sequence(board)
                    checkWin(player_values, 'player')
                else:
                    player_turn_sequence(board)
                    checkWin(player_values, 'player')

                    computer_turn_sequence(board)
                    checkWin(computer_values, "computer")
        else:
            break
    else:
        print("Winner: ", winner)


if __name__ == "__main__":
    print("Lets Play Tic-Tac-Toe!")
    magicSquare()
