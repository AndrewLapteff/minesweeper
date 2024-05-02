from random import random
from typing import Tuple

from piece import Piece


class Board:
    def __init__(self, size: Tuple[int, int], prob: float):
        """
        Ініціалізує новий екземпляр дошки.

        Аргументи:
            size (Tuple[int, int]): Розміри дошки (рядки, стовпці).
            prob (float): Ймовірність того, що комірка містить бомбу.

        Повертає:
            None
        """
        self.size = size
        self.prob = prob
        self.lost = False

        self.numClicked = 0
        self.numNonBombs = 0
        self.setBoard()

    def setBoard(self):
        """
        Налаштовує дошку з випадковим розташуванням бомб на основі заданої ймовірності.

        Аргументи:
            None

        Повертає:
            None
        """
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if not hasBomb:
                    self.numNonBombs += 1
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()

    def setNeighbors(self):
        """
        Встановлює сусідні комірки для кожної комірки на дошці.

        Аргументи:
            None

        Повертає:
            None
        """
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getListOfNeighbors(self, index):
        """
        Повертає список сусідніх шматків для вказаної комірки.

        Аргументи:
            index (Tuple[int, int]): Індекс комірки, для якої потрібно отримати сусідів.

        Повертає:
            List[Piece]: Список сусідніх шматків.
        """
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = (
                    row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                )
                same = row == index[0] and col == index[1]
                if same or outOfBounds:
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors

    def getSize(self) -> Tuple[int, int]:
        """
        Повертає розмір дошки.

        Аргументи:
            None

        Повертає:
            Tuple[int, int]: Розміри дошки (рядки, стовпці).
        """
        return self.size

    def getPiece(self, index: Tuple[int, int]):
        """
        Повертає шматок за вказаним індексом на дошці.

        Аргументи:
            index (Tuple[int, int]): Індекс комірки, яку потрібно отримати.

        Повертає:
            Piece: Об'єкт шматка за вказаним індексом.
        """
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        """
        Обробляє клік по комірці, перемикає прапорець, якщо вказано, і рекурсивно відкриває сусідні комірки.

        Аргументи:
            piece (Piece): Комірка, на яку було клікнуто.
            flag (bool): True, якщо вказано дію з прапорцем, False в іншому випадку.

        Повертає:
            None
        """
        if piece.getClicked() or (not flag and piece.getFlagged()):
            return
        if flag:
            piece.toggleFlag()
            return
        piece.click()
        if piece.getHasBomb():
            self.lost = True
            return
        self.numClicked += 1
        if piece.getNumAround() != 0:
            return
        for neighbor in piece.getNeighbors():
            if not neighbor.getHasBomb() and not neighbor.getClicked():
                self.handleClick(neighbor, False)

    def getLost(self):
        """
        Повертає, чи виграно гру.

        Аргументи:
            None

        Повертає:
            bool: True, якщо гра програна, False в іншому випадку.
        """
        return self.lost

    def getWon(self):
        """
        Повертає, чи виграно гру.

        Аргументи:
            None

        Повертає:
            bool: True, якщо всі комірки без бомб відкриті, False в іншому випадку.
        """
        return self.numNonBombs == self.numClicked
