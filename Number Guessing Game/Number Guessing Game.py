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
