from deck import CardsDeck

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

def test_shuffle_deck():
	"""Test checks, if cards in deck are shuffled in comparison to primary cards order """

	#GIVEN
	deck = CardsDeck()
	deck.create_deck()
	tested_deck = deck.cards.copy()
	first_card = deck.cards[0]
	tenth_card = deck.cards[9]
	twenth_card = deck.cards[19]

	#WHEN
	deck.shuffle_deck()

	#THEN
	assert all(
		[first_card != deck.cards[0],
		 tenth_card != deck.cards[9],
		 twenth_card != deck.cards[19]
		]
	)
	assert tested_deck != deck.cards
	assert len(deck.cards) == 52