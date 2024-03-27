#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers
        return None
    peak = list_of_integers[0]
    for num in list_of_integers:
        if num > peak:
            peak = num

    return peak
