from deck import cards_deck
from person import Player, Croupier

class Game():
	"""Represents single game"""

	def __init__(self):
		"""Inicialization of new game"""

		self.player1 = Player()
		self.croupier1 = Croupier()
	# 	self.cards_deck = CardsDeck()

	def first_distribution(self):
		"""Gives two cards for both player and croupier"""

		self.player1.take_card()
		self.player1.take_card()
		self.croupier1.take_card()
		self.croupier1.take_card()


game1 = Game()

if __name__ == "__main__":
	cards_deck.create_deck()
	cards_deck.shuffle_deck()
	cards_deck.show_deck()
	game1.first_distribution()

	game1.player1.show_person_cards()
	game1.player1.show_current_score()
	game1.croupier1.show_person_cards()
	game1.croupier1.show_current_score()
	game1.player1.take_another_cards()
