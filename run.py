import random
from words import easy_words, medium_words, hard_words

# ANSI escape codes for colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'


def display_game(tries, word_completion):
    """ Displays game and is called in the play(word) function """
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

def get_word(difficulty):
    """ Gets imported list of easy, medium and hard words and returns it as uppercase """
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
    """ Chosses difficulty level of word """
    print("Let's play hangman")
    while True:
        level = input("Choose difficulty level (easy, medium, hard):").lower()
        if level in ["easy", "medium", "hard"]:
            return level
        else:
            print("Invalid choice. Please choose easy, medium, or hard.")

def play(word):
    """ This section holds structure of the game with nested if statements within while loop """
    word_completion = '_ ' * len(word)  
    guessed = False
    guessed_letters = [] # creates empty list for guessed characters
    guessed_words = [] # creates empty list for guessed words
    tries = 6 # number of tries for user which relates to hangman image
    
    display_game(tries, word_completion) # Call game images at start of game
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(colors.GREEN + "Good job," + colors.END, guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print(colors.GREEN + "Congrats, you guessed the word! You win!" + colors.END)
    else:
        print(colors.RED + "Sorry, you ran out of tries. The word was " + colors.END + colors.BLUE + word + colors.END + colors.RED + ". Maybe next time!" + colors.END)
        
def display_hangman(tries):
    """ reveals the hangman based on the number of tries """
    stages = [  """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     / \\
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     /
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |      |
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |
            |
            |
            ---
            """,
        """
            --------
            |      |
            |
            |
            |
            |
            ---
            """,
    ]
    
    return stages[tries] 
    

def main():
    difficulty = choose_difficulty()
    word = get_word(difficulty)
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        difficulty = choose_difficulty()
        word = get_word(difficulty)
        play(word)
        
if __name__ == "__main__":
    main()