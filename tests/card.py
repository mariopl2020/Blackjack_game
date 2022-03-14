"""Card class tests"""
import pytest

from card import Card
from exceptions.card_exception import InvalidColour, InvalidName

def test_card_creation():
    """Testing creation of card object with correct parameters"""

    #GIVEN
    card = Card("A", "diamond")
    #WHEN
    #THEN
    assert card.name == "A"
    assert card.value == 11
    assert card.colour == "diamond"

def test_card_creation_wrong_name():
    """Testing creation of card object with invalid card name parameter"""

    #GIVEN
    with pytest.raises(InvalidName) as exception:
        Card("ACE", "heart")
    #WHEN
    #THEN
        assert exception == "Entered wrong card name"

def test_card_creation_wrong_colour():
    """Testing creation of card object with invalid card colour parameter"""

    #GIVEN
    with pytest.raises(InvalidColour) as exception:
        Card("A", "brown")
    #WHEN
    #THEN
        assert exception == "Entered wrong card colour"

def test_card_representation():
    """Testing card's text representation"""

    #GIVEN
    test_card = Card("K", "heart")
    #WHEN
    #THEN
    assert repr(test_card) == "K heart"
