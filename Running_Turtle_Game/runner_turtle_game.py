#Project: Game-Runner Turtle
"""
PRACTISE: This is a practice for understanding Turtle & the graphical user.
PROJECT: A screen and text box will appear where you can write your bet about the color of the turtles.
The game will start, and one random turtle will cross the hurdle.
Then you will see the final information about whether you are a winner or loser.
"""


from turtle import Turtle, Screen
import random

FONT = ("Courier", 18, "normal")

screen = Screen()
screen.setup(width=500, height=400)

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(x=230, y= -200)
tim.setheading(90)
tim.pendown()
tim.pensize(3)
tim.pencolor()
tim.forward(400)

# turtle for text information to show end of the game
text = Turtle()
text.penup()
text.hideturtle()

# control the user bet for which colored turtle 
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

all_turtles = []

for turtle_index in range(0, 6):
    y = -100
    new_turtle = Turtle(shape="turtle")
    # Turtle production as many colors as possible
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y+40*turtle_index)
    all_turtles.append(new_turtle)

# User claim control and game continues until the fence is crossed.
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON! The {winning_color} turtle is winner!")
                # winner text show page on the screen
                text.goto(x=0, y=0)
                text.pendown()
                text.pensize(20)
                text.pencolor("blue")
                text.write(f"You've won! The {winning_color} turtle is winner!", align="center", font=FONT)
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")
                # loser text show page on the screen
                text.goto(x=0, y=0)
                text.pendown()
                text.pensize(20)
                text.pencolor("red")
                text.write(f"You've LOST! The {winning_color} turtle is winner!", align="center", font=FONT)

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
