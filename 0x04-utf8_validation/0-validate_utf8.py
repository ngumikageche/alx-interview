#!/usr/bin/python3
"""a method that determines if a given data set represents
 a valid UTF-8 encoding"""


def validUTF8(data):
    """Initialize a variable to track the number
      of bytes for the current character"""
    bytes_to_follow = 0

    for byte in data:
        """ Check the two most significant bits of the byte"""
        byte_as_bin = format(byte, '08b')
        if bytes_to_follow == 0:
            if byte_as_bin[0] == '0':
                continue
            """Count the number of consecutive 1s starting from the left"""
            while byte_as_bin.startswith('10'):
                byte_as_bin = byte_as_bin[2:]
                bytes_to_follow -= 1
            """ Determine the number of bytes to follow """
            if byte_as_bin.startswith('110'):
                bytes_to_follow = 1
            elif byte_as_bin.startswith('1110'):
                bytes_to_follow = 2
            elif byte_as_bin.startswith('11110'):
                bytes_to_follow = 3
            else:
                return False
        else:
            if not byte_as_bin.startswith('10'):
                return False
            bytes_to_follow -= 1
    return bytes_to_follow == 0
