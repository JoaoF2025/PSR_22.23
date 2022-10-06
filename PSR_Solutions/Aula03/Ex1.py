#!/usr/bin/env python3

from math import sqrt
import time
from colorama import Fore, Back, Style

def tic():
    # seconds passed since epoch
    initialseconds = time.time()
    date = time.ctime(initialseconds)
    print("I started computing at: " + Back.YELLOW + Fore.BLACK + str(date) + Style.RESET_ALL)   
    return initialseconds

def toc():
    a=5*10**7
    for i in range (0,a):
        b=sqrt(a)
        finalseconds = time.time()
    return finalseconds

def main():
    init=tic()
    final=toc()
    elap=final-init
    print('It took ' + str(elap) + ' seconds to compute that.' + Fore.RED + 'Sorry, I\'m old and slow' + Fore.CYAN + ' uwu' + Style.RESET_ALL)

if __name__ == "__main__":
    main()