#!/usr/bin/env python3

#NOT WORKING YET, REVIEW

from collections import namedtuple

Complex= namedtuple('Complex',['r','i'])

def addComplex(x, y):
#    a,b=x
#    c,d=y
    a=x.r
    b=x.i
    c=y.r
    d=y.i

    real = a+c
    imaginary = b+d


# alternativa ao que foi feito antes
#    real=x[0]+y[0]
#    imaginary=x[1]+y[1]

    return Complex(real, imaginary)


def multiplyComplex(x, y):
    a=x.r
    b=x.i
    c=y.r
    d=y.i

    real=a*c-b*d
    imaginary=a*d+b*c
    return Complex(real, imaginary)


def printComplex(x):
   
    real=x.r
    imaginary=x.i
    print(str(real)+'+'+str(imaginary)+'i')


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 7)
    c2 = Complex(-2, 4)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()





