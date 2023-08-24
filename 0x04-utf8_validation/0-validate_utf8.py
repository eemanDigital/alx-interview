#!/usr/bin/python3
"""Module to check valid UTF-8 Encoding
"""


def validUTF8(data):
    """ Check if data is valid UTF-8 encoding or not
    Args:
    data (int): dinput data to be checked

    Return:
    True or False if data is checked
    """
    num_bytes_to_check = 0
    for byte in data:
        if num_bytes_to_check == 0:
            if (byte >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_to_check = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_check -= 1

    return num_bytes_to_check == 0

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
