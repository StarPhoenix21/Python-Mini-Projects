import random
import time
from words import word_list  # Import the default word list


class HangmanGame:
    def __init__(self, word_list):
        """
        Initializes the HangmanGame class with a word list.

        Parameters:
            word_list (list): List of words with hints to use in the game.
        """
        self.word_list = word_list
        self.word = ""
        self.hint = ""
        self.display_word = []
        self.wrong_attempts = 0
        self.guessed_words = []
        self.hint_used = False
        self.max_attempts = 10
        self.start_time = 0
        self.statistics = {"games_played": 0, "games_won": 0, "games_lost": 0, "total_time": 0}
        self.leaderboard = []

    def display_hangman(self, attempts):
        """
        Returns the current hangman stage based on the number of wrong attempts.

        Parameters:
            attempts (int): Number of wrong attempts made by the player.

        Returns:
            str: The current stage of the hangman.
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

    def choose_word(self, word_list):
        """
        Chooses a word and hint randomly from the word list and initializes the game state.

        Parameters:
             word_list (list): List of words with hints to use in the game.
        """
        chosen_word_info = random.choice(word_list)
        self.word = chosen_word_info["word"]
        self.hint = chosen_word_info["hint"]
        self.display_word, self.wrong_attempts, self.guessed_words = self.initialize_game(self.word)
        self.hint_used = False
        self.start_time = time.time()

    def initialize_game(self, word):
        """
        Initializes the game state for a new word.

        Parameters:
            word (str): The word to be guessed.

        Returns:
            list: A list of underscores representing the word to be guessed.
            int: Initial number of wrong attempts (0).
            list: Initial list of guessed words (empty).
        """
        return ["_"] * len(word), 0, []

    def update_game_state(self, guess):
        """
        Updates the game state based on the player's guess.

        Parameters:
            guess (str): The player's guessed letter or word.
        """
        self.guessed_words.append(guess)
        correct_guess = False

        if guess == self.word:
            self.display_word = list(self.word)
            correct_guess = True
        elif len(guess) == 1:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display_word[i] = letter
                    correct_guess = True

        if not correct_guess:
            self.wrong_attempts += 1
            print(f"Wrong! You have {self.max_attempts - self.wrong_attempts} attempts left.")
        else:
            print("Correct!")

    def give_hint(self):
        """
        Provides a hint for the current word if the hint has not been used yet.
        """
        if self.hint_used:
            print("You have already used your hint!")
        else:
            print(f"Hint: {self.hint}")
            self.hint_used = True

    def game_won(self):
        """
        Checks if the game is won.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        return "_" not in self.display_word

    def game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.wrong_attempts >= self.max_attempts

    def update_statistics(self, won, time_taken):
        """
        Updates the game statistics based on the game result.

        Parameters:
            won (bool): True if the player won, False otherwise.
            time_taken (float): Time taken to complete the game in seconds.
        """
        self.statistics["games_played"] += 1
        self.statistics["total_time"] += time_taken
        if won:
            self.statistics["games_won"] += 1
        else:
            self.statistics["games_lost"] += 1

    def display_statistics(self):
        """
        Displays the game statistics.
        """
        print("\nStatistics:")
        print(f"Games Played: {self.statistics['games_played']}")
        print(f"Games Won: {self.statistics['games_won']}")
        print(f"Games Lost: {self.statistics['games_lost']}")
        if self.statistics["games_played"] > 0:
            avg_time = self.statistics["total_time"] / self.statistics["games_played"]
            print(f"Average Time: {avg_time: .2f} seconds")

    def sort_key(self, entry):
        """
        Key function for sorting leaderboard entries.

        Parameters:
            entry (dict): A leaderboard entry with 'name', 'won', and 'time' keys.

        Returns:
            tuple: Sorting key (won status, negative time).
        """
        return entry["won"], -entry["time"]

    def update_leaderboard(self, name, won, time_taken):
        """
        Updates the leaderboard with the player's game result.

        Parameters:
            name (str): The player's name.
            won (bool): True if the player won, False otherwise.
            time_taken (float): Time taken to complete the game in seconds.
        """
        self.leaderboard.append({"name": name, "won": won, "time": time_taken})
        self.leaderboard.sort(key=self.sort_key, reverse=True)

    def display_leaderboard(self):
        """
        Displays the leaderboard.
        """
        print("\nLeaderboard:")
        for entry in self.leaderboard:
            status = "Won" if entry["won"] else "Lost"
            print(f"{entry['name']}: {status} in {entry['time']:.2f} seconds")

    def get_custom_word_list(self):
        """
        Prompts the player to enter a custom word list.

        Returns:
            list: Custom word list entered by the player.
        """
        custom_word_list = []
        while True:
            word = input("Enter a word (or 'done' to finish): ").lower()
            if word == 'done':
                break
            hint = input("Enter a hint for this word: ").lower()
            custom_word_list.append({"word": word, "hint": hint})
        return custom_word_list

    def try_again(self):
        """
        Prompts the player to decide whether to play again.

        Returns:
            bool: True if the player wants to play again, False otherwise.
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

    def multiplayer_mode(self):
        """
        Allows the game to be played in multiplayer mode, alternating between players.
        """
        player_count = int(input("Enter the number of players: "))
        players = []
        scores = {player: 0 for player in range(player_count)}

        for i in range(player_count):
            name = input(f"Enter player {i + 1} name: ")
            players.append(name)

        current_player_index = 0

        while True:
            current_player = players[current_player_index]
            self.choose_word(self.word_list)
            self.display_word, self.wrong_attempts, self.guessed_words = self.initialize_game(self.word)
            self.hint_used = False
            start_time = time.time()

            while not self.game_won() and not self.game_over():
                print(self.display_hangman(self.wrong_attempts))
                print("Word: " + " ".join(self.display_word))
                guess = input(
                    f"{current_player}, guess a letter or the whole word, or type 'hint' for a hint (you can use the hint only once): ").lower()

                if guess == "hint":
                    self.give_hint()
                elif guess.isalpha():
                    if guess in self.guessed_words:
                        print("You have already guessed that letter or word.")
                    else:
                        if len(guess) == 1:
                            self.update_game_state(guess)
                        elif len(guess) == len(self.word):
                            if guess == self.word:
                                self.display_word = list(self.word)
                                print(
                                    f"Congratulations {current_player}! You guessed the word: {''.join(self.display_word)}")
                                scores[current_player_index] += 1
                                break
                            else:
                                self.guessed_words.append(guess)
                                self.wrong_attempts += 1
                                print(f"Wrong! You have {self.max_attempts - self.wrong_attempts} attempts left.")
                        else:
                            print("Invalid input length. Please guess a single letter or the whole word.")
                else:
                    print("Invalid input. Please guess a letter or the whole word, or type 'hint'.")

            end_time = time.time()
            time_taken = end_time - start_time
            self.update_statistics(won=self.game_won(), time_taken=time_taken)
            self.update_leaderboard(current_player, won=self.game_won(), time_taken=time_taken)

            if not self.game_won():
                print(self.display_hangman(self.wrong_attempts))
                print(f"Game Over! The word was: {self.word}")

            if not self.try_again():
                break

            current_player_index = (current_player_index + 1) % player_count

        self.display_statistics()
        self.display_leaderboard()
        print("\nFinal Scores:")
        for player in players:
            print(f"{player}: {scores[players.index(player)]} points")

    def main(self):
        """
        Main function to run the Hangman game.
        """
        playing = True
        multiplayer = input("Do you want to play in multiplayer mode? (yes/no): ").lower() == "yes"
        if multiplayer:
            self.multiplayer_mode()
        else:
            use_custom_list = input("Do you want to add a custom word list? (yes/no): ").lower() == "yes"
            custom_word_list = self.get_custom_word_list() if use_custom_list else self.word_list

            name = input("Enter your name: ")
            print(f"Welcome {name}")
            print("=====================")
            print("Try to guess it in less than 10 attempts")

            while playing:
                self.choose_word(custom_word_list)
                self.display_word, self.wrong_attempts, self.guessed_words = self.initialize_game(self.word)
                self.hint_used = False
                start_time = time.time()

                while not self.game_won() and not self.game_over():
                    print(self.display_hangman(self.wrong_attempts))
                    print("Word: " + " ".join(self.display_word))
                    guess = input(
                        f"{name}, guess a letter or the whole word, or type 'hint' for a hint (you can use the hint only once): ").lower()

                    if guess == "hint":
                        self.give_hint()
                    elif guess.isalpha():
                        if guess in self.guessed_words:
                            print("You have already guessed that letter or word.")
                        else:
                            if len(guess) == 1:
                                self.update_game_state(guess)
                            elif len(guess) == len(self.word):
                                if guess == self.word:
                                    self.display_word = list(self.word)
                                    print(f"Congratulations {name}! You guessed the word: {''.join(self.display_word)}")
                                    break
                                else:
                                    self.guessed_words.append(guess)
                                    self.wrong_attempts += 1
                                    print(f"Wrong! You have {self.max_attempts - self.wrong_attempts} attempts left.")
                            else:
                                print("Invalid input length. Please guess a single letter or the whole word.")
                    else:
                        print("Invalid input. Please guess a letter or the whole word, or type 'hint'.")

                end_time = time.time()
                time_taken = end_time - start_time
                self.update_statistics(won=self.game_won(), time_taken=time_taken)
                self.update_leaderboard(name, won=self.game_won(), time_taken=time_taken)

                if not self.game_won():
                    print(self.display_hangman(self.wrong_attempts))
                    print(f"Game Over! The word was: {self.word}")

                playing = self.try_again()

            self.display_statistics()
            self.display_leaderboard()


if __name__ == "__main__":
    game = HangmanGame(word_list)
    game.main()
