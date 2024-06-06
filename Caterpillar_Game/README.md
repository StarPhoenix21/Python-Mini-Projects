![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/ndleah)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/ndleah?tab=repositories)

# Caterpillar
<p align="center">
<img src="https://static.wikia.nocookie.net/pixar/images/e/ec/Heimlich.png/revision/latest?cb=20170807224005" width=30% height=30%>

## 🛠️ Description

A simple Caterpillar game built in Python where the player controls a caterpillar to
eat leaves and grow in length while avoiding the window boundaries. The game involves
increasing the score by eating leaves and ends if the caterpillar goes outside the window boundaries.

## ⚙️ Languages or Frameworks Used
```bash
pip install turtle
```

## 🌟 How to run
Running the script is really simple! Just open a terminal in the folder where your script is located and run the following command:

```sh
python caterpillarGame.py
```
## 📺 Demo
<p align="center">
<img src="https://github.com/ndleah/python-mini-project/blob/main/IMG/caterpillar.gif" width=70% height=70%>

## 🕹️ Game Instructions
- Start the Game: Press the 'space' key to start the game.
- Move Up: Press the 'up arrow' key to move the caterpillar up.
- Move Down: Press the 'down arrow' key to move the caterpillar down.
- Move Left: Press the 'left arrow' key to move the caterpillar left.
- Move Right: Press the 'Right arrow' key to move the caterpillar right.

## 🎮 Gameplay Features
- Score: Gain 10 points for each leaf eaten.
- Caterpillar Growth: The caterpillar grows in length and increases in speed with each leaf eaten.
- Game Over: The game ends if the caterpillar hits the window boundary.

## 🧩 Classes and Methods
`CaterpillarGame`
- Attributes:
  - design (GameDesign): Handles game visuals.
  - game_started (bool): Indicates if the game has started.
  - score (int): Current game score.
  - caterpillar_speed (int): Speed of the caterpillar.
  - caterpillar_length (int): Length of the caterpillar.

- Methods:
  - __init__(): Initializes the game state and binds keyboard keys.
  - bind_keys(): Binds arrows keys and space key.
  - start_game(): Starts the game, resets score, speed, and length, and places the first leaf.
  - run_game_loop(): Main game loop to move caterpillar, check collisions, update score, and check game over.
  - outside_window(): Checks if the caterpillar is outside window boundaries.
  - game_over(): Ends the game and displays 'Game Over' text.
  - move_up(), move_down(), move_left(), move_right(): Changes caterpillar's direction.

`GameDesign`
- Attributes:
  - caterpillar (turtle.Turtle): Represents the caterpillar.
  - leaf (turtle.Turtle): Represents the leaf.
  - text_turtle (turtle.Turtle): Displays text messages.
  - score_turtle (turtle.Turtle): Displays the score.
  
- Methods:
  - __init__(): Sets up the screen, caterpillar, leaf, and text and score turtles.
  - setup_screen(): Sets up the game screen.
  - setup_caterpillar(): Sets up the caterpillar.
  - setup_leaf(): Sets up the leaf.
  - setup_text_turtle(), setup_score_turtle(): Set up text and score turtles.
  - write_text (message, position, font): Writes a text message on the screen.
  - display_score(score): Displays the score.
  - place_leaf(): Places the leaf at a random position within the window.

## 🤖 Author
[Leah Nguyen](https://github.com/ndleah)