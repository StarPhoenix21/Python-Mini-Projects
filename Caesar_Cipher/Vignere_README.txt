<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%94%91&message=If%20Useful&style=style=flat&color=green)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Vigenère Cipher: Classical Text Encryption

<p align="center">
<img src="assests/main.png" width=40% height=40%>

## 🛠️ Description

This script implements the **Vigenère Cipher**, a classic polyalphabetic substitution encryption technique. It accepts a keyword from the user to encode and decode messages. The same keyword must be used to decrypt the output, making it a lightweight reversible encryption tool. This is a great intro project for learning about ciphers and key-based text transformations.

The script demonstrates:
1. A `VigenereCipher` class with methods to encrypt and decrypt alphabetic strings
2. Character-level transformation based on a repeating keyword
3. Custom `transform()` logic that handles both encryption and decryption

Feel free to enhance it with non-alphabet support, file-based encryption, or use it inside a larger pipeline.

## ⚙️ Languages or Frameworks Used

- Python 3.x standard library only
- No external packages required

## 🌟 How to run

To execute the script, run the following in your terminal:

```bash
python vigenere_cipher.py
```

When prompted:
- Enter a **keyword** to serve as the encryption key
- Enter the plaintext you'd like to encrypt
- The script will output the encrypted text and decrypt it back immediately

Use `CTRL + C` to exit at any point.

## 📺 Demo

An example prompt might look like:

```
Enter encryption keyword: lemon
Enter text to encrypt: hello world
Encrypted text: siprb xbpqe
Decrypted back: hello world
```

<img src="assests/colorgame.png" width=40% height=40%>

## 🤖 Author

Script by Dr. rer. nat. Nenad Balaneskovic.

Nenad Balaneskovic → [GitHub Profile](https://github.com/NenadBalaneskovic)

Feel free to contribute your own enhancements or port this into other encryption schemes!