#!/usr/bin/env python

import os, sys

ALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Y","Z"]
KEY = 3

def main():
    textlines = []
    for line in sys.stdin:
        textlines.append(line)
    textlines = ''.join(textlines)

    if (len(sys.argv[1:]) > 0  ):
        decoding(textlines)
    else:
        coding(textlines)


def coding(myStr):
    newList = ''
    myStr = myStr.upper()
    for item in myStr:
        if item in ALPHA:
            index_alpha = ALPHA.index(item) + KEY
            if len(ALPHA) > index_alpha:
                newList += ALPHA[index_alpha]
            else:
                newList += ALPHA[index_alpha - len(ALPHA)]
        else:
            newList += item
    print(newList)

def decoding(myStr):
    newList = ''
    myStr = myStr.upper()
    for item in myStr:
        if item in ALPHA:
            index_alpha = ALPHA.index(item) - KEY
            if 0 <= index_alpha:
                newList += ALPHA[index_alpha]
            else:
                newList += ALPHA[index_alpha + len(ALPHA)]
        else:
            newList += item
    print(newList)

if __name__ == "__main__":
    main()
