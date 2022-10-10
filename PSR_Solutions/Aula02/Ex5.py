#!/usr/bin/env python3

import argparse
from readchar import readkey,key 

inputs=[]
def countNumbersUpTo(stop_char):
    while True:
        key = readkey()
        print('You entered the key ' +key)

        if key == stop_char:
            break

        inputs.append(key)


    numeric_inputs=[x for x in inputs if x.isnumeric()]
    other_inputs=[x for x in inputs if not x.isnumeric()]
    other_inputs2=[x for x in inputs if not x in numeric_inputs]

    print('Numeric_Inputs: '+str(numeric_inputs))
    print('Other Inputs: ' + str(other_inputs))
    print('Other Inputs2: ' + str(other_inputs2))


def main():

    parser=argparse.ArgumentParser(description='Test for PSR')
    parser.add_argument('-sc', '--stop_char', type=str, required=  False, default='x')

    args=vars(parser.parse_args)

    countNumbersUpTo(args('stop_char'))


if __name__ == "__main__":
    main()