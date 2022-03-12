from cards_deck import CardsDeck


def test_create_deck():
	"""Test checking correctness of total cards number, one type of figure and one type of colour
	"""

	#GIVEN
	card_number = 52
	ace_counter = 0
	#WHEN
	card_deck = CardsDeck()
	card_deck.create_deck()
	list_of_colours = [card.colour for card in card_deck.cards]
	for card in card_deck.cards:
		if card.name == "Q":
			ace_counter += 1
	#THEN
	assert len(card_deck.cards) == card_number
	assert ace_counter == 4
	assert list_of_colours.count("diamond") == 13
