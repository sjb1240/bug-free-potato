import random

in_progress_arr = []
wrong_guesses = 0


def random_line(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)


def create_array(word):
    global in_progress_arr
    for i in range(len(word)):
        in_progress_arr.append("_")
    return in_progress_arr


def guess():
    guess = input("Please guess a letter: ").lower()

    while not guess.isalpha() or len(guess) != 1:
        if not guess.isalpha():
            print("Thats not a letter!")
        elif len(guess) != 1:
            print("You can only guess one letter at a time!")
        guess = input("Please guess a letter: ").lower()
    else:
        print("You guessed:", guess)
    return guess


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def check_guess(letter, word):
    if letter not in word:
        return False
    else:
        positions = findOccurrences(word, letter)
        return positions


def play_again():
    global in_progress_arr
    global wrong_guesses
    print("Would you like to play again?")
    again = input("Please select (Y/y) or (N/n) ").lower()
    while again != "y" and again != "n":
        print("Thats not a valid option...")
        again = input("Please select (Y/y) or (N/n) ").lower()
    else:
        if again == "y":
            in_progress_arr.clear()
            wrong_guesses = 0
            return True
        elif again == "n":
            return False


def main():
    global in_progress_arr
    global wrong_guesses
    guessed_letters = []
    print("Welcome To Hangman!")
    # hardcoded for now, will change later
    secret_word = random_line("wordlist.txt")
    in_prog = create_array(secret_word)

    print("Your word has", len(in_prog), "letters", in_prog)
    done = False
    turn_count = 0
    while wrong_guesses != 10 and done == False:
        guessed_letter = guess()
        if guessed_letter not in guessed_letters:
            checked_guess = check_guess(guessed_letter, secret_word)
            if checked_guess == False:
                wrong_guesses += 1
                print("Thats not right! You have", 10 -
                      wrong_guesses, "wrong guesses remaining!")
            else:
                print("Great Guess!")
                for pos in checked_guess:
                    in_prog[pos] = guessed_letter
            turn_count += 1
            print(in_prog)
            if "_" in in_prog:
                done = False
            else:
                done = True
                print("DONE!")
                print("Completed in ", turn_count, "guesses")
        else:
            print("You've already guessed that!")
            print("Try Again")
        guessed_letters.append(guessed_letter)
    else:
        print("The word was: ", secret_word)

    pa = play_again()
    if pa == True:
        main()
    if pa == False:
        print("Thanks for playing!")
        print("Goodbye!")


if __name__ == "__main__":
    main()
