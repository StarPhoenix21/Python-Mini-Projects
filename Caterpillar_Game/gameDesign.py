import turtle as t
import random as rd

class GameDesign:
    """
    The GameDesign class handle the setup and visual aspect of the caterpillar game,
    including the screen, caterpillar, leaf, text and score display.

    Attributes:
        caterpillar (turtle.Turtle): A turtle representing the caterpillar.
        leaf (turtle.Turtle): The turtle representing the leaf.
        text_turtle (turtle.Turtle): A turtle for displaying text messages.
        score_turtle (turtle.Turtle): A turtle for displaying the score.
    """
    def __init__(self):
        """
        Initializes the GameDesign class.
        """
        self.setup_screen()
        self.setup_caterpillar()
        self.setup_leaf()
        self.setup_text_turtle()
        self.setup_score_turtle()

    def setup_screen(self):
        """
        Sets up the game screen
        """
        t.bgcolor('yellow')

    def setup_caterpillar(self):
        """
        Sets up the caterpillar turtle.
        """
        self.caterpillar = t.Turtle()
        self.caterpillar.shape('square')
        self.caterpillar.speed(0)
        self.caterpillar.penup()
        self.caterpillar.hideturtle()

    def setup_leaf(self):
        """
        Sets up the leaf turtle.
        """
        self.leaf = t.Turtle()
        leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
        t.register_shape('leaf', leaf_shape)
        self.leaf.shape('leaf')
        self.leaf.color('green')
        self.leaf.penup()
        self.leaf.hideturtle()
        self.leaf.speed(0)

    def setup_text_turtle(self):
        """
        Sets up the text turtle
        """
        self.text_turtle = t.Turtle()
        self.text_turtle.hideturtle()

    def setup_score_turtle(self):
        """
        Sets up the score turtle
        """
        self.score_turtle = t.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.speed(0)

    def write_text(self, message, position, font):
        """
        Writes the given text on the screen.

        Parameters:
            message (str): The text to be displayed.
            position (tuple): The (x, y) position to display the text.
            font (tuple): The font properties for the text.
        """
        self.text_turtle.clear()
        self.text_turtle.penup()
        self.text_turtle.goto(position)
        self.text_turtle.write(message, align='center', font=font)

    def display_score(self, score):
        """
        Displays the current score on the screen.

        Parameters:
            score (int): The current score to be displayed.
        """
        self.score_turtle.clear()
        self.score_turtle.penup()
        x = (t.window_width() / 2) - 70
        y = (t.window_height() / 2) - 70
        self.score_turtle.setpos(x, y)
        self.score_turtle.write(str(score), align='right', font=('Arial', 40, 'bold'))

    def place_leaf(self):
        """
        Places the leaf at a random position on the screen.
        """
        self.leaf.hideturtle()
        self.leaf.setx(rd.randint(-200, 200))
        self.leaf.sety(rd.randint(-200, 200))
        self.leaf.showturtle()





