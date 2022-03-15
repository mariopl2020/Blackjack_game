from random import shuffle
from card import Card

class CardsDeck():
	"""Representation of deck of playing cards"""

	def __init__(self):
		"""Initializing deck of cards as list"""

		self.cards = []

	def create_deck(self) -> list:
		"""Creating deck of cards as list of card.py objects

		Returns:
			self.cards (list): list fulfilled by card.py objects
		"""

		for name in Card.POSSIBLE_FIGURES.keys():
			for colour in Card.POSSIBLE_COLOURS:
				self.cards.append(Card(name=name, colour=colour))
		return self.cards

	def show_deck(self):
		"""Printing all created cards"""

		for card in self.cards:
			print(card.name, card.colour)
		print("------")


	def shuffle_deck(self):
		"""Shuffling of cards deck"""

		shuffle(self.cards)

	def give_card(self) -> Card:
		"""Giving one card from the top of deck

		Returns: card_for_person (Card): card what is given to the person
			"""

		card_for_person = self.cards.pop()
		return card_for_person
		
# cards_deck = CardsDeck()
