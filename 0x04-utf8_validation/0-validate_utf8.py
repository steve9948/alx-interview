#!/usr/bin/python3
"""UTF8 validation."""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits of the first byte
    masks = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
    # Masks to validate the pattern of leading bits
    patterns = [0b00000000, 0b11000000, 0b11100000, 0b11110000]
    # Masks to validate continuation bytes
    continuation_mask = 0b11000000
    continuation_pattern = 0b10000000

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0b11111111

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            for i in range(4):
                if (byte & masks[i]) == patterns[i]:
                    num_bytes = i if i != 0 else 1
                    break
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte & continuation_mask) != continuation_pattern:
                return False

        # If this byte is part of a multi-byte character, decrement the count
        num_bytes -= 1

    # If num_bytes is not zero, then we have an incomplete multi-byte character
    return num_bytes == 0
