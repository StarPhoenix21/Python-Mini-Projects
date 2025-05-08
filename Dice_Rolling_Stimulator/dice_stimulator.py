import random

class DiceSimulator:
    """
    A class to simulate rolling two dice.
    
    Features:
    - Randomly rolls two dice with ASCII representation.
    - Offers user the option to roll again or quit.
    """

    dice_faces = [
        """ 
        ===========
        |         |
        |    O    |
        |         |
        ===========
        """,
        """ 
        ===========
        | O       |
        |         |
        |       O |
        ===========
        """,
        """ 
        ===========
        | O       |
        |    O    |
        |       O |
        ===========
        """,
        """ 
        ===========
        | O     O |
        |         |
        | O     O |
        ===========
        """,
        """ 
        ===========
        | O     O |
        |    O    |
        | O     O |
        ===========
        """,
        """ 
        ===========
        | O     O |
        | O     O |
        | O     O |
        ===========
        """
    ]

    def roll_dice(self):
        """
        Rolls two dice and prints their ASCII representation.
        """
        dice_rolls = random.choices(self.dice_faces, k=2)
        for die in dice_rolls:
            print(die)

    def start_game(self):
        """
        Starts the dice rolling game, giving the user the option to roll again.
        """
        print("🎲 Welcome to the Dice Simulator! 🎲")
        while True:
            self.roll_dice()
            choice = input("Do you want to roll again? (y/n): ").strip().lower()
            if choice != 'y':
                print("Thanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    game = DiceSimulator()
    game.start_game()
