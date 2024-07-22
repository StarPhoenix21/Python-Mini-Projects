Added Code Documentation to the existing Caterpillar game

Changes Made to code:

    Added the try_again() Function: This function resets the game state and displays the initial message prompting the player to press SPACE to start a new game.

    Updated the game_over() Function: Now it also provides instructions to press 'R' to try again and binds the 'R' key to the try_again() function.

    Resetting the Game State in try_again(): This function hides the caterpillar and leaf, and re-displays the initial prompt.

This approach gives players the option to restart the game with the 'R' key and keeps the game logic clear and manageable.