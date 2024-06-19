# Number Guessing Game

## Overview
Welcome to the Number Guessing Game! This is a fun and engaging game where you get to test your guessing skills. The computer will randomly choose a number between 1 and 30, and your goal is to guess what that number is within a limited number of attempts.

## How to Play
1. **Objective:** Guess the number the computer is thinking of, which is between 1 and 30.
2. **Attempts:** You have a maximum of 3 tries to guess the correct number.
3. **Hints:** After each incorrect guess, you will receive a hint indicating whether the actual number is higher or lower than your guess.
4. **Winning:** If you guess the number correctly within the given attempts, you win!
5. **Losing:** If you use all 3 attempts without guessing the correct number, you lose, and the correct number will be revealed.

## Rules
- You must enter a number between 1 and 30.
- Invalid inputs (non-numeric or out-of-range numbers) will prompt an error message and do not count as a try.

## Example
- The computer picks a random number, say 18.
- You guess 10. The game will tell you to guess higher.
- You guess 20. The game will tell you to guess lower.
- You guess 18. You win!

## Code
Here's the code for the Number Guessing Game:

```python
import random

x = random.randint(1, 30)
max_tries = 3
tries = 0

while tries < max_tries:
    try:
        guess = int(input("I am thinking of a number between 1 and 30. Can you guess it?: "))
        if guess < 1 or guess > 30:
            print("Please enter a number between 1 and 30.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 30.")
        continue

    tries += 1

    if guess == x:
        print(f"You guessed it! I was thinking of the number {x}.")
        break
    else:
        if guess < x:
            hint = "higher"
        else:
            hint = "lower"
        if tries < max_tries:
            print(f"Nope, try again. Guess {hint}. You have used {tries} out of {max_tries} tries.")

if tries == max_tries and guess != x:
    print(f"Sorry, you have reached the maximum number of tries. The number I was thinking of was {x}.")


## Demo
![Screenshot 2024-06-19 130607](https://github.com/Hami-d-Raza/python-mini-project/assets/157746262/46a427cc-b79c-4451-919f-e4ff827bb53e)

## Author
This game is from Hamid Raza
<br>
This is my GitHub Profile( https://github.com/Hami-d-Raza ) 
<br>
I am a new user on GitHub and I don't know how to make branches and add them. Please approve this. I spent a whole day making this.
