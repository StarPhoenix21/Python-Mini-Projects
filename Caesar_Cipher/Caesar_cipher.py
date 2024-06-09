class main:
    """
    The Main class provides functionality for encrypting and decrypting strings using a simple substitution cipher.

    Attributes:
        key (dict): A dictionary mapping each letter of the alphabet to its corresponding encrypted letter.
        blank_string (str): The string input by the user to be encrypted.
        decrypted_string (str): The string that results from the encryption of the blank_string.
    """
    def __init__(self,key:dict) -> None:
        """
        Initializes the Main class with the given key for the substitution cipher.

        Parameters:
            key (dict): A dictionary mapping each letter of the alphabet to its corresponding encrypted letter.
        """
        self.key = key

    def get_input(self) -> None:
        """
        Prompts the user to enter a string to be encrypted, validates the input, and converts it to lowercase.
        Only alphabetical input is accepted, if the input is invalid, the user is prompted to try again.
        """
        while True:
            blank_string = str(input("Enter string to decrypt: "))
            if blank_string.isalpha():
                blank_string = blank_string.lower()
                self.blank_string = blank_string
                break
            else:
                print("Input is not valid")
                continue

    def encrypt_string(self) -> str:
        """
        Encrypts the user-provided string using the substitution cipher defined by the key.

        Returns:
            str:The encrypted string.
        """
        output = ""
        for c in self.blank_string:
            for k,v in self.key.items():
                if k == c:
                    output += v
                else:
                    continue
        self.decrypted_string = output
        return(output)

    def decrypt_string(self, string: str) -> str:
        """
        Decrypts a given string using the substitution cipher defined by the key.

        Parameters:
            string (str): The string to be decrypted.

        Returns:
            str: The decrypted string, or the original blank_string if the input string is empty.
        """
        output = "" 
        string = string.lower()
        string = string.strip()
        if string == "":
            return(self.blank_string)
        else: 
            for c in string:
                for k,v in self.key.items():
                    if v == c:
                        output += k
        
        return(output)

if __name__ == "__main__":
    key ={"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}
    main = main(key=key)
    main.get_input()
    print(main.encrypt_string())
