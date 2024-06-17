import random
import time
from words import word_list  # Import the default word list


class HangmanGame:
    def __init__(self, word_list):
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
        chosen_word_info = random.choice(word_list)
        self.word = chosen_word_info["word"]
        self.hint = chosen_word_info["hint"]
        self.display_word, self.wrong_attempts, self.guessed_words = self.initialize_game(self.word)
        self.hint_used = False
        self.start_time = time.time()

    def initialize_game(self, word):
        return ["_"] * len(word), 0, []

    def update_game_state(self, guess):
        self.guessed_words.append(guess)
        correct_guess = False

        if guess == self.word:
            self.display_word = list(self.word)
            correct_guess = True
        else:
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
        if self.hint_used:
            print("You have already used your hint!")
        else:
            print(f"Hint: {self.hint}")
            self.hint_used = True

    def game_won(self):
        return "_" not in self.display_word

    def game_over(self):
        return self.wrong_attempts >= self.max_attempts

    def update_statistics(self, won, time_taken):
        self.statistics["games_played"] += 1
        self.statistics["total_time"] += time_taken
        if won:
            self.statistics["games_won"] += 1
        else:
            self.statistics["games_lost"] += 1

    def display_statistics(self):
        print("\nStatistics:")
        print(f"Games Played: {self.statistics['games_played']}")
        print(f"Games Won: {self.statistics['games_won']}")
        print(f"Games Lost: {self.statistics['games_lost']}")
        if self.statistics["games_played"] > 0:
            avg_time = self.statistics["total_time"] / self.statistics["games_played"]
            print(f"Average Time: {avg_time: .2f} seconds")

    def sort_key(self, entry):
        # Sort by won status (True > False), then by time (ascending)
        return entry["won"], -entry["time"]

    def update_leaderboard(self, name, won, time_taken):
        self.leaderboard.append({"name": name, "won": won, "time": time_taken})
        self.leaderboard.sort(key=self.sort_key, reverse=True)

    def display_leaderboard(self):
        print("\nLeaderboard:")
        for entry in self.leaderboard:
            status = "Won" if entry["won"] else "Lost"
            print(f"{entry['name']}: {status} in {entry['time']:.2f} seconds")

    def get_custom_word_list(self):
        custom_word_list = []
        while True:
            word = input("Enter a word (or 'done' to finish): ").lower()
            if word == 'done':
                break
            hint = input("Enter a hint for this word: ").lower()
            custom_word_list.append({"word": word, "hint": hint})
        return custom_word_list

    def try_again(self):
        while True:
            response = input("Do you want to play again? (yes/no): ").lower()
            if response == "yes":
                return True
            elif response == "no":
                print("Thanks for playing! Goodbye.")
                return False
            else:
                print("Please answer 'yes' or 'no'.")

    def main(self):
        playing = True
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
                guess = input(f"{name}, guess the word or type 'hint' for a hint (you can use the hint only once): ").lower()

                if guess == "hint":
                    self.give_hint()
                elif guess.isalpha() and guess == self.word:
                    self.display_word = list(self.word)
                    print(f"Congratulations {name}! You guessed the word: {''.join(self.display_word)}")
                    break
                elif guess.isalpha():
                    self.update_game_state(guess)
                else:
                    print("Invalid input. Please guess a word or type 'hint'.")

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
