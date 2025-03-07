from random import randint

def get_guess():
  while True:
      try:
          guess = int(input("What number do you think it is? "))
          if 1 <= guess <= 100:
              return guess
          else:
              print("Please enter a number between 1 and 100.")
      except ValueError:
          print("Invalid input. Please enter a number.")

def give_advanced_hint(secret_number, guess):
  difference = abs(secret_number - guess)
  
  if difference > 50:
      return "You're very far!"
  elif difference > 30:
      return "You're quite far"
  elif difference > 20:
      return "You're getting closer..."
  elif difference > 10:
      return "Getting even closer!"
  elif difference > 5:
      return "Almost there!"
  else:
      return "You're very very close!"

def give_mathematical_hint(secret_number, attempt):
  hints = []
  
  if secret_number % 2 == 0:
      hints.append("The secret number is even")
  else:
      hints.append("The secret number is odd")
  
  if secret_number % 5 == 0:
      hints.append("It's a multiple of 5")
  elif secret_number % 3 == 0:
      hints.append("It's a multiple of 3")
      
  if secret_number > 50:
      hints.append("It's greater than 50")
  else:
      hints.append("It's less than or equal to 50")
  
  return hints[attempt % len(hints)]

def play():
  secret_number = randint(1, 100)
  attempts_dict = {}
  name = input("What's your name? ")

  print(f"\nHello, {name}. I've thought of a number between 1 and 100, and you have eight attempts to guess it.")

  for i in range(1, 9):
      guess = get_guess()
      attempts_dict[f"attempt{i}"] = guess

      if guess == secret_number:
          print(f"Congratulations, {name}! You guessed the secret number {secret_number} in attempt {i}!")
          break
      else:
          print(f"\nAttempt {i}:")
          if guess < secret_number:
              print("The secret number is higher than your guess.")
          else:
              print("The secret number is lower than your guess.")
          
          print(give_advanced_hint(secret_number, guess))
          print(give_mathematical_hint(secret_number, i))
          print(f"Remaining attempts: {8-i}")
          print("-" * 40)
  else:
      print(f"\nSorry! You didn't guess the secret number. It was {secret_number}.")

  print("\nYour attempts history:")
  for key, value in attempts_dict.items():
      print(f"{key}: {value}")

  play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
  if play_again == "y":
      print("\n" + "="*50 + "\n")
      play()
  else:
      print("\nThanks for playing!")

if __name__ == "__main__":
  play()