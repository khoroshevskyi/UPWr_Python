#!/usr/bin/env python

from generator import *
import sys
import ast
#import generator

class Wyswietlacz():

    def __init__(self, loc):
        board = self.ship_loc_to_board(loc)
        board_strings_list = self.add_name_col()
        board_strings_list = self.add_ships(board_strings_list, board)
        self.print_board(board_strings_list)

    def ship_loc_to_board(self, loc):
        board = [['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0']]
        for ship in loc:
            for ship_pos in ship:
                board[ship_pos[0]][ship_pos[1]] = 'XX'

        return(board)

    def add_name_col(self):
        col_name_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        start = ["---|", "----"]
        for col_name in col_name_list:
            first_str = " " + col_name + "  |"
            start[0] +=  first_str
            start[1] += "-----"
        return(start)

    def add_ships(self, board_strings_list, board):
        row_name = 0
        for board_row in board:
            row_name += 1
            if len(str(row_name)) == 1:
                row_name_s = '0' + str(row_name)
            else:
                row_name_s = str(row_name)
            row_str = row_name_s + ' |'

            for board_element in board_row:
                if board_element != '0':
                    symbol = board_element + ""
                else:
                    symbol = '  '
                row_str += " " + symbol + " |"

            board_strings_list.append(row_str)
            board_strings_list.append(board_strings_list[1])

        return(board_strings_list)

    def print_board(self, board_strings_list):
        for st in board_strings_list:
            print(st)

if __name__ == "__main__":
    # if you want to take vales like .\generator.py | .\wyswietlacz.py:

    for line in sys.stdin:
        pass
    loc = ast.literal_eval(line)

    # if you want to get board without terminal do this:
    #loc = CreateBoard().return_ships_position()
    #Wyswietlacz(loc)
