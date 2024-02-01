#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: List of integers representing the UTF-8 encoded data.

    Returns:
    - True if the data is a valid UTF-8 encoding, False otherwise.
    """
    nbytes = 0
    b1 = 1 << 7
    b2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if nbytes == 0:
            while mask & byte:
                nbytes += 1
                mask = mask >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (byte & b1 and not (byte & b2)):
                return False
        nbytes -= 1

    return nbytes == 0
