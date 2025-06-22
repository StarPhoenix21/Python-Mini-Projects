class VigenereCipher:
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def shift_char(self, c, key_c, encode=True):
        if c not in self.alphabet:
            return c
        shift = self.alphabet.index(key_c)
        if not encode:
            shift = -shift
        return self.alphabet[(self.alphabet.index(c) + shift) % 26]

    def transform(self, text: str, encode=True):
        text = text.lower()
        result = []
        key_len = len(self.keyword)
        for i, c in enumerate(text):
            key_c = self.keyword[i % key_len]
            result.append(self.shift_char(c, key_c, encode))
        return ''.join(result)

    def encrypt(self, text: str) -> str:
        return self.transform(text, True)

    def decrypt(self, text: str) -> str:
        return self.transform(text, False)

if __name__ == "__main__":
    keyword = input("Enter encryption keyword: ").strip()
    cipher = VigenereCipher(keyword)

    plaintext = input("Enter text to encrypt: ").strip()
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted text: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted back: {decrypted}")