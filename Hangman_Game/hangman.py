import random
from words import word_list  # Import the word list


def display_hangman(attempts):
    """
    Returns the hangman diagram based on the number of wrong attempts.
    """
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """,
    ]
    return stages[attempts]


def choose_word(word_list):
    """
    Chooses a random word from the word list.
    """
    return random.choice(word_list)


def initialize_game(word):
    """
    Initializes the game state with underscores for the word,
    zero wrong attempts, and an empty list of guessed words.
    """
    return ["_"] * len(word), 0, []


def update_game_state(guess, word, display_word, guessed_words, wrong_attempts, max_attempts):
    """
    Updates the game state based on the player's guess.
    """
    guessed_words.append(guess)
    if guess == word:
        display_word = list(word)

    else:
        wrong_attempts += 1
        print(f"Wrong! You have {max_attempts - wrong_attempts} attempts left.")

    return display_word, guessed_words, wrong_attempts


def hangman():
    """
    Main function to run the hangman game.
    """
    word = choose_word(word_list)  # Choose a random word
    max_attempts = 10
    display_word, wrong_attempts, guessed_words = initialize_game(word)

    while wrong_attempts < max_attempts:
        print(display_hangman(wrong_attempts))  # Display hangman diagram
        print("Word: " + " ".join(display_word))  # Display the current state of the word
        guess = input("Guess the word: ").lower()  # Get the player's guess

        if guess.isalpha():  # Validate input
            if guess in guessed_words:
                print("You already guessed that word.")
            else:
                display_word, guessed_words, wrong_attempts = update_game_state(
                    guess, word, display_word, guessed_words, wrong_attempts, max_attempts)
        else:
            print("Invalid input. Please guess a word.")

        if "_" not in display_word:  # Check if the word is completely guessed
            print(f"Congratulations! You guessed the word: {''.join(display_word)}")
            break
    else:
        print(display_hangman(wrong_attempts))  # Display final hangman diagram
        print(f"Game Over! The word was: {word}")


# Get player's name and start the game
name = input("Enter your name: ")
print(f"Welcome {name}")
print("=====================")
print("Try to guess the word in less than 10 attempts")
hangman()
print()
