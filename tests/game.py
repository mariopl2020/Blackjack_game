import pytest

from game import Game
from card import Card
from exceptions.game_exceptions import DrawException, BlackJack


def test_check_if_blackjack_draw():
	"""Test checks when is blackjack draw after first taking cards, program raises an appropriate exception"""

	#GIVEN
	test_game = Game()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("A", "heart")
	test_card3 = Card("A", "spade")
	test_card4 = Card("A", "club")
	test_game.player1.take_card(test_card1)
	test_game.player1.take_card(test_card2)
	test_game.croupier1.take_card(test_card3)
	test_game.croupier1.take_card(test_card4)
	with pytest.raises(DrawException) as exception:
		#WHEN
		test_game.check_if_blackjack_draw()
		#THEN
		assert test_game.player1.current_score == test_game.croupier1.current_score == 21
		assert exception == "You have the same score. BlackJack draw!"


def test_first_distribution():
	"""Tests if after first distribution of cards users have correct points amount and card deck is decreased by\
	given cards"""

	#GIVEN
	test_game = Game()
	test_card1 = Card("9", "diamond")
	test_card2 = Card("K", "heart")
	test_card3 = Card("2", "spade")
	test_card4 = Card("A", "club")
	test_game.cards_deck.cards = [test_card1, test_card2, test_card3, test_card4]
	#WHEN
	test_game.first_distribution()
	#THEN
	assert test_game.croupier1.current_score == 19
	assert test_game.player1.current_score == 13
	assert test_game.cards_deck.cards == []


def test_first_distribution_four_aces():
	"""Tests if method raise correct exception when both persons have two aces"""

	#GIVEN
	test_game = Game()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("A", "heart")
	test_card3 = Card("A", "spade")
	test_card4 = Card("A", "club")
	test_game.cards_deck.cards = [test_card1, test_card2, test_card3, test_card4]
	with pytest.raises(DrawException) as exception:
		#WHEN
		test_game.first_distribution()
		#THEN
		assert test_game.player1.current_score == test_game.croupier1.current_score == 21
		assert exception == "You have the same score. BlackJack draw!"


def test_first_distribution_player_two_aces():
	"""Tests if method raise correct exception when player have two aces"""

	#GIVEN
	test_game = Game()
	test_card1 = Card("K", "diamond")
	test_card2 = Card("K", "heart")
	test_card3 = Card("A", "spade")
	test_card4 = Card("A", "club")
	test_game.cards_deck.cards = [test_card1, test_card2, test_card3, test_card4]
	with pytest.raises(BlackJack) as exception:
		#WHEN
		test_game.first_distribution()
		#THEN
		assert test_game.player1.current_score == 21
		assert exception == "Player have black jack"


def test_first_distribution_croupier_two_aces():
	"""Tests if method raise correct exception when croupier have two aces"""

	#GIVEN
	test_game = Game()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("A", "heart")
	test_card3 = Card("K", "spade")
	test_card4 = Card("K", "club")
	test_game.cards_deck.cards = [test_card1, test_card2, test_card3, test_card4]
	with pytest.raises(BlackJack) as exception:
		#WHEN
		test_game.first_distribution()
		#THEN
		assert test_game.croupier1.current_score == 21
		assert exception == "Croupier have black jack"


# def show_both_cards_and_points(self):
# 	""""""
#
# 	#GIVEN
# 	#WHEN
# 	#THEN
#
# 	def show_both_cards_and_points(self):
# 		"""Grouped representation of player and croupier points and cards"""
#
# 		self.player1.show_person_cards()
# 		self.player1.show_current_score()
# 		self.croupier1.show_person_cards()
# 		self.croupier1.show_current_score()