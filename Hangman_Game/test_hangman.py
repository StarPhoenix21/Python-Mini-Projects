import time
import unittest
from hangman import HangmanGame
from words import word_list  # Ensure the correct import path


class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        # Initialize a new Hangman game instance for each test
        self.game = HangmanGame(word_list)

    def test_choose_word_randomness(self):
        chosen_words = set()
        iterations = 100  # Number of iterations to test randomness

        # Choose a word multiple times to test for randomness
        for _ in range(iterations):
            self.game.choose_word(self.game.word_list)
            chosen_words.add(self.game.word)

        # Ensure that multiple unique words have been chosen
        self.assertGreater(len(chosen_words), 1, "Randomness test failed. Only one word was chosen repeatedly.")

    def test_initialize_game(self):
        word = "elephant"
        display_word, wrong_attempts, guessed_words = self.game.initialize_game(word)
        # Verify that the display word is initialized correctly
        self.assertEqual(display_word, ["_"] * len(word), "Display word initialization failed.")
        self.assertEqual(wrong_attempts, 0, "Wrong attempts initialization failed.")
        self.assertEqual(guessed_words, [], "Guessed words initialization failed.")

    def test_update_game_state_wrong_guess(self):
        word = "python"
        guess = "java"
        self.game.display_word, self.game.wrong_attempts, self.game.guessed_words = self.game.initialize_game(word)

        # Update game state with an incorrect word guess
        self.game.update_game_state(guess)

        self.assertEqual(self.game.display_word, ["_"] * len(word), "Wrong guess update failed.")
        self.assertIn(guess, self.game.guessed_words, "Guessed words update failed.")
        self.assertEqual(self.game.wrong_attempts, 1, "Wrong attempts should have incremented for wrong guess.")

    def test_give_hint(self):
        self.game.hint = "a large wild cat"
        self.game.hint_used = False

        # Use a hint and verify that the hint used flag is set to True
        self.game.give_hint()
        self.assertTrue(self.game.hint_used, "Hint usage failed.")


if __name__ == "__main__":
    unittest.main()
