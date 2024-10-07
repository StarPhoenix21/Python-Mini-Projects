import os
import argparse
def open_file():
    try:
        file_path = input("Enter the path to the file: ")
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening file: {e}")





  
def create_folder():
    folder_path = input("Enter the path to the folder: ")
    folder_name = input("Enter the name of the folder: ")
    try:
        os.makedirs(os.path.join(folder_path, folder_name), exist_ok=True)
        print(f"Folder '{folder_name}' created successfully.")
    except Exception as e:
        print(f"Error creating folder: {e}")


def write_to_file():
    file_path = input("Enter the name of the file:  ")
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, 'w') as f:
           f.write(input("Enter the text to be written to the file:  "))
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
   
    parseer = argparse.ArgumentParser(description="Command Line Argumet")
    parseer.add_argument("-w", "--write", help="write to a file", action="store_true")
    parseer.add_argument("-o", "--open", help="open a file", action="store_true")
    parseer.add_argument("-c", "--create", help="create a new folder", action="store_true")
    args = parseer.parse_args()
    if args.write:
        write_to_file()
    elif args.open:
        open_file()
    elif args.create:
        create_folder()


    else:
        print("Invalid input. Please try again.")

if __name__== "__main__":
  main()