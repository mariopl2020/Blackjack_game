from player import Player
from deck import cards_deck

def test_take_card():
	"""Test checks, if card is taken by player from last index in cards list and correctly count points"""

	#GIVEN
	player1 = Player()
	cards_deck.create_deck()
	first_card_in_deck = cards_deck.cards[-1]
	second_card_in_deck = cards_deck.cards[-2]

	#WHEN
	player1.take_card()
	player1.take_card()

	#THEN
	assert player1.person_cards[0] == first_card_in_deck
	assert player1.person_cards[1] == second_card_in_deck
	assert player1.current_score == first_card_in_deck.value + second_card_in_deck.value