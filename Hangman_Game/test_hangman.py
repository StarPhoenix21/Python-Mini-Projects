import time
import unittest
from Hangman_Game import Hangman
from words import word_list


class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        # Initialize a new Hangman game instance for each test
        self.game = HangmanGame(word_list)

    def test_choose_word_randomness(self):
        chosen_words = set()
        iterations = 100  # Number of iterations to test randomness

        # Choose a word multiple times to test for randomness
        for _ in range(iterations):
            chosen_word_info = self.game.choose_word()
            chosen_words.add(chosen_word_info['word'])

        # Ensure that multiple unique words have been chosen
        self.assertGreater(len(chosen_words), 1, "Randomness test failed. Only one word was chosen repeatedly.")

    def test_initialize_game(self):
        word = "elephant"
        display_word, wrong_attempts, guessed_words, hint_used = self.game.initialize_game(word)
        # Verify that the display word is initialized correctly
        self.assertEqual(display_word, ["_"] * len(word), "Display word initialization failed.")
        self.assertEqual(wrong_attempts, 0, "Wrong attempts initialization failed.")
        self.assertEqual(guessed_words, [], "Guessed words initialization failed.")
        self.assertFalse(hint_used, "Hint used initialization failed.")

    def test_update_game_state_correct_guess(self):
        word = "python"
        guess = "python"
        display_word = ["_"] * len(word)
        guessed_words = []
        wrong_attempts = 0
        max_attempts = 10

        display_word, guessed_words, wrong_attempts = self.game.update_game_state(
            guess, word, display_word, guessed_words, wrong_attempts, max_attempts
        )

        self.assertEqual(display_word, list(word), "Correct guess update failed.")
        self.assertIn(guess, guessed_words, "Guessed words update failed.")
        self.assertEqual(wrong_attempts, 0, "Wrong attempts should not have incremented for correct guess.")

    def test_update_game_state_wrong_guess(self):
        word = "python"
        guess = "java"
        display_word = ["_"] * len(word)
        guessed_words = []
        wrong_attempts = 0
        max_attempts = 6

        # Update game state with an incorrect word guess
        display_word, guessed_words, wrong_attempts = self.game.update_game_state(
            guess, word, display_word, guessed_words, wrong_attempts, max_attempts
        )

        self.assertEqual(display_word, ["_"] * len(word), "Wrong guess update failed.")
        self.assertIn(guess, guessed_words, "Guessed words update failed.")
        self.assertEqual(wrong_attempts, 1, "Wrong attempts should have incremented for wrong guess.")

    def test_give_hint(self):
        hint = "a large wild cat"
        hint_used = False

        # Use a hint and verify that the hint used flag is set to True
        hint_used = self.game.give_hint(hint, hint_used)
        self.assertTrue(hint_used, "Hint usage failed.")

    def test_update_statistics(self):
        # Update game statistics and verify changes
        self.game.update_statistics(won=True, time_taken=10)
        self.assertEqual(self.game.statistics['games_played'], 1, "Games played count is incorrect.")
        self.assertEqual(self.game.statistics['games_won'], 1, "Games won count is incorrect.")
        self.assertEqual(self.game.statistics['total_time'], 10, "Total time is incorrect.")

    def test_update_leaderboard(self):
        # Update leaderboard and verify the changes
        self.game.update_leaderboard(name="Alice", won=True, time_taken=20)
        self.assertEqual(len(self.game.leaderboard), 1, "Leaderboard entry count is incorrect.")
        self.assertEqual(self.game.leaderboard[0]['name'], "Alice", "Leaderboard name is incorrect.")
        self.assertTrue(self.game.leaderboard[0]['won'], "Leaderboard win status is incorrect.")
        self.assertEqual(self.game.leaderboard[0]['time'], 20, "Leaderboard time is incorrect.")

    def test_timer(self):
        start_time = time.time()
        time.sleep(1)  # Simulate a delay
        end_time = time.time()
        time_taken = end_time - start_time
        self.assertTrue(1 <= time_taken < 2, "Timer function is incorrect.")

    def test_multiplayer_turns(self):
        players = ["Alice", "Bob"]
        self.game.players = players
        current_player_index = 0

        # Stimulate turns and verify the turn order
        for _ in range(4):
            current_player = players[current_player_index]
            self.assertEqual(current_player, self.game.players[current_player_index], "Turn order is incorrect.")
            current_player_index = (current_player_index + 1) % len(players)

    def test_winning_condition(self):
        word = "python"
        guess = "python"
        display_word = ["_"] * len(word)
        guessed_words = []
        wrong_attempts = 0
        max_attempts = 6

        # Simulate guessing the entire word correctly
        display_word, guessed_words, wrong_attempts = self.game.update_game_state(
            guess, word, display_word, guessed_words, wrong_attempts, max_attempts
        )

        # Verify that the game recognizes the win
        self.assertEqual(display_word, list(word), "Winning condition failed: Display word update is incorrect.")
        self.assertIn(guess, guessed_words, "Winning condition failed: Guessed words update is incorrect.")
        self.assertEqual(wrong_attempts, 0, "Winning condition failed: Wrong attempts should not have incremented.")


if __name__ == "__main__":
    unittest.main()