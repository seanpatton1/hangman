import random
from words import easy_words, medium_words, hard_words

def welcome_message(tries, word_completion):
    print("Let's play hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

def get_word(difficulty):
    """gets random words from imported list and returns it as uppercase"""
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
    """ Chosses difficulty level of word"""
    while True:
        level = input("Choose difficulty level (easy, medium, hard):").lower()
        if level in ["easy", "medium", "hard"]:
            return level
        else:
            print("Invalid choice. Please choose easy, medium, or hard.")

def play(word):
    """ This section holds structure of the game with nested if statements within while loop"""
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = [] # creates empty list for guessed characters
    guessed_words = [] # creates empty list for guessed words
    tries = 6 # number of tries for user which relates to hangman image
    
    welcome_message(tries, word_completion) # Call welcome message at start of game
    
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
                print("Good job,", guess, "is in the word")
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
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        
def display_hangman(tries):
    """ 
    reveals the hangman based on the number of tries
    
    """
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