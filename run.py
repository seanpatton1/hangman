""" all imports for game """
import random
import time
import os
from words import easy_words, medium_words, hard_words


class ColorsGame:
    """ ANSI escape codes for ColorsGame """
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def game_title():
    """ Hangman title """
    os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal
    time.sleep(0.1)
    print("HANGMAN".center(80, "-"))
    print("\n")


def welcome_message():
    """ Welcome message and option for user to read instructions
        before beginning the game.
    """

    # Print game title
    game_title()

    # Welcome message

    instructions = ("In Hangman, the goal is to guess the hidden word one "
                    "letter at a time before \nthe hangman figure is fully "
                    "drawn. \nCorrect guesses reveal letters in the word, while "
                    "incorrect guesses add parts\nto the hangman.\nThe game is "
                    "won by revealing the entire word before the hangman is "
                    "completed.\n")
    start_one = input(ColorsGame.GREEN + "Welcome! Before we begin the game,\n"
                      "would you like to see the instructions? (Y/N):\n" +
                      ColorsGame.END).upper()
    if start_one == 'Y':
        print(ColorsGame.CYAN + instructions + ColorsGame.END)


def display_game(tries, word_completion, guessed_letters):
    """ Displays game and is called in the play(word) function and
        the guessed letters
    """
    print(display_hangman(tries))
    print(word_completion)
    print(ColorsGame.GREEN + "Guessed letters: " + ColorsGame.END + ", "
          .join(guessed_letters))
    print("\n")


def get_word(difficulty):
    """ Gets imported list of easy, medium and hard words
        and returns it as uppercase
    """
    if difficulty == "easy":
        word = random.choice(easy_words)
    elif difficulty == "medium":
        word = random.choice(medium_words)
    elif difficulty == "hard":
        word = random.choice(hard_words)
    else:
        raise ValueError("Invalid difficulty level")
    return word.upper()


def choose_difficulty():
    """ Chooses difficulty level of word """
    print(ColorsGame.BLUE + "Let's play hangman\n" + ColorsGame.END)
    while True:
        level = input(ColorsGame.CYAN + "Choose difficulty level "
                      "(easy, medium, hard):\n" + ColorsGame.END).lower()
        if level in ["easy", "medium", "hard"]:
            return level
        else:
            print(ColorsGame.RED + "Invalid choice. Please choose easy, medium, "
                  "or hard." + ColorsGame.END)


def play(word):
    """ This section holds structure of the game
        with nested if statements within while loop
    """
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []  # creates empty list for guessed characters
    guessed_words = []  # creates empty list for guessed words
    tries = 6  # number of tries for user which relates to hangman image

    # Call game images at start of game
    display_game(tries, word_completion, guessed_letters)

    while not guessed and tries > 0:
        guess = input(ColorsGame.BLUE + "Please guess a letter or word:\n" +
                      ColorsGame.END).upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(ColorsGame.RED + "You already guessed the letter" +
                      ColorsGame.END, ColorsGame.BLUE + guess + ColorsGame.END)
            elif guess not in word:
                print(guess, ColorsGame.RED + "is not in the word" + ColorsGame.END)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(ColorsGame.GREEN + "Good job," + ColorsGame.END, ColorsGame.BLUE +
                      guess + ColorsGame.END, ColorsGame.GREEN + "is in the word" +
                      ColorsGame.END)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(ColorsGame.RED + "You already guessed the word" + ColorsGame.RED,
                      ColorsGame.BLUE + guess + ColorsGame.END)
            elif guess != word:
                print(guess, ColorsGame.RED + "is not in the word." + ColorsGame.END)
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
        display_game(tries, word_completion, guessed_letters)
    if guessed:
        print(ColorsGame.GREEN + "Congrats, you guessed the word! You win!" +
              ColorsGame.END)
    else:
        print(ColorsGame.RED + "Sorry, you ran out of tries. The word was " +
              ColorsGame.END + ColorsGame.BLUE + word + ColorsGame.END + ColorsGame.RED +
              ". Maybe next time!" + ColorsGame.END)


def display_hangman(tries):
    """ reveals the hangman based on the number of tries """
    stages = [ColorsGame.YELLOW + stage + ColorsGame.END for stage in ["""
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     / \\
            ---
            """, """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     /
            ---
            """, """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |
            ---
            """, """
            --------
            |      |
            |      o
            |     \\|
            |      |
            |
            ---
            """, """
            --------
            |      |
            |      o
            |      |
            |      |
            |
            ---
            """, """
            --------
            |      |
            |      o
            |
            |
            |
            ---
            """, """
            --------
            |      |
            |
            |
            |
            |
            ---
            """, ]]

    return stages[tries]


def main():
    """ Main function containing game functions """
    game_title()
    welcome_message()
    difficulty = choose_difficulty()
    word = get_word(difficulty)
    play(word)
    #  Code to allow user to play again
    while True:
        play_again = input(ColorsGame.GREEN + "Play Again? (Y/N):\n" + ColorsGame.END).upper()
        if play_again in ['Y', 'N']:
            if play_again == 'Y':
                difficulty = choose_difficulty()
                word = get_word(difficulty)
                play(word)
            else:
                print(ColorsGame.GREEN + "Thanks for playing! Goodbye!" + ColorsGame.END)
                break
        else:
            print(ColorsGame.RED + "Invalid input. Please enter Y or N." + ColorsGame.END)


if __name__ == "__main__":
    main()
