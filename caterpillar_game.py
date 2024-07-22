import turtle as t
import random as rd

# Set up the screen
t.bgcolor('yellow')

# Create and set up the caterpillar turtle
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# Create and set up the leaf turtle
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

# Initialize game state
game_started = False

# Create a turtle for displaying text
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

# Create a turtle for displaying the score
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

# Create and set up the obstacle turtles
num_obstacles = 5  # Number of obstacles
obstacles = []

for _ in range(num_obstacles):
    new_obstacle = t.Turtle()
    new_obstacle.shape('circle')
    new_obstacle.color('red')
    new_obstacle.penup()
    new_obstacle.setposition(rd.randint(-200, 200), rd.randint(-200, 200))
    new_obstacle.showturtle()
    obstacles.append(new_obstacle)

# Check if the caterpillar is outside the window bounds
def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside

# Handle game over conditions and prompt to try again
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER ! Press R to Try Again', align='center', font=('Arial', 30, 'normal'))
    t.onkey(try_again, 'r')  # Bind 'r' key to try_again function

# Display the current score on the screen
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 70
    y = (t.window_height()/2) - 70
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

# Randomly place the leaf on the screen
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200, 200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()

# Start or restart the game
def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        
        # Check for collision with the leaf
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)
        
        # Check for collision with obstacles
        for obstacle in obstacles:
            if caterpillar.distance(obstacle) < 20:
                game_over()
                return
        
        # Check if caterpillar is outside the window bounds
        if outside_window():
            game_over()
            return

# Control the caterpillar's movement
def move_up():
    caterpillar.setheading(90)

def move_down():
    caterpillar.setheading(270)

def move_left():
    caterpillar.setheading(180)

def move_right():
    caterpillar.setheading(0)

# Restart the game when the 'r' key is pressed
def try_again():
    global game_started
    game_started = False
    caterpillar.hideturtle()
    leaf.hideturtle()
    for obstacle in obstacles:
        obstacle.hideturtle()
    text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
    t.onkey(start_game, 'space')

# Set up key bindings
t.onkey(start_game, 'space')  # Start the game with SPACE key
t.onkey(try_again, 'r')       # Restart the game with 'r' key
t.onkey(move_up, 'Up')        # Move up with UP key
t.onkey(move_right, 'Right')  # Move right with RIGHT key
t.onkey(move_down, 'Down')    # Move down with DOWN key
t.onkey(move_left, 'Left')    # Move left with LEFT key
t.listen()

# Start the Turtle graphics loop
t.mainloop()
