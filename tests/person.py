from person import Player
from cards_deck import cards_deck
from main_game import Game
from exceptions.game_exceptions import BlackJack

def test_take_card():
	"""Test checks, if card.py is taken by player from last index in cards list and correctly count points"""

	#GIVEN
	test_player = Player()
	cards_deck.create_deck()
	first_card_in_deck = cards_deck.cards[-1]
	second_card_in_deck = cards_deck.cards[-2]

	#WHEN
	test_player.take_card()
	test_player.take_card()

	#THEN
	assert test_player.person_cards[0] == first_card_in_deck
	assert test_player.person_cards[1] == second_card_in_deck
	assert len(cards_deck.cards) == 50
	assert test_player.current_score == first_card_in_deck.value + second_card_in_deck.value
	assert test_player.person_cards[0] not in cards_deck.cards


def test_check_if_black_jack():
	"""Checks what happens when player has blackjack, how many points he has and if croupier's card.py deck is empty """

	#GIVEN
	test_game = Game()
	cards_deck.create_deck()
	#WHEN
	try:
		test_game.first_distribution()
	except BlackJack as ex:
		pass
	#THEN
	assert test_game.player1.current_score == 21
	# assert test_game.croupier1.person_cards == []

#TO DO
# def test_take_another_cards():
# 	""""""
# 	#GIVEN
# 	test_game = Game()
#
# 	#WHEN
# 	cards_deck.create_deck()
# 	test_game.first_distribution()
# 	test_game.player1.ask_about_another_cards()
#
# 	#THEN
# 	assert  test_game.player1.take_another_cards() ==

