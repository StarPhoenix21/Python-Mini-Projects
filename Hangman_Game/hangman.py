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
    return stages[min(attempts, len(stages) - 1)]


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
    correct_guess = False

    # Check each character and update display_word accordingly
    for i, letter in enumerate(word):
        if i < len(guess) and guess[i] == letter:
            display_word[i] = letter
            correct_guess = True

    if not correct_guess:
        wrong_attempts += 1
        print(f"Wrong! You have {max_attempts - wrong_attempts} attempts left.")

    return display_word, guessed_words, wrong_attempts


def give_hint(hint, hint_used):
    """
    Provides a hint to the player if not already used.
    """
    if hint_used:
        print("You have already used your hint!")
    else:
        print(f"Hint: {hint}")
        hint_used = True
    return hint_used


def try_again():
    """
    Asks the player if they want to play again.
    """
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            print("Thanks for playing! Goodbye.")
            return False
        else:
            print("Please answer 'yes' or 'no'.")


def hangman():
    """
    Main function to run the hangman game.
    """
    chosen_word_info = choose_word(word_list)  # Choose a random word
    word = chosen_word_info["word"]
    hint = chosen_word_info["hint"]
    max_attempts = 10
    display_word, wrong_attempts, guessed_words = initialize_game(word)
    hint_used = False

    while wrong_attempts < max_attempts:
        print(display_hangman(wrong_attempts))  # Display hangman diagram
        print("Word: " + " ".join(display_word))  # Display the current state of the word
        guess = input("Guess the word or type 'hint' for a hint: ").lower()  # Get the player's guess

        if guess == "hint":
            hint_used = give_hint(hint, hint_used)
        elif guess.isalpha():  # Validate input
            if guess in guessed_words:
                print("You already guessed that word.")
            else:
                display_word, guessed_words, wrong_attempts = update_game_state(
                    guess, word, display_word, guessed_words, wrong_attempts, max_attempts)
        else:
            print("Invalid input. Please guess a word or type 'hint'.")

        if "_" not in display_word:  # Check if the word is completely guessed
            print(f"Congratulations! You guessed the word: {''.join(display_word)}")
            break
    else:
        print(display_hangman(wrong_attempts))  # Display final hangman diagram
        print(f"Game Over! The word was: {word}")


# Main game loop
playing = True
while playing:
    name = input("Enter your name: ")
    print(f"Welcome {name}")
    print("=====================")
    print("Try to guess the word in less than 10 attempts")
    hangman()
    playing = try_again()

