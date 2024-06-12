![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/ndleah)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/ndleah?tab=repositories)

# Egg Catcher
<p align="center">
<img src="https://lh3.googleusercontent.com/gGELzDfgqxLvLQLxgn_LrhTQ9IrfFvrpMmRdN9fPHjSwzfew4QN22PyqRJwXZMGql7E" width=40% height=40%>

## 🛠️ Description

The Egg Catcher is a fun and interactive game built using Python and Tkinter. In this game, you can control a catcher,
with the catcher you need to catch the falling eggs, If an egg hits the ground, you lose a life.

## ⚙️ Languages or Frameworks Used
```bash
pip install tk
```

## 🌟 How to run
Running the script is really simple! Just open a terminal in the folder where your script is located and run the following command:

```sh
python eggcatcher_design.py
```

## 📺 Demo
<p align="center">
<img src="https://github.com/ndleah/python-mini-project/blob/main/IMG/eggcatcher.gif" width=40% height=40%>

## 🕹️ Game Instructions
  - Move Catcher: Use the left and right arrow key to move the catcher.
  - Catch Eggs: Move the catcher to catch the falling eggs before they hit the ground.
  - Lose a Life: You lose a life if an egg hits the ground.
  - Game Over: The game ends when all lives are lost.

## 🎮 Gameplay Features
  - Colorful Eggs: Eggs of different colors fall from the top of the screen.
  - Increasing Difficulty: The game speeds up as you get more points.
  - Score Tracking: Keep track of your score as you catch more eggs.
  - Lives Remaining: Track the number of lives you have left.

## 🧩 Classes and Methods
`EggCatchGame`
  - Attributes:
    - win: The root window of the Tkinter application.
    - canvas: The canvas widget where the game will be played.
    - canvas_width: Width of the game canvas.
    - canvas_height: Height of the game canvas.
    - color_cycle: Cycle of colors used for the eggs.
    - egg_width: Width of an egg.
    - egg_height: Height of an egg.
    - egg_score: Points scored for catching an egg.
    - egg_speed: Speed at which eggs fall.
    - egg_interval: Interval between egg drops.
    - difficulty_factor: Factor by which the game difficulty increases.
    - catcher_color: Color of the catcher.
    - catcher_width: Width of the catcher.
    - catcher_height: Height of the catcher.
    - score: Current score of the game.
    - lives_remaining: Number of lives remaining.
    
  - Methods:
    - __init__(self, win, canvas): Initializes the game state with the root window and canvas.
    - create_egg(self): Creates eggs at random position and adds them to the canvas.
    - move_eggs(self): Moves the eggs down the canvas.
    - move_left(self): Moves the catcher to the left.
    - move_right(self): Moves the catcher to the right.
    - egg_dropped(self, egg): Handles the event when an egg is dropped and removes it from the canvas.
    - lose_a_life(self): Decreases the number of lives.
    - catch_check(self): Checks if any eggs have been caught by the catcher.
    - increase_score(self, points): Increases the score by a specified number of points and adjust the game difficulty.
    
`EggCatchDesign`
  - Attributes:
    - win: The root window of the Tkinter application.
    - canvas: The canvas widget where the game will be played.
    - game: An instance of 'EggCatchGame' that manage the game logic.
    
  - Methods:
    - __init__(self, win): Initializes the EggCatchDesign with the root window.
    - Sets up the canvas and game environment.
    - Binds keyboard events for moving the catcher.
    - Starts the main event loop.

## 🤖 Author
[Leah Nguyen](https://github.com/ndleah)