import pytest

from board import Board
from piece import Piece


def test_board_initialization():
    board = Board((5, 5), 0.2)
    assert board.getSize() == (5, 5)
    assert board.getLost() == False
    assert board.getWon() == False
    assert len(board.board) == 5
    assert len(board.board[0]) == 5
    assert isinstance(board.getPiece((0, 0)), Piece)
