import sys

import pytest

sys.path.append("src")

from piece import Piece
from src.board import Board


@pytest.fixture
def board():
    return Board((5, 5), 0.2)


def test_board_initialization(board):
    assert board.getSize() == (5, 5)
    assert board.getLost() == False
    assert board.getWon() == False
    assert len(board.board) == 5
    assert len(board.board[0]) == 5
    assert isinstance(board.getPiece((0, 0)), Piece)


def test_handleClick(board):
    piece = board.getPiece((0, 0))
    board.handleClick(piece, False)
    assert piece.getClicked() == True


def test_getListOfNeighbors(board):
    neighbors = board.getListOfNeighbors((2, 2))
    assert len(neighbors) == 8
    assert all(isinstance(n, Piece) for n in neighbors)


def test_setNeighbors(board):
    piece = board.getPiece((2, 2))
    assert len(piece.getNeighbors()) == 8
    assert all(isinstance(n, Piece) for n in piece.getNeighbors())


def test_getListOfNeighbors_edge(board: Board):
    neighbors = board.getListOfNeighbors((0, 0))
    assert len(neighbors) == 3
    assert all(isinstance(n, Piece) for n in neighbors)


def test_getSize(board: Board):
    assert board.getSize() == (5, 5)


def test_getPiece(board: Board):
    assert isinstance(board.getPiece((0, 0)), Piece)


def test_getLost(board: Board):
    assert board.getLost() == False


def test_getWon(board: Board):
    assert board.getWon() == False
