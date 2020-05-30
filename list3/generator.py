#!/usr/bin/env python

import random
BOARDLENGTH = 10

class Generator():
    def __init__(self):
        self.create_empty_board()
        self.print_Board()

    def create_empty_board(self):
        self.listOfStrings2 = [[0 for i in range(BOARDLENGTH)] for k in range(BOARDLENGTH)]
        print("This is my generator")

    def generate_ship_place(self):
        pass

    def check_distance(self):
        pass

    def write_to_file(self, file_name):
        my_file = open("./"+file_name, "w+")

        my_file.close()

    def print_Board(self):
        for line in self.listOfStrings2:
            print(line)

if __name__ == '__main__':
    first = Generator()

import random
for k in range(0,10):
    print("+"+"---+"*10)
    for b in range(0,10):
        f = random.choice(["   ","   ", "XXX"])
        print(("|"+f), end="")
    print("|\n", end="")
print("+"+"---+"*10)
