import unittest
from caterpillarGame import CaterpillarGame


class TestCaterpillarGame(unittest.TestCase):

    def setUp(self):
        self.game = CaterpillarGame()

    def test_initial_state(self):
        self.assertFalse(self.game.game_started)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.caterpillar_speed, 2)
        self.assertEqual(self.game.caterpillar_length, 3)

    def test_move_up(self):
        self.game.move_up()
        self.assertEqual(self.game.design.caterpillar.heading(), 90)

    def test_move_down(self):
        self.game.move_down()
        self.assertEqual(self.game.design.caterpillar.heading(), 270)

    def test_move_left(self):
        self.game.move_left()
        self.assertEqual(self.game.design.caterpillar.heading(), 180)

    def test_move_right(self):
        self.game.move_right()
        self.assertEqual(self.game.design.caterpillar.heading(), 0)


if __name__ == '__main__':
    unittest.main()
