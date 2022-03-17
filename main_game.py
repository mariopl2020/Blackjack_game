from cards_deck import CardsDeck
from person import Player, Croupier
from exceptions.answer_exceptions import InvalidAnswer
from exceptions.game_exceptions import ExceededLimit, BlackJack, DrawException, CroupierWin


class Game():
	"""Represents single game"""

	def __init__(self):
		"""Initialization of new game"""

		self.player1 = Player()
		self.croupier1 = Croupier()
		self.points_limit = 21
		self.cards_deck = CardsDeck()

		self.game_result = ""

	def first_distribution(self):
		"""Gives two cards for both player and croupier"""

		self.player1.take_card(card=self.cards_deck.give_card())
		self.player1.take_card(card=self.cards_deck.give_card())
		self.croupier1.take_card(card=self.cards_deck.give_card())
		self.croupier1.take_card(card=self.cards_deck.give_card())

		try:
			self.player1.check_if_black_jack()
		except BlackJack as ex:
			raise BlackJack(ex)
		try:
			self.croupier1.check_if_black_jack()
		except BlackJack as ex:
			print(ex)
			self.check_if_blackjack_draw()

	def check_if_blackjack_draw(self):
		"""Checks if both person have blackjack at the beginning"""

		if self.croupier1.current_score == self.points_limit and self.player1.current_score == self.points_limit:
			raise DrawException("You have the same score. BlackJack draw!")

	def players_run(self):
		"""Consists of whole steps of player's run in logic loop. Defined exception checks, if player exceed points\
		limit or enter wrong value"""

		while True:
			try:
				still_play = self.player1.ask_about_another_cards()
				if still_play:
					self.player1.take_another_cards(self.cards_deck.give_card())
					self.player1.check_if_exceed_limit(points_limit=self.points_limit)
				elif still_play == False:
					break
			except InvalidAnswer as exception:
				print(exception)
			except ExceededLimit as exception:
				print(exception)
				break

	def croupiers_run(self):
		"""Consists of calling method of taking cards by algorith in logic loop. Defined exception checks, if croupier\
		win or lost"""

		while True:
			try:
				self.croupier1.take_cards_algorithm(player_score=self.player1.current_score,\
				points_limit=self.points_limit, card=self.cards_deck.give_card())
			except (CroupierWin) as ex:
				raise CroupierWin(ex)
			except (ExceededLimit) as ex:
				raise ExceededLimit(ex)
			except DrawException as ex:
				raise DrawException(ex)

	# @ TODO
	def show_stats(self):
		# kumuluje wyswietlanie statow i kart
		pass

	# @ TODO
	def sum_up_game(self):
		pass


game1 = Game()

if __name__ == "__main__":
	game1.cards_deck.create_deck()
	game1.cards_deck.shuffle_deck()
	game1.cards_deck.show_deck()

	try:
		game1.first_distribution()
		game1.player1.show_person_cards()
		game1.player1.show_current_score()
		game1.croupier1.show_person_cards()
		game1.croupier1.show_current_score()
		game1.players_run()
		try:
			game1.croupiers_run()
		except (CroupierWin, ExceededLimit, DrawException) as ex:
			print(ex)
	except (DrawException, BlackJack) as ex:
		print(ex)
	else:
		game1.player1.show_person_cards()
		game1.player1.show_current_score()
		game1.croupier1.show_person_cards()
		game1.croupier1.show_current_score()
