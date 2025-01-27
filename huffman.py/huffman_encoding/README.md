# Huffman Coding in Python

## Overview
This repository contains a Python implementation of the Huffman coding algorithm for text compression and decompression. The implementation is designed to help beginners understand the concept of data encoding using binary trees.

## Author
- Ayush Bhardwaj

## Features
- Build a frequency map of characters from the input text.
- Construct a Huffman Tree based on character frequencies.
- Generate Huffman codes for each character.
- Encode and decode text using the generated Huffman codes.

## Setup
To run this project, you'll need Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

1. Clone this repository or download the files to your local machine.
2. Navigate to the directory containing the project files in your terminal.
3. Run the script using Python:

## How It Works
The `huffman_coding.py` script performs several key functions:
- **Frequency Map Building:** Counts the frequency of each character in the provided text.
- **Huffman Tree Construction:** Uses a priority queue to build a tree where each node represents a character and its frequency. Nodes with the lowest frequency are combined and placed back into the queue until only one node remains, representing the root of the tree.
- **Encoding Map Construction:** Traverses the Huffman Tree to assign a unique binary code to each character, where the path to a character determines its code.
- **Text Encoding and Decoding:** Converts the original text into a string of binary codes and then back into the original text using the Huffman Tree.

## Contributing
Contributions to this project are welcome! You can contribute by:
- Improving the efficiency of the existing implementation.
- Adding new features, such as file input/output handling to work with different file types.
- Refactoring the code for clarity and maintainability.

## License
This project is open source and available under the [MIT License](LICENSE).

Enjoy exploring and enhancing the Huffman coding project!
