import random
from words import word_list  # Import the word list


# Function to display the hangman diagram based on the number of wrong attempts
def display_hangman(attempts):
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

# Main function to run the hangman game
def hangman():
    # Choose a random word from the word list
    word = random.choice(word_list)
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guess_made = ''
    display_word = ["_"] * len(word)  # Initialize display word with underscores

    while turns > 0:
        print(display_hangman(10 - turns))  # Display hangman diagram
        print("Word: " + " ".join(display_word))  # Display the current state of the word
        guess = input("Guess the word: ").lower()  # Get the player's guess

        if guess.isalpha():  # Check if the guess is a valid word
            if guess in guess_made:
                print("You already guessed that word.")
            else:
                guess_made += guess  # Add the guess to guessed words
                if guess == word:  # Check if the guess is correct
                    display_word = list(word)
                    break
                else:
                    turns -= 1  # Decrease the number of attempts
                    print(f"Wrong! You have {turns} attempts left.")
        else:
            print("Invalid input. Please guess a word.")

        if "_" not in display_word:  # Check if the word is completely guessed
            print("Congratulations! You guessed the word: " + word)
            break
    else:
        print(display_hangman(10 - turns))  # Display final hangman diagram
        print("Game Over! The word was: " + word)  # Reveal the word


# Get player's name and start the game
name = input("Enter your name: ")
print(f"Welcome {name}")
print("=====================")
print("Try to guess the word in less than 10 attempts")
hangman()
print()
