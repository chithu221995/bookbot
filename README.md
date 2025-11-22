# BookBot

BookBot - A Python application that reads and analyzes text files from books.

## Description

This is a training project from [Boot.dev](https://boot.dev) that demonstrates fundamental Python skills including:
- File I/O operations
- String manipulation
- Data structures (dictionaries and lists)
- Sorting algorithms
- Function design

## Features

- **Word Count**: Calculates the total number of words in a book
- **Character Frequency Analysis**: Counts how many times each alphabetic character appears (case-insensitive)
- **Formatted Report**: Displays results in a clean, readable format sorted by character frequency

## Usage

Run the program with:

```bash
python3 main.py
```

The program will analyze the book located at `books/frankenstein.txt` and display a report.

## Example Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
--- End report ---
```

## Project Structure

```
bookbot/
├── main.py              # Main application file
├── books/               # Directory containing text files to analyze
│   └── frankenstein.txt # Sample book (Frankenstein by Mary Shelley)
└── README.md            # This file
```

## Requirements

- Python 3.x
- No external dependencies required (uses only Python standard library)
