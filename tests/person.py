from person import Person, Player, Croupier
from card import Card
from cards_deck import CardsDeck
from game import Game
from exceptions.game_exceptions import BlackJack, ExceededLimit, CroupierWin, DrawException
import pytest


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


def test_check_if_black_jack_two_aces():
	"""Checks if is raised blackjack exception with 2 aces created manually"""

	# GIVEN
	test_card01 = Card("A", "diamond")
	test_card02 = Card("A", "heart")
	test_person = Person()
	test_person.take_card(test_card01)
	test_person.take_card(test_card02)

	with pytest.raises(BlackJack) as exception:
		# WHEN
		test_person.check_if_black_jack()
		# THEN
		assert exception == "You have black jack"
		assert test_person.current_score == 21


def test_check_if_black_jack_with_deck():
	"""""Checks if is raised blackjack exception with deck created manually without shuffle"""""

	# GIVEN
	test_deck = CardsDeck()
	test_deck.create_deck()
	test_card01 = test_deck.give_card()
	test_card02 = test_deck.give_card()
	test_person = Person()
	test_person.take_card(test_card01)
	test_person.take_card(test_card02)

	with pytest.raises(BlackJack) as exception:
		# WHEN
		test_person.check_if_black_jack()
		# THEN
		assert exception == "You have black jack"
		assert test_person.current_score == 21


def test_show_person_cards():
	"""Tests correctness of showed person's cards"""

	#GIVEN
	test_person = Person()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("9", "spade")
	test_person.take_card(test_card1)
	test_person.take_card(test_card2)
	#WHEN
	#THEN
	assert test_person.show_person_cards() == print("Person's cards: 9 spade, A diamond")


def test_show_current_score():
	"""Tests correctness of showed person's score"""

	#GIVEN
	test_person = Person()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("3", "spade")
	test_person.take_card(test_card1)
	test_person.take_card(test_card2)
	#WHEN
	#THEN
	assert test_person.show_current_score() == print("Person's score: 14")


def test_check_if_exceed_limit():
	"""Tests if points limit is exceeded, exception is raised"""

	#GIVEN
	test_person = Player()
	test_card1 = Card("9", "diamond")
	test_card2 = Card("3", "spade")
	test_card3 = Card("K", "spade")
	test_person.take_card(test_card1)
	test_person.take_card(test_card2)
	test_person.take_card(test_card3)
	#WHEN
	#THEN
	assert test_person.current_score == 22
	with pytest.raises(ExceededLimit) as exception:
		test_person.check_if_exceed_limit(points_limit=21)
		assert exception == "You have more than 21 points. You lost!"
		assert test_person.show_current_score() == print("Person's score: 22")


def test_take_another_cards():
	"""Tests if taking another cards one by one correctly adding them to player and counts points"""

	test_person = Player()
	test_card1 = Card("9", "diamond")
	test_card2 = Card("3", "spade")
	test_card3 = Card("K", "spade")
	#WHEN
	test_person.take_another_cards(test_card1)
	#THEN
	assert test_person.person_cards == [test_card1]
	assert test_person.current_score == 9
	#WHEN
	test_person.take_another_cards(test_card3)
	#THEN
	assert test_person.person_cards == [test_card1, test_card3]
	assert test_person.current_score == 19
	#WHEN
	test_person.take_another_cards(test_card2)
	#THEN
	assert test_person.person_cards == [test_card1, test_card3, test_card2]
	assert test_person.current_score == 22


def test_take_cards_algorithm_draw_without_card_taking():
	"""Tests, if draw exception is raised, when player, croupier and limit points are the same"""

	#GIVEN
	test_croupier = Croupier()
	test_card1 = Card("A", "diamond")
	test_card2 = Card("K", "spade")
	test_card3 = Card("2", "heart")
	test_croupier.take_card(test_card1)
	test_croupier.take_card(test_card2)
	#WHEN
	with pytest.raises(DrawException) as exception:
		test_croupier.take_cards_algorithm(player_score=21, points_limit=21, card=test_card3)
		#THEN
		assert exception == "Both players has the same points - 21 as limit. Draw!"
		assert test_croupier.current_score == 21
		assert test_card3 not in test_croupier.person_cards


def test_take_cards_algorithm_draw_after_taking_one_card():
	"""Tests, if draw exception is raised, when player, croupier and limit points are the same"""

	#GIVEN
	test_croupier = Croupier()
	test_card1 = Card("9", "diamond")
	test_card2 = Card("K", "spade")
	test_card3 = Card("2", "heart")
	test_croupier.take_card(test_card1)
	test_croupier.take_card(test_card2)
	#WHEN
	with pytest.raises(DrawException) as exception:
		test_croupier.take_cards_algorithm(player_score=21, points_limit=21, card=test_card3)
		#THEN
		assert exception == "Both players has the same points - 21 as limit. Draw!"
		assert test_croupier.current_score == 21
		assert test_card3 in test_croupier.person_cards


def test_take_cards_algorithm_croupier_win():
	"""Tests, if croupier's win exception is raised, when croupier has greater score than player and not exceeded\
	limit"""

	#GIVEN
	test_croupier = Croupier()
	test_card1 = Card("K", "diamond")
	test_card2 = Card("5", "spade")
	test_card3 = Card("2", "heart")
	test_card4 = Card("2", "heart")
	test_croupier.take_card(test_card1)
	test_croupier.take_card(test_card2)
	#WHEN
	test_croupier.take_cards_algorithm(player_score=18, points_limit=21, card=test_card3)
	with pytest.raises(CroupierWin) as exception:
		test_croupier.take_cards_algorithm(player_score=18, points_limit=21, card=test_card4)
		#THEN
		assert exception == "Croupier wins"
		assert test_croupier.current_score == 19
		assert test_card4 in test_croupier.person_cards


def test_take_cards_algorithm_croupier_exceeded_limit():
	"""Tests if croupier exceed limit exception is raised, when croupier has greater score than limit"""

	#GIVEN
	test_croupier = Croupier()
	test_card1 = Card("K", "diamond")
	test_card2 = Card("5", "spade")
	test_card3 = Card("5", "heart")
	test_card4 = Card("3", "heart")
	test_croupier.take_card(test_card1)
	test_croupier.take_card(test_card2)
	#WHEN
	test_croupier.take_cards_algorithm(player_score=20, points_limit=21, card=test_card3)
	with pytest.raises(ExceededLimit) as exception:
		test_croupier.take_cards_algorithm(player_score=20, points_limit=21, card=test_card4)
		#THEN
		assert exception == "Croupier has more than 21 points. He lost!"
		assert test_croupier.current_score == 23
		assert test_card4 in test_croupier.person_cards





