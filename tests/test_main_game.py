from main_game import Game
from player import person1, croupier1
from deck import cards_deck
from card import Card

def test_first_distribution():
	"""Test"""

	#GIVEN
	# person1 = Person()
	# croupier1 = Person()
	game1 = Game()
	cards_deck.cards = [Card("9", 9, "diamond"), Card("10", 10, "diamond"), Card("2", 2, "heart"), Card("10", 10, "heart")]
	first_card = cards_deck.cards[-1]
	second_card = cards_deck.cards[-2]

	#WHEN
	game1.first_distribution()

	#THEN
	assert print(person1.person_cards) == print(["10 heart", "2 heart"])
	assert person1.person_cards == [first_card, second_card]
	assert person1.current_score == 12
	assert croupier1.current_score == 19