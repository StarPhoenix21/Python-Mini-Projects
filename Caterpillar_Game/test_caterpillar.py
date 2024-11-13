import unittest
from unittest.mock import patch, MagicMock
import caterpillar

class TestCaterpillarGame(unittest.TestCase):

    def setUp(self):
        """在每个测试之前运行"""
        self.caterpillar = caterpillar.caterpillar

    @patch('caterpillar.t.Turtle')
    def test_start_game(self, MockTurtle):
        """测试开始游戏"""
        mock_turtle = MockTurtle()
        caterpillar.start_game()

        # 验证调用了显示初始得分的方法
        self.assertTrue(mock_turtle.write.called, "Failed to display score at the start.")

    def test_outside_window(self):
        """测试毛毛虫是否在窗口外"""
        # 设置位置为窗口边界外
        self.caterpillar.setx(caterpillar.t.window_width() / 2 + 10)
        self.caterpillar.sety(caterpillar.t.window_height() / 2 + 10)

        # 使用断言来检查
        self.assertTrue(caterpillar.outside_window(), "Caterpillar should be outside the window.")

    @patch('caterpillar.t.Turtle')
    def test_move_up(self, MockTurtle):
        """测试毛毛虫向上移动"""
        caterpillar.caterpillar.setheading(0)  # Initially set to right
        caterpillar.move_up()
        self.assertEqual(caterpillar.caterpillar.heading(), 90, "Caterpillar did not change heading to up correctly.")

    @patch('caterpillar.t.Turtle')
    def test_move_down(self, MockTurtle):
        """测试毛毛虫向下移动"""
        caterpillar.caterpillar.setheading(0)  # Initially set to right
        caterpillar.move_down()
        self.assertEqual(caterpillar.caterpillar.heading(), 270, "Caterpillar did not change heading to down correctly.")

    @patch('caterpillar.t.Turtle')
    def test_move_left(self, MockTurtle):
        """测试毛毛虫向左移动"""
        caterpillar.caterpillar.setheading(90)  # Initially set to up
        caterpillar.move_left()
        self.assertEqual(caterpillar.caterpillar.heading(), 180, "Caterpillar did not change heading to left correctly.")

    @patch('caterpillar.t.Turtle')
    def test_move_right(self, MockTurtle):
        """测试毛毛虫向右移动"""
        caterpillar.caterpillar.setheading(180)  # Initially set to left
        caterpillar.move_right()
        self.assertEqual(caterpillar.caterpillar.heading(), 0, "Caterpillar did not change heading to right correctly.")

    @patch('caterpillar.t.Turtle')
    def test_place_leaf(self, MockTurtle):
        """测试随机放置叶子"""
        mock_leaf = MockTurtle()
        caterpillar.place_leaf()
        self.assertTrue(mock_leaf.showturtle.called, "Leaf was not displayed after placing.")

if __name__ == '__main__':
    unittest.main()
