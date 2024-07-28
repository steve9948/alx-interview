#!/usr/bin/python3
"""UTF8 validation."""


def is_continuation(byte):
    """
    Check if the byte is a valid continuation byte.

    A continuation byte in UTF-8 starts with the bits '10'.
    """
    return (byte & 0b11000000) == 0b10000000


def get_num_bytes(byte):
    """
    Determine the number of bytes in the current UTF-8 character.

    The number of leading '1' bits in the first byte determines
    the number of bytes.
    """
    if (byte & 0b10000000) == 0b00000000:
        return 1
    elif (byte & 0b11100000) == 0b11000000:
        return 2
    elif (byte & 0b11110000) == 0b11100000:
        return 3
    elif (byte & 0b11111000) == 0b11110000:
        return 4
    else:
        return -1


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8, False otherwise.
    """
    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])
        if num_bytes == -1:
            return False

        # Check if the subsequent bytes are valid continuation bytes.
        for j in range(i + 1, i + num_bytes):
            if j >= len(data) or not is_continuation(data[j]):
                return False

        i += num_bytes

    return True
