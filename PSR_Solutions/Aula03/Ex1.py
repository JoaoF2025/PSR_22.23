#!/usr/bin/env python3

from math import sqrt
import time

def tic():
    # seconds passed since epoch
    initialseconds = time.time()
    date = time.ctime(initialseconds)
    print("I started computing at: ", date)
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
    print('It took ' + str(elap) + ' seconds to compute that. Sorry, I\'m old and slow')

if __name__ == "__main__":
    main()