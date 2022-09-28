#!/usr/bin/env python
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, Setember 2020.
# --------------------------------------------------

maximum_number = 100  # maximum number to test.


def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    # <Add stuff here>
    return []


def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """

    # <Add stuff here>
    return False


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()