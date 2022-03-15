from card import Card
from exceptions.answer_exceptions import InvalidAnswer
from exceptions.game_exceptions import ExceededLimit, BlackJack

class  Person():
	"""Represents person who plays in the game"""

	def __init__(self):
		"""Inicialization of new person"""

		self.person_cards = []
		self.current_score = 0

	def take_card(self, card: Card):
		"""Simulates taking one card by person and thereby increases person score"""

		self.person_cards.append(card)
		self.current_score += card.value

	def calculate_points(self) -> int:
		"""Calculates total points after looking at all person's cards

		Returns points (int): amount of player's points"""

		points = 0
		for card in self.person_cards:
			points += card.value
		return points

	def show_person_cards(self):
		"""Shows current person's cards set"""

		print(f"Person's cards: {self.person_cards}")

	def show_current_score(self):
		"""Shows current person's score"""

		print(f"Person's score: {self.current_score}")

	def check_if_black_jack(self):
		"""Checks if person get black jack at the beginning"""

		if self.person_cards[0].name == "A" and self.person_cards[1].name == "A":
			self.current_score = 21
			raise BlackJack("You have black jack")


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
		"""Asks player whether he would like to take another card.py to increase score.

		Returns:
			False (bool): if player do not want to take cards anymore
			True (bool):  if player want to take next ard
		"""

		self.answer = input("Do you take another card.py? (y/n)\n")
		if self.answer == "n":
			return False
		elif self.answer == "y":
			return True
		else:
			raise InvalidAnswer("You have entered wrong value! Try again")




	def take_another_cards(self):
		"""Interprets player's answer, if he want to take cards anymore or not """

		# taking_cards = self.ask_about_another_cards()
		# if taking_cards == False:
		# 	br
		# elif taking_cards == True:
		self.take_card()
		self.show_person_cards()
		self.show_current_score()

	def check_if_lost(self, points_limit):
		"""Checks if user exceed points limit what defines defeat"""

		if self.current_score > points_limit:
			raise ExceededLimit("You have more than 21 points. You lost!")

	def check_if_black_jack(self):
		"""Checks if player get black jack at the beginning"""

		if self.person_cards[0].name == "A" and self.person_cards[1].name == "A":
			self.current_score = 21
			raise BlackJack("Player have black jack")


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

	def check_if_black_jack(self):
		"""Checks if croupier get black jack at the beginning"""

		if self.person_cards[0].name == "A" and self.person_cards[1].name == "A":
			self.current_score = 21
			raise BlackJack("Croupier have black jack")
