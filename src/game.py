import os
from time import sleep
from typing import Tuple

import pygame

from board import Board
from piece import Piece


class Game:
    """
    Атрибути:
     board (Board): ігрова дошка
     screenSize (Tuple[int, int]): розмір екрану
     pieceSize (Tuple[int, int]): розмір одного елементу на дошці
     screen (pygame.Surface): поверхня для відображення гри

    Методи:
     __init__(self, board: Board, screenSize: Tuple[int, int]): конструктор класу
     run(self): запускає гру
     draw(self): відображає стан гри на екрані
     loadImages(self): завантажує зображення для елементів гри
     getImage(self, piece: Piece): повертає зображення для заданого елементу
     handleClick(self, position, rightClick): обробляє клік користувача
    """

    def __init__(self, board: Board, screenSize: Tuple[int, int]):
        """
        Ініціалізує об'єкт гри.

        Параметри:
        - board (Board): ігрова дошка
        - screenSize (Tuple[int, int]): розмір екрану
        """
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = (
            self.screenSize[0] // self.board.getSize()[1],
            self.screenSize[1] // self.board.getSize()[0],
        )
        self.loadImages()
        self.screen = pygame.display.set_mode(self.screenSize)

    def run(self) -> None:
        """
        Запускає гру.
        """
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                sleep(3)
                running = False
            if self.board.getLost():
                sound = pygame.mixer.Sound("lose.wav")
                sound.play()
                sleep(2)
                running = False
        pygame.quit()

    def draw(self) -> None:
        """
        Відображає стан гри на екрані.
        """
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadImages(self) -> None:
        """
        Завантажує зображення для елементів гри.
        """
        self.images = {}
        for fileName in os.listdir("images"):
            if not fileName.endswith(".png"):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece: Piece):
        """
        Повертає зображення для заданого елементу.

        Параметри:
        - piece (Piece): елемент гри

        Повертає:
        - pygame.Surface: зображення для елементу
        """
        string = None
        if piece.getClicked():
            string = (
                "bomb-at-clicked-block"
                if piece.getHasBomb()
                else str(piece.getNumAround())
            )
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
        return self.images[string]

    def handleClick(self, position, rightClick) -> None:
        """
        Обробляє клік користувача.

        Параметри:
        - position: позиція кліку
        - rightClick: чи був клік правою кнопкою миші
        """
        if self.board.getLost():
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)
