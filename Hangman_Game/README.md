![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/ndleah)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/ndleah?tab=repositories)

# Hangman Game
<p align="center">
<img src="https://i.pinimg.com/736x/56/21/55/5621553db7eedebcad64bf185be3d7e6.jpg" width=40% height=40%>

## 🛠️ Description

A hangman game simulator using Python in which the player have 10 attempts to guess the phrase before the man is hung.

## ⚙️ Languages or Frameworks Used
You only need Python to run this script. You can visit [here](https://www.python.org/downloads/) to download Python.

# Hangman Game Documentation

Welcome to the Hangman Game documentation. This documentation will guide you through the installation, usage, gameplay, code structure, testing, contributing, and contact information.

## Table of Contents

1. [Installation](installation.md)
2. [Usage](usage.md)
3. [Gameplay](gameplay.md)
4. [Code Structure](code_structure.md)
5. [Testing](testing.md)
6. [Contributing](contributing.md)
7. [License](license.md)
8. [Contact](contact.md)


## 🌟 How to run
Running the script is really simple! Just open a terminal in the folder where your script is located and run the following command:

<p align="center">
<img src="https://github.com/ndleah/python-mini-project/blob/main/IMG/hangman.gif" width=70% height=70%>

## 🔧 Features
* Single-player mode: Play against the computer with a random word.
* Multiplayer mode: Play with a friend, taking turns to guess the word.
* Custom word list: Option to add your own words to the game.
* Hints: Get hints to help you guess the word.
* Statistics: Track your game statistics including games played, games won, and average time taken.
* Leaderboard: View the leaderboard with the fastest times and highest scores.
* Timer: Each game session is timed to add an extra challenge.

# Gameplay
## Single-Player Mode
* The game selects a random word from a predefined list.
* You have 10 attempts to guess the word.
* Enter one letter at a time to guess the word.
* You can also type "hint" to receive a hint for the current word.

## Multiplayer Mode
* Two players take turns to guess the word.
* Each player is prompted to enter their name at the start.
* Players alternate turns after each guess.

## Custom Word List
* The game will prompt you to add custom words before starting.
* If you choose to add a custom word, you will also need to provide a hint for the word.

## Hints
* Players can type "hint" during their turn to receive a hint.
* Each hint usage is counted and displayed in the statistics.

## Statistics and Leaderboard
* The game tracks the number of games played, games won, and total time taken.
* A leaderboard displays the fastest times and highest scores.

## Code Structure
The project consists of the following main files:
* `hangman.py`: The main game script. Contains the game logic and user interactions.
* `words.py`: Contains the list of words and hints used in the game.
* `test_hangman.py`: Unit tests for the game logic.

`hangman.py`
This script includes:

* `HangmanGame`: The main class managing the game logic.
* Methods for initializing the game, updating game state, providing hints, tracking statistics, and handling multiplayer turns.

## `words.py`
This script includes:

* `word_list:` A list of words and their associated hints used in the game. 

## `test_hangman.py`
This script includes:

* Unit tests for verifying the correctness of the game logic.
* Tests for word selection randomness, game initialization, state updates, hint usage, statistics tracking, and multiplayer functionality.
## 📂 Project Structure
This project consists of the following main files: 
* 'hangman.py': The main game script.
* words.py: Contains the list of words and hints.
* test_hangman.py: Unit tests for the game logic.

## 🧪 Running Tests
To ensure that everything is working correctly, you can run the unit tests provided. Open a terminal in the folder where your test script is located and run the following command:

## 📝 License
This project is open source and available under the MIT License.

## 🤖 Author
[Leah Nguyen](https://github.com/ndleah)

## 🙌 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact
If you have any questions or suggestions, feel free to reach out to me at ndleah@gmail.com.

## ⭐ Acknowledgements
* Open Source Love
* GitHub Profile
* View Repositories 

Thank you for checking out this project! If you found it useful, please consider giving it a star. 🌟