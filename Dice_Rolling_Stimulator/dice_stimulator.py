import random

class DiceSimulator:
    """
    A class to simulate rolling a dice.

    Attributes:
        dice_faces (dict): A dictionary that contain the faces of the dice as lists of strings.
    """
    def __init__(self):
        """
        Initializes the DiceSimulator with dice faces.
        """
        self.dice_faces = {
            1: [
                "===========",
                "|         |",
                "|    O    |",
                "|         |",
                "==========="
            ],
            2: [
                "===========",
                "|         |",
                "| O     O |",
                "|         |",
                "==========="
            ],
            3: [
                "===========",
                "|    O    |",
                "|    O    |",
                "|    O    |",
                "==========="
            ],
            4: [
                "===========",
                "| O     O |",
                "|         |",
                "| O     O |",
                "==========="
            ],
            5: [
                "===========",
                "| O     O |",
                "|    O    |",
                "| O     O |",
                "==========="
            ],
            6: [
                "===========",
                "| O     O |",
                "| O     O |",
                "| O     O |",
                "==========="
            ]
        }

    def roll_dice(self):
        """
        Rolls the dice and prints the corresponding face.

        Returns:
            int: The number rolled on the dice
        """
        number = random.randint(1, 6)
        dice_face = self.dice_faces[number]
        for line in dice_face:
            print(line)
        return number

    def play_again(self):
        """
        Prompts the user to roll again or exit the game.

        Returns:
            roll_again (bool): Indicates whether the user wants to roll again.
            exit_game (bool): Indicates whether the user wants to exit the game.
        """
        choice = input("Type 'y' and enter if you want to roll again, or 'x' to exit: ").lower()
        return choice == 'y', choice == 'x'

    def start(self):
        """
        Starts the dice rolling simulation.
        """
        print("This is a dice stimulator")
        while True:
            number = self.roll_dice()
            roll_again, exit_game = self.play_again()
            if exit_game:
                print("Exiting the game...")
                break
            elif not roll_again:
                print("Rolling stopped.")
                break

if __name__ == "__main__":
    game = DiceSimulator()
    game.start()





