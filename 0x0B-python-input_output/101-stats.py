#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print(f"Total Size: {size}")
    print("Status Codes:")
    for code, count in sorted(status_codes.items()):
        print(f"  {code}: {count}")

def process_log():
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count = 1 if count == 10 else count + 1

            try:
                parts = line.split()
                size += int(parts[-1])
                status_code = parts[-2]
                if status_code in valid_codes:
                    status_codes[status_code] = status_codes.get(status_code, 0) + 1
            except (IndexError, ValueError):
                pass

            if count == 1:
                print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

if __name__ == "__main__":
    process_log()
