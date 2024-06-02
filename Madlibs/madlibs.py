import random
from sys import exit

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input.strip()
        else:
            print("Please enter a valid input.")

def play_madlib():
    print("Title: Eat, Drink, And Be Sick")
    nouns = [get_user_input("Enter noun: ") for _ in range(4)]
    plural_nouns = [get_user_input("Enter plural noun: ") for _ in range(6)]
    adjectives = [get_user_input("Enter adjective: ") for _ in range(2)]
    adverb = get_user_input("Enter adverb: ")
    letter = get_user_input("Enter any letter: ")
    body_part = get_user_input("Enter any body part: ")

    print("\nAn inspector from the Department of Health and", random.choice(nouns), "Services paid a surprise visit to our", random.choice(adjectives), "school cafeteria.")
    print("The lunch special, prepared by our", random.choice(adjectives), "dietician, was spaghetti and", random.choice(nouns), "balls with a choice of either a", random.choice(nouns), "salad or French", random.choice(plural_nouns), ".")
    print("The inspector found the meat-", random.choice(plural_nouns), "to be overcooked and discovered a live", random.choice(nouns), "in the fries, causing him to have a " + body_part + " ache.")
    print("In response, he threw up all over his", random.choice(plural_nouns), ".")
    print("In his report, the inspector", adverb, "recommended that the school cafeteria serve only nutritious", random.choice(plural_nouns), "as well as low-calorie", random.choice(plural_nouns), "and that all of the saturated", random.choice(plural_nouns), "be eliminated.")
    print("He rated the cafeteria a " + letter + "-minus.")

    return get_user_input('\nDo you want to play again? (Yes/No): ').lower().startswith('y')

def main():
    print("Starting the madlib game...\n")
    play_again = True
    while play_again:
        play_again = play_madlib()

    print("You've chosen not to play.")
    print('Exiting....')
    exit(0)

if __name__ == '__main__':
    main()



