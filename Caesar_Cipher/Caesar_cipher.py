class CipherTool:
    def __init__(self, key: dict) -> None:
        self.key = key
        self.reverse_key = {v: k for k, v in key.items()}
        self.blank_string = ""
        self.decrypted_string = ""

    def get_input(self) -> None:
        while True:
            blank_string = input("Enter string to encrypt (letters only): ")
            if blank_string.isalpha():
                self.blank_string = blank_string.lower()
                break
            else:
                print("Invalid input. Please enter alphabetic characters only.")

    def encrypt_string(self) -> str:
        output = ''.join(self.key.get(c, c) for c in self.blank_string)
        self.decrypted_string = output
        return output

    def decrypt_string(self, string: str) -> str:
        string = string.lower().strip()
        if not string:
            return self.blank_string
        return ''.join(self.reverse_key.get(c, c) for c in string)


if __name__ == "__main__":
    key = {
        "a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i",
        "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o",
        "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u",
        "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a",
        "y": "b", "z": "c"
    }

    cipher = CipherTool(key=key)
    cipher.get_input()
    encrypted = cipher.encrypt_string()
    print("Encrypted string:", encrypted)

    decrypted = cipher.decrypt_string(encrypted)
    print("Decrypted back:", decrypted)
