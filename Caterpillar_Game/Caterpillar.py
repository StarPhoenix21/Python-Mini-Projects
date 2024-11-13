import turtle as t
import random as rd

# Set the background color
t.bgcolor('yellow')

# Caterpillar setup
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# Leaf setup
leaf = t.Turtle()
leaf_shape = ((0,0), (14,2), (18,6), (20,20), (6,18), (2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

# Text setup
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

# Score setup
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

# Game state variables
game_started = False

def outside_window():
    """Check if the caterpillar is outside the window."""
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside

def game_over():
    """Handle game over scenario."""
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))
    t.onkey(start_game, 'space')  # Allow the user to restart the game by pressing SPACE

def display_score(current_score):
    """Display the score on the screen."""
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 70
    y = (t.window_height() / 2) - 70
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    """Randomly place the leaf on the screen."""
    leaf.hideturtle()
    leaf.setx(rd.randint(-200, 200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()

def start_game():
    """Start the game."""
    global game_started
    if game_started:
        return
    game_started = True

    # Reset game state
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    caterpillar.color('black')
    score = 0
    caterpillar_speed = 2
    text_turtle.clear()

    # Reset caterpillar position
    caterpillar.penup()
    caterpillar.setpos(0, 0)
    caterpillar.setheading(0)

    # Display initial score and place the first leaf
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)

        # Check if the caterpillar eats the leaf
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)

        # Check if the caterpillar is outside the window
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() != 270:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() != 90:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() != 0:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() != 180:
        caterpillar.setheading(0)

def restart_game():
    """Restart the game when 'R' is pressed."""
    global game_started
    if game_started:
        game_started = False
        caterpillar.hideturtle()
        leaf.hideturtle()
        score_turtle.clear()
        text_turtle.clear()
        t.clear()  # Clear any game over text
        start_game()

# Bind keys
t.onkey(start_game, 'space')
t.onkey(restart_game, 'r')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')

# Listen to the keyboard inputs
t.listen()
t.mainloop()

