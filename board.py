from random import random
from typing import Tuple

from piece import Piece


class Board:
    def __init__(self, size: Tuple[int, int], prob: float):
        self.size = size
        self.prob = prob
        self.setBoard()

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)

    def getSize(self) -> Tuple[int, int]:
        return self.size

    def getPiece(self, index: Tuple[int, int]):
        return self.board[index[0]][index[1]]
