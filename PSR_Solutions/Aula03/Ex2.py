#!/usr/bin/env python3


def addComplex(x, y):
    a,b=x
    c,d=y
    real = a+c
    imaginary = b+d

# alternativa ao que foi feito antes
#    real=x[0]+y[0]
#    imaginary=x[1]+y[1]

    return (real, imaginary)


def multiplyComplex(x, y):
    a,b=x
    c,d=y
    real = a+c
    imaginary = b+d

    real=a*c-b*d
    imaginary=a*d+b*c
    return (real, imaginary)


def printComplex(x):
   
    real,imaginary=x
    print(str(real)+'+'+str(imaginary)+'i')


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()





