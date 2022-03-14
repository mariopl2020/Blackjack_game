from person import Player
from deck import cards_deck
from main_game import Game

def test_take_card():
	"""Test checks, if card is taken by player from last index in cards list and correctly count points"""

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
	assert test_player.current_score == first_card_in_deck.value + second_card_in_deck.value


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

