class Card():
	"""Class representing card.py of standard playing cards """

	POSSIBLE_FIGURES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, \
	                    "K": 10, "A": 11}
	POSSIBLE_COLOURS = ["heart", "diamond", "club", "spade"]

	def __init__(self, name, colour):
		"""Initializing card object with appropriate parameters validation

		Args:
			name (str): figure name of card.py
			colour (int): kind of card.py's colour
		"""

		if name not in self.POSSIBLE_FIGURES.keys():
			raise IndexError("Entered wrong card name")
		self.name = name
		self.value = self.POSSIBLE_FIGURES[name]

		if colour not in self.POSSIBLE_COLOURS:
			raise ValueError("Entered wrong card colour")
		self.colour = colour


	def __repr__(self):
		"""String representation of card.py object. Includes name and colour

		Returns:
			card_description (str): text description of card.py object
		"""

		card_description = f"{self.name} {self.colour}"
		return card_description
