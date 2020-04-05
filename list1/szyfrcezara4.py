#!/usr/bin/env python

import os, sys, getopt

ALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Y","Z"]
KEY = 3

def main(argv):
    try:
        inputfile = ''
        options, remainder = getopt.getopt(sys.argv[1:], '',['decode=', ])
        if options != []:
            for opt, arg in options:
                if opt in ('--decode'):
                    file = openFile(arg)
                    writeFile(decoding(file), arg)
        else:
            file = openFile(remainder[0])
            writeFile(coding(file), remainder[0])
    except Exception as err:
        print(err)

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
    return(newList)

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
    return(newList)

def openFile(fileName):
    with open("./"+fileName, "r") as file:
        ourStringList = []
        for k in (file):
            ourStringList.append(k)
        return("".join(ourStringList))

def writeFile(text, fileName):
    print(text)
    file = open("./"+fileName, "w")
    file.write(text)
    file.close()

if __name__ == "__main__":
    main(sys.argv[1:])
