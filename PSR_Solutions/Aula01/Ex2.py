#!/usr/bin/env python3

from colorama import Fore,Back,Style
from math import remainder


# Global variable
#A small user interface to insert the number
while True:
    try:
        maximum_number = int(input("Please insert a number: "))
    except ValueError:
        print("The number is not a valid integer number.")
    else:
        break
    
    


def isPrime(value):

    for number in range(2,value):
        remainder = value%number
        if remainder==0: #I'm sure the number isn't prime
            return False

    #If I get here there it was no divider with remainder 0
    return True



def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number+1):
        if isPrime(i):
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.' + Style.RESET_ALL)
        else:
            print(Fore.BLUE + 'Number ' + str(i) + ' is not prime.' + Style.RESET_ALL)

if __name__ == "__main__":
    main()