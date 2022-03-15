from person import Person
from card import Card
from cards_deck import CardsDeck
from main_game import Game
from exceptions.game_exceptions import BlackJack

def test_take_card():
	"""Tests if taken card is correctly added to person's cards list"""

	#GIVEN
	test_person = Person()
	test_card1 = Card("J", "heart")
	test_card2 = Card("9", "diamond")
	#WHEN
	test_person.take_card(test_card1)
	test_person.take_card(test_card2)
	#THEN
	assert test_card1 in test_person.person_cards
	assert test_card2 in test_person.person_cards


def test_take_card_from_cards_deck():
	"""Test checks, if card is taken by person from last index in cards list"""

	#GIVEN
	test_person = Person()
	cards_deck = CardsDeck()
	cards_deck.create_deck()
	first_card_in_deck = cards_deck.give_card()
	second_card_in_deck = cards_deck.give_card()

	#WHEN
	test_person.take_card(first_card_in_deck)
	test_person.take_card(second_card_in_deck)

	#THEN
	assert test_person.person_cards[0] == first_card_in_deck
	assert test_person.person_cards[1] == second_card_in_deck
	assert len(cards_deck.cards) == 50
	assert test_person.person_cards[0] not in cards_deck.cards

def test_take_card_check_score():
	"""Checks if after taking single cards current score changes correctly"""

	#GIVEN
	test_person = Person()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("2", "diamond")
	test_card3 = Card("A", "spade")

	#WHEN
	test_person.take_card(test_card1)
	#THEN
	assert test_person.current_score == 11
	#WHEN
	test_person.take_card(test_card2)
	#THEN
	assert test_person.current_score == 13
	#WHEN
	test_person.take_card(test_card3)
	#THEN
	assert test_person.current_score == 4

def test_calculate_points_two_aces():
	"""Test points calculation in case of 2 aces"""

	#GIVEN
	test_person = Person()
	test_card1 = Card("A", "heart")
	test_card2 = Card("A", "diamond")
	points = 21
	#WHEN
	test_person.take_card(test_card1)
	test_person.take_card(test_card2)
	calculated_points = test_person.calculate_points()
	#THEN
	assert calculated_points == points
	assert test_person.aces_number == 2


def test_calculate_points_one_ace_two_cards():
	"""Tests points calculation in case of ace and one other card"""

	#GIVEN
	test_person = Person()
	test_card1 = Card("9", "heart")
	test_card2 = Card("A", "diamond")
	points = 20
	#WHEN
	test_person.take_card(test_card1)
	test_person.take_card(test_card2)
	#THEN
	assert test_person.calculate_points() == points
	assert test_person.aces_number == 1


def test_calculate_points_one_ace_three_cards():
	"""Tests points calculation in case of one ace and two or more other cards"""

	#GIVEN
	test_player = Person()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("2", "heart")
	test_card3 = Card("3", "heart")
	points = 6
	#WHEN
	test_player.take_card(test_card1)
	test_player.take_card(test_card2)
	test_player.take_card(test_card3)
	#THEN
	assert test_player.calculate_points() == points
	assert test_player.aces_number == 1

# def test_check_if_black_jack():
# 	"""Checks what happens when player has blackjack, how many points he has and if croupier's card.py deck is empty """
#
# 	#GIVEN
# 	test_game = Game()
# 	cards_deck = CardsDeck()
# 	cards_deck.create_deck()
# 	#WHEN
# 	try:
# 		test_game.first_distribution()
# 	except BlackJack as ex:
# 		pass
# 	#THEN
# 	assert test_game.player1.current_score == 21
# 	# assert test_game.croupier1.person_cards == []



