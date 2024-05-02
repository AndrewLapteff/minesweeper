import pytest

from src.piece import Piece


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


def test_piece_toggle_flag(piece: Piece):
    piece.toggleFlag()
    assert piece.getFlagged() == True
    piece.toggleFlag()
    assert piece.getFlagged() == False


def test_piece_click(piece: Piece):
    piece.click()
    assert piece.getClicked() == True


def test_piece_set_num_around(piece: Piece):
    neighbors = [Piece(False), Piece(True)]
    piece.setNeighbors(neighbors)
    assert piece.getNumAround() == 1


def test_piece_get_clicked(piece: Piece):
    assert piece.getClicked() == False
    piece.click()
    assert piece.getClicked() == True


def test_piece_get_flagged(piece: Piece):
    assert piece.getFlagged() == False
    piece.toggleFlag()
    assert piece.getFlagged() == True


def test_piece_get_num_around(piece: Piece):
    neighbors = [Piece(False), Piece(True)]
    piece.setNeighbors(neighbors)
    assert piece.getNumAround() == 1
    neighbors.append(Piece(True))
    piece.setNeighbors(neighbors)
    assert piece.getNumAround() == 3


def test_piece_get_has_bomb(piece: Piece):
    assert piece.getHasBomb() == False
    piece = Piece(True)
    assert piece.getHasBomb() == True

