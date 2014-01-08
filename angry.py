#!/usr/bin/python

# h = hereillä
# k = kypärä
# l = lintu
# n = nukkuva
# p = punasilmä
# s = säikähtäny

def rot(piece):
    n = 0
    while n < 4:
        new_piece = []
        for coord in piece:
            x = int(coord[1])
            y = int(-1 * coord[0])
            new_piece.append(tuple((x, y)))
        yield new_piece
        piece = new_piece
        n += 1


def print_grid(coordlist, indent=0):
    initial = [["+", "+", "+", "+", "+"],
               ["+", "+", "+", "+", "+"],
               ["+", "+", "+", "+", "+"],
               ["+", "+", "+", "+", "+"],
               ["+", "+", "+", "+", "+"]]
    for coord in coordlist:
        initial[coord[0]][coord[1]] = "#"
    for row in initial:
        print(" " * indent,''.join(row))
    print("---")

if __name__ == '__main__':
    table = [["k", "n", "h", " " , " " ],
             [" " , "s", "k", "p", "h"],
             [" " , "n", "l", "h", "n"],
             ["k", "n", "s", "h", "h"],
             ["p", " " , "k", "s", "n"]]

    one = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
    two = [(0, 0), (1, 0), (1, 1), (0, 2), (1, 2)]
    three = [(1, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
    four = [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)]

    tabledict = dict()
    for x in range(5):
        for y in range(5):
            tabledict[(x, y)] = table[x][y]

    tables = []
    tables.append(tabledict)
    for first in rot(one):
        for x_1 in range(5):
            for y_1 in range(5):
                tables.append(dict(tabledict))
                try:
                    for coord in first:
                        del tabledict[(coord[0] + x_1, coord[1] + y_1)]
                except KeyError:
                    pass
                if len(tabledict) == 20:
                    #print_grid(lIST(TABLEdict.keys()), 0)
                    for second in rot(two):
                        for x_2 in range(5):
                            for y_2 in range(5):
                                tables.append(dict(tabledict))
                                try:
                                    for coord in second:
                                        del tabledict[(coord[0] + x_2, coord[1] + y_2)]
                                except KeyError:
                                    pass
                                if len(tabledict) == 15:
                                    #print_grid(list(tabledict.keys()), 2)
                                    for third in rot(three):
                                        for x_3 in range(5):
                                            for y_3 in range(5):
                                                tables.append(dict(tabledict))
                                                try:
                                                    for coord in third:
                                                        del tabledict[(coord[0] + x_3, coord[1] + y_3)]
                                                except KeyError:
                                                    pass
                                                if len(tabledict) == 10:
                                                    #print_grid(list(tabledict.keys()), 4)
                                                    for fourth in rot(four):
                                                        for x_4 in range(5):
                                                            for y_4 in range(5):
                                                                tables.append(dict(tabledict))
                                                                error = False
                                                                try:
                                                                    for coord in fourth:
                                                                        del tabledict[(coord[0] + x_4, coord[1] + y_4)]
                                                                except KeyError:
                                                                    error = True
                                                                if len(tabledict) == 5:
                                                                    print([x for x in tabledict.values() if x != " "])
                                                                tabledict = dict(tables.pop())
                                                tabledict = dict(tables.pop())
                                tabledict = dict(tables.pop())
                tabledict = dict(tables.pop())
