#!/usr/bin/python3

"""function that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    n (int) :
    Return : returns an integer
    """


def minOperations(n):
    if n == 1:
        return (n)

    operations = 0
    copied = 0
    current_H = 1

    while current_H < n:
        if n % current_H == 0:
            """If n is div by the current num of 'H's,
            we copy all and pate multiple times"""
            copied = current_H
        """perform copy and paste operations"""
        operations += 1
        current_H += copied

    return (operations)
