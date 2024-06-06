import turtle as t
from gameDesign import GameDesign


class CaterpillarGame:
    """
    The CaterPillarGame is a game where the player controls a caterpillar to eat leaves and grow in length,
    while avoiding the window boundaries.

    Attributes:
        design (GameDesign): An instance of the GameDesign class to handle game visuals.
        game_started (bool): A flag indicating if the game has started.
        score (int): The current score of the game.
        caterpillar_speed (int): The current speed of the caterpillar.
        caterpillar_length (int): The current length of the caterpillar.
    """
    def __init__(self):
        """
        Initializes the game by setting up the initial game state and binding keyboard keys.
        """
        self.design = GameDesign()
        self.game_started = False
        self.score = 0
        self.caterpillar_speed = 2
        self.caterpillar_length = 3

        self.design.write_text('Press Space to start', (0, 0), ('Arial', 18, 'bold'))
        self.bind_keys()

    def bind_keys(self):
        """
        Binds the arrow keys for controlling the caterpillar and the space key to start the game.
        """
        t.onkey(self.start_game, 'space')
        t.onkey(self.move_up, 'Up')
        t.onkey(self.move_right, 'Right')
        t.onkey(self.move_down, 'Down')
        t.onkey(self.move_left, 'Left')
        t.listen()

    def start_game(self):
        """
        Start the game, resetting the score, caterpillar's speed, and length. Places the first leaf.
        """
        if self.game_started:
            return
        self.game_started = True

        self.score = 0
        self.design.text_turtle.clear()

        self.caterpillar_speed = 2
        self.caterpillar_length = 3
        self.design.caterpillar.shapesize(1, self.caterpillar_length, 1)
        self.design.caterpillar.showturtle()

        self.design.display_score(self.score)
        self.design.place_leaf()

        self.run_game_loop()

    def run_game_loop(self):
        """
        Runs the main game loop, moving the caterpillar, checking for collisions with leaves,
        updating the score, and checking for a game over conditions.
        """
        while True:
            self.design.caterpillar.forward(self.caterpillar_speed)
            if self.design.caterpillar.distance(self.design.leaf) < 20:
                self.design.place_leaf()
                self.caterpillar_length += 1
                self.design.caterpillar.shapesize(1, self.caterpillar_length, 1)
                self.caterpillar_speed += 1
                self.score += 10
                self.design.display_score(self.score)
            if self.outside_window():
                self.game_over()
                break

    def outside_window(self):
        """
        Checks if the caterpillar is outside the window boundaries.

        Returns:
            bool: True if the capillar is outside the window, False otherwise.
        """
        left_wall = -t.window_width() / 2
        right_wall = t.window_width() / 2
        top_wall = t.window_height() / 2
        bottom_wall = -t.window_height() / 2
        (x, y) = self.design.caterpillar.pos()
        outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
        return outside

    def game_over(self):
        """
        Ends the game by changing the color of the caterpillar and leaf, and displaying 'Game Over' text.
        """
        self.design.caterpillar.color('yellow')
        self.design.leaf.color('yellow')
        t.penup()
        t.hideturtle()
        t.write('Game Over!', align='center', font=('Arial', 30, 'normal'))
        t.onkey(self.start_game, 'space')

    def move_up(self):
        """
        Changes the caterpillar's direction to up
        """
        self.design.caterpillar.setheading(90)

    def move_down(self):
        """
        Changes the caterpillar's direction to down.
        """
        self.design.caterpillar.setheading(270)

    def move_left(self):
        """
        Changes the caterpillar's direction to left
        """
        self.design.caterpillar.setheading(180)

    def move_right(self):
        """
        Changes the caterpillar's direction to right
        """
        self.design.caterpillar.setheading(0)


if __name__ == '__main__':
    game = CaterpillarGame()
    t.mainloop()
