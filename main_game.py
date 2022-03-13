
from deck import cards_deck
from player import person1, croupier1

class Game():
	#
	# def __init__(self):
	# 	self.cards_deck = CardsDeck()

	def first_distribution(self):
		person1.take_card()
		person1.take_card()
		croupier1.take_card()
		croupier1.take_card()

game1 = Game()

if __name__ == "__main__":
	cards_deck.create_deck()
	cards_deck.shuffle_deck()
	cards_deck.show_deck()
	game1.first_distribution()

	cards_deck.show_deck()
	person1.show_person_cards()
	person1.show_current_score()
	croupier1.show_person_cards()
	croupier1.show_current_score()
