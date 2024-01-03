#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input 'text' is not a string.

    Notes:
        - The function prints each sentence or phrase on a new line with two blank lines between them.
        - There are no leading or trailing spaces on each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in separators:
            print(current_line.strip())
            print()  # Print an empty line after the separator
            current_line = ""

    # Print the last line if it's not empty
    if current_line.strip():
        print(current_line.strip())
