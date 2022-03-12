from card import Card

class CardsDeck():
	"""Representation of deck of playing cards"""

	def __init__(self):
		"""Initializing of full deck of cards as list"""

		self.cards = []


	def create_deck(self):
		"""Creating deck of cards as list of card objects

		Returns:
			self.cards (list): list fulfilled by card objectss
		"""

		for name, value in Card.possible_figeres.items():
			for colour in Card.possible_colours:
				self.cards.append(Card(name, value, colour))
		return self.cards


	def show_deck(self):
		"""Printing all created cards"""

		for card in self.cards:
			print(card)


cards_deck = CardsDeck()
cards_deck.create_deck()
cards_deck.show_deck()