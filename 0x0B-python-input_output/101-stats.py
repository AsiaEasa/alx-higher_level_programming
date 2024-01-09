#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
def print_stats(size, status_codes):
    print("File size: {}".format(size))
    for key, value in status_codes.items():
        print("{}: {}".format(key, value))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            size += int(line.split()[-1])
            code = line.split()[-2]
            if code in valid_codes:
                status_codes[code] = status_codes.get(code, 0) + 1

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, statu
	raise
