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

    return {'r':real, 'i':imaginary}


def multiplyComplex(x, y):
    a,b=x
    c,d=y
    real = a+c
    imaginary = b+d
    real=a*c-b*d
    imaginary=a*d+b*c
    return (real, imaginary)


def printComplex(x):
   
    real=x['r']
    imaginary=x['i']
    print(str(real)+'+'+str(imaginary)+'i')


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 ={'r':5, 'i':7}
    c2 = {'r':-2, 'i':4}

    # Test add
    c3 = addComplex(c1, c2)
    print('Result of addition is: ')

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()





