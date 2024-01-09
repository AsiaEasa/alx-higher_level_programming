#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            if count == 10:
                print("File size:", size)
                for key in sorted(status_codes):
                    print(f"{key}: {status_codes[key]}")
                count = 0

            parts = line.split()
            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    status_codes[parts[-2]] = status_codes.get(parts[-2], 0) + 1
            except IndexError:
                pass

        print("File size:", size)
        for key in sorted(status_codes):
            print(f"{key}: {status_codes[key]}")

    except KeyboardInterrupt:
        print("File size:", size)
        for key in sorted(status_codes):
            print(f"{key}: {status_codes[key]}")
        raise
