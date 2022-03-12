class Card():
	"""Class representing card of standard playing cards """

	possible_figeres = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, \
	                    "K": 10, "A": 11}
	possible_colours = ["heart", "diamond", "club", "spade"]

	def __init__(self, name, value, colour):
		"""Initializing card object

		Args:
			name (str): figure name of card
			value (int): value of  card's power
			colour (int): kind of card's colour
		"""

		self.name = name
		self.value = value
		self.colour = colour


	def __repr__(self):
		"""String representation of card object. Includes name and colour

		Returns:
			card_description (str): text description of card object
		"""

		card_description = f"{self.name} {self.colour}"
		return card_description
