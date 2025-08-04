import random
import operator
import math

def get_user_input(prompt):
    """Get a validated float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_random_problem():
    """Generate a random math problem and return its answer."""
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op_symbol = random.choice(list(operations.keys()))
    
    # Avoid divide by zero
    if op_symbol == '/':
        while num2 == 0:
            num2 = random.randint(1, 10)

    answer = round(operations[op_symbol](num1, num2), 3)
    print(f"\nWhat is {num1} {op_symbol} {num2}?")
    return answer

def ask_question():
    """Ask one question and check the user's answer."""
    correct_answer = generate_random_problem()
    user_answer = get_user_input("Enter your answer: ")
    
    # Use math.isclose to compare floats with a tolerance
    if math.isclose(user_answer, correct_answer, rel_tol=1e-2):
        return True
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}")
        return False

def play_game():
    """Main game loop."""
    score = 0
    print("🧠 Welcome to the Math Quiz Game!")
    while True:
        if ask_question():
            score += 1
            print("✅ Correct!")
        else:
            break
    print(f"\n🎮 Game Over! Your score: {score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
