from deck import cards_deck

class  Person():
	"""Represents person who plays in the game"""

	def __init__(self):
		"""Inicialization of new person"""

		self.person_cards = []
		self.current_score = 0
		# self.cards_deck = CardsDeck()


	def take_card(self):
		"""Simulates taking one card by person and thereby increases person score"""

		currently_taken_card = cards_deck.cards.pop(-1)
		self.person_cards.append(currently_taken_card)
		self.current_score += currently_taken_card.value


	def show_person_cards(self):
		"""Shows current person's cards set"""

		print(f"Person's cards: {self.person_cards}")


	def show_current_score(self):
		"""Shows current person's score"""

		print(f"Person's score: {self.current_score}")


class Player(Person):
	"""Represents real player. This class inherites from Person"""

	def __init__(self):
		"""Initialization of new player"""

		super().__init__()


	def show_person_cards(self):
		"""Shows current player's cards set"""

		print(f"Player's cards: {self.person_cards}")


class Croupier(Person):
	"""Represents croupier who is the host of game. This class inherites from Person"""

	def __init__(self):
		"""Initialization of new croupier"""

		super().__init__()

	def show_person_cards(self):
		"""Shows current croupier's cards set"""

		print(f"Croupier's cards: {self.person_cards}")


person1 = Player()
croupier1 = Croupier()