#!/usr/bin/env python
import os
import string

def main(fileName):
    wordList = dict()
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + fileName
    with open(dir_path,"r") as input_file:
        for words in input_file:
            unnecessarySimbols = str(string.punctuation)
            words = deleteSimbols(words, unnecessarySimbols)
            words = words.lower()
            words = words.split(" ")
            for word in words:
                if word not in wordList:
                    wordList[word] = 1
                else:
                    wordList[word] += 1

    sortedList = sorted(wordList.items(), key = lambda count: count[1], reverse=True)
    printList(sortedList[0:11])

def printList(list):
    for item in list:
        print(item)

def deleteSimbols(text, simbols):
    for simbol in simbols:
        text = text.replace(simbol,"")
    return(text)

if __name__ == '__main__':
    # file has to be in the same directory py file
    main("someWords.txt")
