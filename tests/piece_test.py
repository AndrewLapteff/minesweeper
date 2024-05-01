import pytest

from piece import Piece


@pytest.fixture
def piece():
    return Piece(False)


def test_piece_initialization(piece: Piece):
    assert piece.getHasBomb() == False
    assert piece.getClicked() == False
    assert piece.getFlagged() == False
    assert piece.getNumAround() == 0


def test_piece_set_neighbors(piece: Piece):
    neighbors = [Piece(False), Piece(True)]
    piece.setNeighbors(neighbors)
    assert piece.getNeighbors() == neighbors
    assert piece.getNumAround() == 1


def test_piece_get_neighbors(piece: Piece):
    neighbors = [Piece(False), Piece(True)]
    piece.setNeighbors(neighbors)
    assert piece.getNeighbors() == neighbors
