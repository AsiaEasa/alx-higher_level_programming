#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    print("File size:", size)
    for key, value in sorted(status_codes.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {value}")
