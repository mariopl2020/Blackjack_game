from deck import cards_deck
from exceptions.answer_exceptions import InvalidAnswer

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

	def show_current_score(self):
		"""Shows current player's score"""

		print(f"Player's score: {self.current_score}")


	def ask_about_another_cards(self):
		"""Asks player whether he would like to take another card to increase score.

		Returns:
			False (bool): if player do not want to take cards anymore
			True (bool):  if player want to take next ard
		"""

		try:
			self.answer = input("Do you take another card? (y/n)\n")
			if self.answer == "n":
				return False
			elif self.answer == "y":
				return True
			else:
				raise InvalidAnswer("You have entered wrong value! Try again")
		except InvalidAnswer as exception:
			print(exception)


	def take_another_cards(self):
		"""Interpretes player's answer, if he want to take cards anymore or not """

		while True:
			taking_cards = self.ask_about_another_cards()
			if taking_cards == False:
				break
			elif taking_cards == True:
				self.take_card()
				self.show_person_cards()
				self.show_current_score()


class Croupier(Person):
	"""Represents croupier who is the host of game. This class inherites from Person"""

	def __init__(self):
		"""Initialization of new croupier"""

		super().__init__()

	def show_person_cards(self):
		"""Shows current croupier's cards set"""

		print(f"Croupier's cards: {self.person_cards}")


	def show_current_score(self):
		"""Shows current croupier's score"""

		print(f"Croupier's score: {self.current_score}")



# person1 = Player()
# croupier1 = Croupier()