# TODO:
# make a game with gui
# enable game actions

import numpy as np


class board:
    """
    counstracts a new board
    """

    def __init__(self):
        # board
        # none = 0 empty = 1, white = 2, black = 3
        self.entries = np.array(
            [
                [2, 2, 2, 2, 2, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 0, 0, 0],
                [1, 1, 2, 2, 2, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 3, 3, 3, 1, 1, 0, 0],
                [3, 3, 3, 3, 3, 3, 0, 0, 0],
                [3, 3, 3, 3, 3, 0, 0, 0, 0],
            ],
            dtype=int,
        )

        # possible moves
        self.moves1 = {}
        self.moves2 = {}
        self.moves3 = {}

    """
    param the row
    returns the length of the row
    """

    def row_length(row):
        if row < 5:
            return row + 5
        else:
            return 13 - row

    """
    param potential move
    return if that move is legal
    """

    def legal_moves(self, color):
        pass

    """
    """

    def gen_neighbors(self, row, index):
        res = []

        #
        if row == 0:
            if index > 0:
                res.append((row, index - 1))
            if index < 4:
                res.append((row, index + 1))
            res.append((row + 1, index))
            res.append((row + 1, index + 1))
        elif row == 8:
            if index > 0:
                res.append((row, index - 1))
            if index < 4:
                res.append((row, index + 1))
            res.append((row - 1, index))
            res.append((row - 1, index + 1))
        else:
            if index > 0:
                res.append((row, index - 1))
            if index < self.row_length(row) - 1:
                res.append((row, index + 1))
            if row < 4:
                res.append((row + 1, index))
                res.append((row + 1, index + 1))
                if index > 0:
                    res.append((row - 1, index - 1))
                if index < self.row_length(row) - 1:
                    res.append((row - 1, index))
            if row > 4:
                res.append((row - 1, index))
                res.append((row - 1, index + 1))
                if index > 0:
                    res.append((row + 1, index - 1))
                if index < self.row_length(row) - 1:
                    res.append((row + 1, index))
            if row == 4:
                if index > 0:
                    res.append((row + 1, index - 1))
                if index < self.row_length(row) - 1:
                    res.append((row + 1, index))
        return res
