from random import shuffle
from card import Card

class CardsDeck():
	"""Representation of deck of playing cards"""

	def __init__(self):
		"""Initializing of full deck of cards as list"""

		self.cards = []


	def create_deck(self):
		"""Creating deck of cards as list of card.py objects

		Returns:
			self.cards (list): list fulfilled by card.py objects
		"""

		for name in Card.POSSIBLE_FIGURES.keys():
			for colour in Card.POSSIBLE_COLOURS:
				self.cards.append(Card(name, colour))
		return self.cards


	def show_deck(self):
		"""Printing all created cards"""

		for card in self.cards:
			print(card.name, card.colour)
		print("------")


	def shuffle_deck(self):
		"""Shuffling of cards deck"""

		shuffle(self.cards)

cards_deck = CardsDeck()
