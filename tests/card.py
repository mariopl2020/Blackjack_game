import pytest
from card import Card

def test_card_creation():
	"""Testing creation of card object with correct parameters"""

	#GIVEN
	card = Card("A", "diamond")
	#WHEN
	#THEN
	assert card.name == "A"
	assert card.value == 11
	assert card.colour == "diamond"


def test_creation_wrong_value():
	"""Testing creation of card object with invalid card name parameter"""

	#GIVEN
	with pytest.raises(IndexError) as exception:
		wrong_card = Card("ACE", "heart")
	#WHEN
	#THEN
		assert exception == "Entered wrong card name"

def test_creation_wrong_colour():
	"""Testing creation of card object with invalid card colour parameter"""

	#GIVEN
	with pytest.raises(ValueError) as exception:
		card_with_wrong_colour = Card("A", "brown")
	#WHEN
	#THEN
		assert exception == "Entered wrong card colour"