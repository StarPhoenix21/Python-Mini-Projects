import random


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


def hangman():
    word = random.choice(["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream"])
    validletter = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            break
        print("Guess the word:", main)
        guess = input().casefold()

        if guess in validletter:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            continue
        if guess not in word:
            turns = turns - 1

        print(display_hangman(10 - turns))

        if turns == 0:
            print("Game Over! The word was:", word)
            break


name = input("Enter your name: ")
print(f"Welcome {name}")
print("=====================")
print("Try to guess it in less than 10 attempts")
hangman()
print()
