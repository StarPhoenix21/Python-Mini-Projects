import pyfiglet

def print_3d_ascii_art():
    # Get user input
    user_text = input("Enter your name or text: ")
    
    # Use a 3D-like font
    ascii_art = pyfiglet.figlet_format(user_text, font="slant")
    
    # Print the 3D ASCII art
    print(ascii_art)

# Run the function
print_3d_ascii_art()
