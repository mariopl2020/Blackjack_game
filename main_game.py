from deck import cards_deck
from person import Player, Croupier
from exceptions.answer_exceptions import InvalidAnswer
from exceptions.game_exceptions import ExceededLimit, BlackJack, DrawException

class Game():
	"""Represents single game"""

	def __init__(self):
		"""Inicialization of new game"""

		self.player1 = Player()
		self.croupier1 = Croupier()
		self.points_limit = 21
	# 	self.cards_deck = CardsDeck()

	def first_distribution(self):
		"""Gives two cards for both player and croupier"""

		self.player1.take_card()
		self.player1.take_card()
		self.croupier1.take_card()
		self.croupier1.take_card()

		# self.player1.check_if_black_jack()
		# self.croupier1.check_if_black_jack()
		# self.check_if_blackjack_draw()

		try:
			self.player1.check_if_black_jack()
		except BlackJack as ex:
			print(ex)
		try:
			self.croupier1.check_if_black_jack()
		except BlackJack as ex:
			print(ex)
			self.check_if_blackjack_draw()

	def check_if_blackjack_draw(self):
		""""""

		if self.croupier1.current_score == self.points_limit and self.player1.current_score == self.points_limit:
			raise DrawException("You have the same score. BlackJack draw!")

	def player_run(self):
		"""Consists of whole steps of player's run in logic loop. Defined exception checks, if player do not lose"""

		while True:
			try:
				still_play = self.player1.ask_about_another_cards()
				if still_play:
					self.player1.take_another_cards()
					self.player1.check_if_lost(points_limit= self.points_limit)
				elif still_play == False:
					break
			except InvalidAnswer as exception:
				print(exception)
			except ExceededLimit as exception:
				print(exception)
				break

game1 = Game()

if __name__ == "__main__":
	cards_deck.create_deck()
	# cards_deck.shuffle_deck()
	cards_deck.show_deck()
	try:
		game1.first_distribution()
	except (DrawException) as ex:
		print(ex)
	else:
		game1.player1.show_person_cards()
		game1.player1.show_current_score()
		game1.croupier1.show_person_cards()
		game1.croupier1.show_current_score()
		game1.player_run()
