#!/usr/bin/env python3

#This is the test file for the first GROUP PROJECT

import readchar
import colorama
import random


def printChars(stop_char):
    myList=[]
    while True:
        print('Type something (Press ' + colorama.Fore.RED + stop_char + colorama.Style.RESET_ALL + ' to stop)')
        pressed_key=readchar.readkey()
        
        if pressed_key==stop_char:
            print('You typed ' + colorama.Fore.RED + stop_char + colorama.Style.RESET_ALL + '... terminating process... Cyaaaaaa') 
            break
        else:
            myList.append(pressed_key)
            key=random.randint(97,122)
            print('Your random number is '+ str(key) + ' and it\'s equivalent to '+ str(chr(key)))
            print('Key ' + colorama.Fore.YELLOW + pressed_key + colorama.Style.RESET_ALL + ' was added to your list.')
    
    print('Thank you for typing, here\'s your list: ' + str(myList))


       
def main():
    printChars('x')
    

if __name__ == '__main__':
    main()