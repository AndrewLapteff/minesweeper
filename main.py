from board import Board
from game import Game

size = (9, 9)
prob = 0.2
screenSize = (800, 800)

board = Board(size, prob)
game = Game(board, screenSize)
game.run()
