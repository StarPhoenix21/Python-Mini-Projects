import turtle as t
from gameDesign import GameDesign

class CaterpillarGame:
    def __init__(self):
        self.design = GameDesign()
        self.game_started = False
        self.score = 0
        self.caterpillar_speed = 2
        self.caterpillar_length = 3

        self.design.write_text('Press Space to start', (0, 0), ('Arial', 18, 'bold'))

    def start_game(self):
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
        left_wall = -t.window_width() / 2
        right_wall = t.window_width() / 2
        top_wall = t.window_height() / 2
        bottom_wall = -t.window_height() / 2
        (x, y) = self.design.caterpillar.pos()
        outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
        return outside

    def game_over(self):
        self.design.caterpillar.color('yellow')
        self.design.leaf.color('yellow')
        t.penup()
        t.hideturtle()
        t.write('Game Over!', align='center', font=('Arial', 30, 'normal'))
        t.onkey(self.start_game, 'space')

    def move_up(self):
        self.design.caterpillar.setheading(90)

    def move_down(self):
        self.design.caterpillar.setheading(270)

    def move_left(self):
        self.design.caterpillar.setheading(180)

    def move_right(self):
        self.design.caterpillar.setheading(0)

game = CaterpillarGame()

t.onkey(game.start_game, 'space')
t.onkey(game.move_up, 'Up')
t.onkey(game.move_right, 'Right')
t.onkey(game.move_down, 'Down')
t.onkey(game.move_left, 'Left')
t.listen()
t.mainloop()

