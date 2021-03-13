#!/usr/bin/env python
import random

# Ships in the game:
# BATTLESHIP - 1
# CRUISER - 2
# DESTROYER -3
# SUBMARINE -4

#BOARD = [[0]*SIZE]*SIZE - nie dziala

class CreateBoard():
    """Creating a board """
    SHIPS = [{"ship_sign": "4",
                "length": 4,
                "number": 1},
            {"ship_sign": "3",
                "length": 3,
                "number": 2},
            {"ship_sign": "2",
                "length": 2,
                "number": 3},
            {"ship_sign": "1",
                "length": 1,
                "number": 4}
            ]

    SIZE = 10
    BOARD = [['0' for column in range(10)] for row in range(10)]

    def __init__(self, board=BOARD, ships=SHIPS):
        ships_list = []
        for ship in ships:
            for n in range(ship["number"]):
                board, ships_list = self.add_ship(board, ship["length"], ship["ship_sign"], ships_list)
        self.board = board
        self.ships_list = ships_list
        print(ships_list)

    def return_board(self):
        return self.board

    def return_ships_position(self):
        return(self.ships_list)

    def print_board(self):
        for k in self.board:
            print(k)
        #print(self.board)
    def print_ships_position(self):
        for k in self.ships_list:
            print(k)

    def add_ship(self, board, ship_len, ship_sign, ships_list):
        row = random.randint(0, len(board) - 1)
        column = random.randint(0, len(board[1]) - 1)

        if ship_len != 1:
            ship_list = self.choose_position(row, column, ship_len)
        else:
            ship_list = [[row, column]]

        if self.choice_ok(board, ship_list):
            board = self.add_to_board(board, ship_list, ship_sign)
            ships_list.append(ship_list)
        else:
            # funkcja rekurencyjna
            self.add_ship(board, ship_len, ship_sign, ships_list)
        return(board, ships_list)

    def choose_position(self, row, column, ship_len):
        direction = random.choice(["UP","DOWN","LEFT", "RIGHT"])

        ship_list = []
        if direction == "UP":
            #[[x,y],[x-1,y],[x-2,y],[x-3,y]]
            for l in range(ship_len):
                ship_list.append([row - l, column])

        elif direction == "DOWN":
            #[[x,y],[x+1,y],[x+2,y],[x+3,y]]
            for l in range(ship_len):
                ship_list.append([row + l, column])

        elif direction == "LEFT":
            #[[x,y],[x,y-1],[x,y-2],[x,y-3]]
            for l in range(ship_len):
                ship_list.append([row, column - l])

        elif direction == "RIGHT":
            #[[x,y],[x,y+1],[x,y+2],[x,y+3]]
            for l in range(ship_len):
                ship_list.append([row, column + l])
        else:
            print("ERROR")

        return(ship_list)

    def ship_in_board(self, ship_list):
        for ship in ship_list:
            for s in ship:
                if (s < 0 or s > 9):
                    return(False)
        return(True)

    def ship_near(self, board, ship_list):
        neighbours = [[-1, -1], [-1,  0],[-1, 1],
                      [ 0, -1], [ 0,  0],[ 0, 1],
                      [ 1, -1], [ 1,  0],[ 1, 1]]
        for ship_part in ship_list:

            for neigh in neighbours:
                if (ship_part[0] + neigh[0] < 0  or
                        ship_part[0] + neigh[0] > 9 or
                        ship_part[1] + neigh[1] < 0  or
                        ship_part[1] + neigh[1] > 9):
                    continue

                if board[ship_part[0] + neigh[0]][ship_part[1] + neigh[1]] != '0':
                    return(True)
        return(False)

    def choice_ok(self, board, ship_list):
        if self.ship_in_board( ship_list) == False:
            return(False)
        if self.ship_near(board, ship_list) == True:
            return(False)
        return(True)

    def add_to_board(self, board, ship_list, ship_sign):
        for each_ship in ship_list:
            board[each_ship[0]][each_ship[1]] = ship_sign
        return(board)

if __name__ == '__main__':
    b = CreateBoard()
    #b.print_board()
    #b.print_ships_position()
