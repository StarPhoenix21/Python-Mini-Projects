
import random
import time
from words import word_list  # Import the word list


class HangmanGame:
    """
    A class to represent a Hangman game.
    """

    def __init__(self):
        """
        Initialize the Hangman game with a word list, statistics, and leaderboard.
        """
        self.word_list = word_list.copy()  # Copy the initial word list
        self.statistics = {"games_played": 0, "games_won": 0, "games_lost": 0, "total_time": 0}
        self.leaderboard = []

    def display_hangman(self, attempts):
        """
        Display the hangman graphic based on the number of wrong attempts.

        Parameters:
        attempts (int): The number of wrong attempts

        Returns:
        str: The hangman graphic corresponding to the attempts
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

    def add_custom_words(self):
        """
        Allow the user to add custom words and hints to the word list.
        """
        while True:
            add_word = input("Do you want to add a custom word? (yes/no): ").lower()
            if add_word == "yes":
                word = input("Enter the word: ").lower()
                hint = input("Enter the hint: ").lower()
                self.word_list.append({"word": word, "hint": hint})
                print("Custom word added!")
            elif add_word == "no":
                break
            else:
                print("Please answer 'yes' or 'no'.")

    def choose_word(self):
        """
        Choose a random word from the word list.

        Returns:
        dict: A dictionary containing the chosen word and its hint
        """
        return random.choice(self.word_list)

    def initialize_game(self, word):
        """
        Initialize the game state.

        Parameters:
        word (str): The word to be guessed

        Returns:
        tuple: A tuple containing the display word list, wrong attempts count, guessed words list, and hint usage flag
        """
        return ["_"] * len(word), 0, [], False

    def update_game_state(self, guess, word, display_word, guessed_words, wrong_attempts, max_attempts):
        """
        Update the game state based on the player's guess.

        Parameters:
        guess (str): The player's guessed word or letter
        word (str): The word to be guessed
        display_word (list): The current state of the word being displayed
        guessed_words (list): The list of words guessed by the player
        wrong_attempts (int): The number of wrong attempts made by the player
        max_attempts (int): The maximum number of wrong attempts allowed

        Returns:
        tuple: A tuple containing the updated display word list, guessed words list, and wrong attempts count
        """
        guessed_words.append(guess)
        correct_guess = False

        if guess == word:
            display_word = list(word)
            correct_guess = True
        else:
            for i, letter in enumerate(word):
                if i < len(guess) and guess[i] == letter:
                    display_word[i] = letter
                    correct_guess = True

        if not correct_guess:
            wrong_attempts += 1
            print(f"Wrong! You have {max_attempts - wrong_attempts} attempts left.")

        return display_word, guessed_words, wrong_attempts

    def give_hint(self, hint, hint_used):
        """
        Provide a hint to the player.

        Parameters:
        hint (str): The hint for the current word
        hint_used (bool): A flag indicating if a hint has already been used

        Returns:
        bool: Updated hint usage flag
        """
        if hint_used:
            print("You have already used your hint!")
            return hint_used

        print(f"Hint: {hint}")
        return True

    def try_again(self):
        """
        Ask the player if they want to play again.

        Returns:
        bool: True if the player wants to play again, False otherwise
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

    def update_statistics(self, won, time_taken):
        """
        Update the game statistics.

        Parameters:
        won (bool): A flag indicating if the player won the game
        time_taken (float): The time taken to complete the game
        """
        self.statistics["games_played"] += 1
        self.statistics["total_time"] += time_taken
        if won:
            self.statistics["games_won"] += 1
        else:
            self.statistics["games_lost"] += 1

    def display_statistics(self):
        """
        Display the game statistics.
        """
        print("\nStatistics:")
        print(f"Games Played: {self.statistics['games_played']}")
        print(f"Games Won: {self.statistics['games_won']}")
        print(f"Games Lost: {self.statistics['games_lost']}")
        if self.statistics["games_played"] > 0:
            avg_time = self.statistics["total_time"] / self.statistics["games_played"]
            print(f"Average Time: {avg_time:.2f} seconds")

    def sort_key(self, entry):
        """
        Define a custom sort key for sorting the leaderboard.

        Parameters:
        entry (dict): A dictionary containing leaderboard entry details

        Returns:
        tuple: A tuple used for sorting the leaderboard
        """
        return (entry["won"], entry["time"])

    def update_leaderboard(self, name, won, time_taken):
        """
        Update the leaderboard with the player's performance.

        Parameters:
        name (str): The player's name
        won (bool): A flag indicating if the player won the game
        time_taken (float): The time taken to complete the game
        """
        self.leaderboard.append({"name": name, "won": won, "time": time_taken})
        # Sort using the custom sort_key function
        self.leaderboard.sort(key=self.sort_key, reverse=True)

    def display_leaderboard(self):
        """
        Display the leaderboard.
        """
        print("\nLeaderboard:")
        for entry in self.leaderboard:
            status = "Won" if entry["won"] else "Lost"
            print(f"{entry['name']}: {status} in {entry['time']:.2f} seconds")

    def main(self):
        """
        The main function to run the Hangman game.
        """
        playing = True
        players = []
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            player_name = input(f"Enter the name of player {i + 1}: ")
            players.append(player_name)

        multiplayer = True if num_players > 1 else False

        if multiplayer:
            print(f"Welcome {' and '.join(players)} to Multiplayer Hangman!")
        else:
            name = players[0]
            print(f"Welcome {name} to Single Player Hangman!")

        print("=====================")
        print("Try to guess it in less than 10 attempts")

        self.add_custom_words()  # Allow the user to add custom words

        current_player_index = 0

        while playing:
            current_player = players[current_player_index]
            print(f"\n{current_player}'s turn!")

            chosen_word_info = self.choose_word()
            chosen_word = chosen_word_info["word"]
            hint = chosen_word_info["hint"]
            display_word, wrong_attempts, guessed_words, hint_used = self.initialize_game(chosen_word)
            max_attempts = 10

            start_time = time.time()

            while wrong_attempts < max_attempts:
                print(self.display_hangman(wrong_attempts))
                print(f"Word: {' '.join(display_word)}")
                print(f"Guessed Words: {', '.join(guessed_words)}")
                guess = input(f"{current_player}, guess the word or type 'hint' for a hint: ").lower()

                # Handle the hint request
                if guess == 'hint':
                    hint_used = self.give_hint(hint, hint_used)
                    continue

                # Validate input to ensure it's a valid guess
                if not guess.isalpha():
                    print("Invalid input. Please guess a word.")
                    continue

                display_word, guessed_words, wrong_attempts = self.update_game_state(
                    guess, chosen_word, display_word, guessed_words, wrong_attempts, max_attempts
                )

                if "_" not in display_word:
                    end_time = time.time()
                    time_taken = end_time - start_time
                    print(f"Congratulations {current_player}! You guessed the word: {''.join(display_word)}")
                    self.update_statistics(won=True, time_taken=time_taken)
                    self.update_leaderboard(current_player, won=True, time_taken=time_taken)
                    break
                else:
                    current_player_index = (current_player_index + 1) % num_players
                    current_player = players[current_player_index]
                    print(f"\n{current_player}'s turn!")

            if "_" in display_word:
                end_time = time.time()
                time_taken = end_time - start_time
                print(self.display_hangman(wrong_attempts))
                print(f"Game Over! The word was: {chosen_word}")
                self.update_statistics(won=False, time_taken=time_taken)
                self.update_leaderboard(players[current_player_index], won=False, time_taken=time_taken)

            current_player_index = (current_player_index + 1) % num_players
            playing = self.try_again()

        self.display_statistics()
        self.display_leaderboard()


if __name__ == "__main__":
    game = HangmanGame()
    game.main()
