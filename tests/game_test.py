import pytest

from board import Board
from game import Game


@pytest.fixture
def game() -> Game:
    board = Board((9, 9), 0.2)
    screenSize = (800, 800)
    game = Game(board, screenSize)
    return game


def test_draw(game: Game):
    game.draw()
    assert game.board.getWon() == False
    assert game.board.getLost() == False
    assert game.screen.get_width() == 800
    assert game.screen.get_height() == 800


# Клік по верхній лівій клітинці
def test_handleClick(game: Game):
    position = (0, 0)
    rightClick = False
    game.handleClick(position, rightClick)

    piece = game.board.getPiece((0, 0))

    assert piece.getClicked() == True
