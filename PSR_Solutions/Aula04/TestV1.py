#!/usr/bin/env python3

#This is the test file for the first GROUP PROJECT

import readchar
import colorama
import random


def printChars(stop_char):
    myList=[]
    randomList=[]
    print('Type something (Press ' + colorama.Fore.RED + stop_char + colorama.Style.RESET_ALL + ' to stop)')
    while True:
        key=chr(random.randint(97,122))
        print('Press the key ' + key)
        pressed_key=readchar.readkey()

        if pressed_key==stop_char:
            print('You typed ' + colorama.Fore.RED + stop_char + colorama.Style.RESET_ALL + '... terminating process... Cyaaaaaa') 
            break
        if pressed_key==key:
            myList.append(pressed_key)
            randomList.append(key)
            print('Congrats!')
        else:
            randomList.append(key)
            print("Try Again!")

    mlNum=len(myList)
    rdmNum=len(randomList)
    acc=int((mlNum/rdmNum)*100)
    if mlNum==rdmNum:
        print('Congrats! You got ' + colorama.Fore.RED + str(acc) +'%' + colorama.Style.RESET_ALL + ' accuracy! Well Done <3')
    else:
        print('Ufff, almost there! You got '+ colorama.Fore.RED + str(acc) +'%' +colorama.Style.RESET_ALL+' accuracy! Keep Trying <3')

       
def main():
    printChars('x')
    

if __name__ == '__main__':
    main()