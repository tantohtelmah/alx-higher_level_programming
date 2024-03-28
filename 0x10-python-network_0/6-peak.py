#!/usr/bin/python3
"""
Inisialiation of the code
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in an unsorted list of integers.
    """
    n = len(list_of_integers)
    left, right = 0, n - 1

    try:
        while left < right:
            mid = left + (right - left) // 2

            # Check if the middle element is a peak
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return list_of_integers[left]
    except IndexError:
        print(None)
