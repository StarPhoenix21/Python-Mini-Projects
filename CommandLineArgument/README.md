# File Management Tool

A simple command-line tool for managing files and folders in Python. This tool allows users to create folders, open files, and write content to files through command-line arguments.

## Features

- **Open a File**: Opens a specified file using the default application.
- **Create a Folder**: Creates a new folder at a specified location.
- **Write to a File**: Creates a new file or overwrites an existing one with user-provided text.

## Requirements

- Python 3.x
- os
- argparse

## Usage

### Command Line Arguments

You can use the following command-line arguments to execute different functionalities:

- `-o` or `--open`: Opens a specified file.
- `-c` or `--create`: Creates a new folder.
- `-w` or `--write`: Writes to a specified file.

### Examples

1. **To Open a File:**
   ```bash
   name_of_the_file -o
