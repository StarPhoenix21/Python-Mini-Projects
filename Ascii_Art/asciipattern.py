import pyfiglet

def print_ascii_art():
    # Get user input
    user_text = input("Enter your name or text: ")
    
    # Generate ASCII art
    ascii_art = pyfiglet.figlet_format(user_text)
    
    # Print the ASCII art
    print(ascii_art)

# Run the function
print_ascii_art()
