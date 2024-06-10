import turtle as t
from gameDesign import GameDesign

class CaterpillarGame:
    """
    The CaterpillarGame is a game where the player controls a caterpillar to eat
    leaves, and grow in length, while avoiding the window boundaries.

    Attributes:
        design (GameDesign): An instance of the GameDesign class to handle game visuals.
        game_started (bool): A flag indicating if the game has started.
        score (int): The score of the player
        caterpillar_speed (int): the speed of the caterpillar
        caterpillar_length (int): the length of the caterpillar
        retry_button (turtle.Turtle): A turtle to represent the retry button.
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
        self.create_retry_button()
        t.tracer(0)

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

    def create_retry_button(self):
        """
        Creates the retry button.
        """
        self.retry_button = t.Turtle()
        self.retry_button.shape('square')
        self.retry_button.color('blue')
        self.retry_button.penup()
        self.retry_button.hideturtle()
        self.retry_button.goto(0, -50)
        self.retry_button.onclick(self.start_game)
        self.retry_button.write('Retry', align='center', font=('Arial', 18, 'bold'))

    def start_game(self, x=None, y=None):
        """
        Start the game, resetting the score, caterpillar's speed, and length, and placing the first leaf.
        """
        if self.game_started:
            return
        self.game_started = True
        self.retry_button.clear()
        self.retry_button.hideturtle()
        self.reset_game()
        self.run_game_loop()

    def reset_game(self):
        """
        Resets the game to its initial state.
        """
        self.score = 0
        self.design.text_turtle.clear()
        self.design.score_turtle.clear()
        self.clear_game_over_text()

        self.caterpillar_speed = 2
        self.caterpillar_length = 3
        self.design.caterpillar.color('black')
        self.design.caterpillar.shapesize(1, self.caterpillar_length, 1)
        self.design.caterpillar.goto(0, 0)
        self.design.caterpillar.setheading(0)
        self.design.caterpillar.showturtle()

        self.design.leaf.color('green')
        self.design.display_score(self.score)
        self.design.place_leaf()

    def run_game_loop(self):
        """
        Runs the main loop, moving the caterpillar, checking for collisions with leaves,
        updating the score, and checking for game over conditions.
        """
        if self.game_started:
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
                return
            t.update()
            t.ontimer(self.run_game_loop, 100)

    def outside_window(self):
        """
        Checks if the caterpillar is outside the window boundaries.

        Returns:
            bool: True if the caterpillar is outside the window, False otherwise.
        """
        left_wall = -t.window_width() / 2
        right_wall = t.window_width() / 2
        top_wall = t.window_height() / 2
        bottom_wall = -t.window_height() / 2
        (x, y) = self.design.caterpillar.pos()
        return x < left_wall or x > right_wall or y > top_wall or y < bottom_wall

    def game_over(self):
        """
        Ends the game by changing the color of the caterpillar and leaf, and displaying 'Game Over' text.
        """
        self.game_started = False
        self.design.caterpillar.color('yellow')
        self.design.leaf.color('yellow')
        t.penup()
        t.hideturtle()
        t.write('Game Over!', align='center', font=('Arial', 30, 'normal'))
        self.retry_button.showturtle()
        self.retry_button.goto(0, -50)
        self.retry_button.write('Retry', align='center', font=('Arial', 18, 'bold'))

    def clear_game_over_text(self):
        """
        Clears the 'Game Over' Text.
        """
        t.clear()
        t.hideturtle()

    def move_up(self):
        """
        Changes the caterpillar's directions to up.
        """
        if self.design.caterpillar.heading() != 270:
            self.design.caterpillar.setheading(90)

    def move_down(self):
        """
        changes the caterpillar's direction to down.
        """
        if self.design.caterpillar.heading() != 90:
            self.design.caterpillar.setheading(270)

    def move_left(self):
        """
        Changes the caterpillar's direction to left.
        """
        if self.design.caterpillar.heading() != 0:
            self.design.caterpillar.setheading(180)

    def move_right(self):
        """
        Changes the caterpillar's direction to right.
        """
        if self.design.caterpillar.heading() != 180:
            self.design.caterpillar.setheading(0)

if __name__ == '__main__':
    game = CaterpillarGame()
    t.mainloop()








