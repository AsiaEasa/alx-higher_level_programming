#!/usr/bin/python3


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = [".", "?", ":"]
    for delimiter in delimiters:
        split_lines = text.split(delimiter)
        stripped_lines = [line.strip(" ") for line in split_lines]
        formatted_text = (delimiter + "\n\n").join(stripped_lines)
        text = formatted_text

    print(text, end="")

if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
