import turtle as t
import random as rd

class GameDesign:
    def __init__(self):
        self.setup_screen()
        self.setup_caterpillar()
        self.setup_leaf()
        self.setup_text_turtle()
        self.setup_score_turtle()

    def setup_screen(self):
        t.bgcolor('yellow')

    def setup_caterpillar(self):
        self.caterpillar = t.Turtle()
        self.caterpillar.shape('square')
        self.caterpillar.speed(0)
        self.caterpillar.penup()
        self.caterpillar.hideturtle()

    def setup_leaf(self):
        self.leaf = t.Turtle()
        leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
        t.register_shape('leaf', leaf_shape)
        self.leaf.shape('leaf')
        self.leaf.color('green')
        self.leaf.penup()
        self.leaf.hideturtle()
        self.leaf.speed(0)

    def setup_text_turtle(self):
        self.text_turtle = t.Turtle()
        self.text_turtle.hideturtle()

    def setup_score_turtle(self):
        self.score_turtle = t.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.speed(0)

    def write_text(self, message, position, font):
        self.text_turtle.clear()
        self.text_turtle.penup()
        self.text_turtle.goto(position)
        self.text_turtle.write(message, align='center', font=font)

    def display_score(self, score):
        self.score_turtle.clear()
        self.score_turtle.penup()
        x = (t.window_width() / 2) - 70
        y = (t.window_height() / 2) - 70
        self.score_turtle.setpos(x, y)
        self.score_turtle.write(str(score), align='right', font=('Arial', 40, 'bold'))

    def place_leaf(self):
        self.leaf.hideturtle()
        self.leaf.setx(rd.randint(-200, 200))
        self.leaf.sety(rd.randint(-200, 200))
        self.leaf.showturtle()

