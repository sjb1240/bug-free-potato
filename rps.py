import random as r
options = {0: "Rock", 1: "Paper", 2: "Scissors", 5: "Tie"}


def oponent():
    move = r.randint(0, 2)
    return options[move], move


def check_moves(move1, move2):
    if move1 == move2:
        return 5
    elif move1 == 0:
        if move2 == 1:
            return 1
        else:
            return 0
    elif move1 == 1:
        if move2 == 0:
            return 1
        else:
            return 2
    elif move1 == 2:
        if move2 == 0:
            return 0
        else:
            return 2


def understand_results(result):
    options[result]


def main():
    op_move, op_pos = oponent()
    user_hand = input("(R)ock (P)aper or (S)cissors: ").lower()
    while user_hand not in ["r", "p", "s"]:
        print("That isn't a valid move")
        user_hand = input("Try Again: (R)ock (P)aper or (S)cissors: ").lower()
    else:
        if user_hand == "p":
            user_move = 1
        elif user_hand == "r":
            user_move = 0
        else:
            user_move = 2
        winning_move = check_moves(user_move, op_pos)
        print("Your move has been recorded as", options[user_move])
        print("Your opponents move has been recorded as:", op_move, "")
        print("And the winner is:")
        print("...")
        if winning_move == 5:
            print("Its a Tie!")
        elif winning_move == user_move:
            print(options[winning_move], "Congratulations!")
        else:
            print(options[winning_move])
            print("You Lose :P")
        print("Would you like to play again?")
        play_again = input("(Y/y) or (N/n) ").lower()
        while play_again not in ["y", "n"]:
            print("Thats not a valid option")
            play_again = input("(Y/y) or (N/n) ").lower()
        else:
            if play_again == "y":
                main()
            else:
                print("Goodbye")


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    print("To begin please select:")
    main()
    print("Thanks for playing!")
