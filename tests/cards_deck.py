from cards_deck import CardsDeck
from card import Card


def test_create_deck():
	"""Test checking correctness of total cards number, one type of figure and one type of colour
	"""

	#GIVEN
	cards_number = 52
	card_deck = CardsDeck()
	#WHEN
	card_deck.create_deck()
	#THEN
	assert len(card_deck.cards) == cards_number


def test_create_deck_colours():
	"""Testing, if created deck has appropriate number of cards in each colour"""

	#GIVEN
	card_deck = CardsDeck()
	cards_number_in_colour = 13
	#WHEN
	card_deck.create_deck()
	#THEN
	for colour in Card.POSSIBLE_COLOURS:
		card_in_colour = [card for card in card_deck.cards if card.colour == colour]
		assert len(card_in_colour) == cards_number_in_colour


def test_create_deck_name():
	"""Testing, if created deck has appropriate number of of cards in each figure"""

	#GIVEN
	card_deck = CardsDeck()
	cards_number_in_figure = 4
	#WHEN
	card_deck.create_deck()
	#THEN
	for figure in Card.POSSIBLE_FIGURES:
		cards_in_figure = [card for card in card_deck.cards if card.name == figure]
		assert len(cards_in_figure) == cards_number_in_figure


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