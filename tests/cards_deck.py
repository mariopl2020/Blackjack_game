from cards_deck import CardsDeck
from card import Card


def test_create_deck_cards_number():
	"""Test checking correctness of total cards number"""

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
		cards_in_colour = [card for card in card_deck.cards if card.colour == colour]
		assert len(cards_in_colour) == cards_number_in_colour


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
	"""Test checks, if cards in cards_deck are shuffled in comparison to primary cards order """

	#GIVEN
	cards_deck = CardsDeck()
	cards_deck.create_deck()
	tested_deck = cards_deck.cards.copy()
	first_card = cards_deck.cards[0]
	tenth_card = cards_deck.cards[9]
	twenth_card = cards_deck.cards[19]

	#WHEN
	cards_deck.shuffle_deck()

	#THEN
	assert all(
		[first_card != cards_deck.cards[0],
		tenth_card != cards_deck.cards[9],
		twenth_card != cards_deck.cards[19]
		]
	)
	assert tested_deck != cards_deck.cards
	assert len(cards_deck.cards) == 52

def test_give_card():
	"""Tests correctness of giving card from the deck"""

	#GIVEN
	cards_deck = CardsDeck()
	#WHEN
	cards_deck.create_deck()
	first_card_for_person = cards_deck.cards[-1]
	second_card_for_person = cards_deck.cards[-2]
	#THEN
	assert cards_deck.give_card() == first_card_for_person
	assert cards_deck.give_card() == second_card_for_person
	assert first_card_for_person not in cards_deck.cards

def test_give_card_count_cards():
	"""Tests if remaining cards number in the deck after giving card is correct"""

	#GIVEN
	cards_deck = CardsDeck()
	cards_number = 50
	#WHEN
	cards_deck.create_deck()
	cards_deck.give_card()
	cards_deck.give_card()
	#THEN
	assert len(cards_deck.cards) == cards_number

	