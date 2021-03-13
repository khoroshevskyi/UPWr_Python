#!/usr/bin/env python

import os, sys, getopt
import optparse
import ast
import random


# '0' - pusto
# '1' - statek
# '2' - pudlo
# '8' - trafione
# '9' - zatopione


class Gracz(object):
    board_names = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                   'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

    board = [['0' for column in range(10)] for row in range(10)]

    opponent_board = [['0' for column in range(10)] for row in range(10)]
    current_buttle = []

    def __init__(self, options):
        # print("Lest start the game!")

        if options['filename'] != "" and options['filename'] != '-s':
            ships_pos = self.open_file(options['filename'])
        else:
            ships_pos = self.open_file('ustawienia.txt')

        self.create_board(ships_pos)
        self.ships_pos = ships_pos
        self.ships_killed = []
        self.computer_steps = []

        koniec = self.game_start(options['start'])
        print(koniec, " Won the game! Congratulations")

    # method for opening file with ship configuration
    def open_file(self, file_name):
        file_object = open(file_name, "r")
        for file_string in file_object:
            string_arr = file_string
        file_object.close()

        # ast is used to convert string to array
        return ast.literal_eval(string_arr)

    # filling board variable with predefined locations
    def create_board(self, loc):
        for ship in loc:
            for ship_pos in ship:
                self.board[ship_pos[0]][ship_pos[1]] = '1'

        # for b in self.board:
        #    print(b)

    def game_start(self, who_starts):
        # if who_starts == True, than user, who starts program - starts game
        while True:
            if who_starts:
                if self.user_move() == "koniec":
                    return "User"

                if self.computer_move() == "koniec":
                    return "Computer"
            else:
                if self.computer_move() == "koniec":
                    return "Computer"

                if self.user_move() == "koniec":
                    return "User"

    def user_move(self):
        # print("Your move:")
        while True:
            try:
                move = input("")

                col = self.board_names[move[0]]
                row = int(move[1:]) - 1

                if self.board[row][col] == "1":
                    result = self.check_ship([row, col])
                    print(result)

                else:
                    self.board[row][col] == "2"
                    print("pudlo_")
                    return "pudlo_"

                if self.game_over() == True:
                    print("koniec")
                    return "koniec"

            except Exception as err:
                print("blad__", err)

    def check_ship(self, place):
        n = -1
        while n < len(self.ships_pos) - 1:
            n += 1
            m = -1
            while m < len(self.ships_pos[n]) - 1:
                m += 1
                if self.ships_pos[n][m] == place:
                    self.ships_killed.append(place)
                    self.board[place[0]][place[1]] = "9"

                    # for s in self.board:
                    #     print(s)

                    del self.ships_pos[n][m]

                    if len(self.ships_pos[n]) == 0:
                        del self.ships_pos[n]
                        return "zatop_"
                    else:
                        return "trafio"

    def game_over(self):
        if len(self.ships_pos) == 0:
            return True
        return False

    def computer_move(self):
        "Computer move:"
        try:
            while True:
                current_move = self.generate_move()
                print(current_move)
                u_move = input("")
                if u_move == "pudlo_":
                    return ""

                if u_move == "koniec":
                    return "koniec"
        except Exception as err:
            print(f"error: {err}")

    # method to generate shoot that has to be done by computer
    def generate_move(self):
        # print("generator works")

        current_move = ''
        row = random.randint(0, 9)
        column = random.randint(0, 9)

        if [row, column] not in self.computer_steps:

            self.computer_steps.append([row, column])
            for key, value in self.board_names.items():
                if value == row:
                    current_move += key
                    break
        else:
            if len(self.computer_steps) != 100:
                print("We have to specify another value!")
                return self.generate_move()

        if column > 8:
            current_move += str(column + 1)
        else:
            current_move += ("0" + str(column + 1))
        return current_move


def get_arg():
    parser = optparse.OptionParser()

    parser.add_option("-u", "--ustawienia", dest="filename", default='',
                      help="File that contains ships positions, earlier generated")
    parser.add_option("-s", "--start",
                      action="store_true", default=False,
                      help="Player can start the game first")

    (options, args) = parser.parse_args()
    return vars(options)


if __name__ == "__main__":
    Gracz(get_arg())
