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

		#@TODO
		self.game_result = ""

	def first_distribution(self): #T
		"""Gives two cards for both player and croupier"""

		for _ in range(2):
			card = self.cards_deck.give_card()
			self.player1.take_card(card)
		for _ in range(2):
			card = self.cards_deck.give_card()
			self.croupier1.take_card(card)

		try:
			self.check_if_blackjack_draw()
		except DrawException as exception:
			raise DrawException(exception)
		try:
			self.player1.check_if_black_jack()
		except BlackJack as exception:
			raise BlackJack(exception)
		try:
			self.croupier1.check_if_black_jack()
		except BlackJack as exception:
			raise BlackJack(exception)

	def check_if_blackjack_draw(self): #T
		"""Checks if both persons have blackjack at the beginning"""

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
				raise ExceededLimit(exception)

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

	def show_both_cards_and_points(self):
		"""Grouped representation of player and croupier points and cards"""

		self.player1.show_person_cards()
		self.player1.show_current_score()
		self.croupier1.show_person_cards()
		self.croupier1.show_current_score()

	# @ TODO
	def sum_up_game(self):
		pass

	def run_game(self):
		"""Grouped methods call as game engine to run complete game"""

		self.cards_deck.create_deck()
		self.cards_deck.shuffle_deck()
		self.cards_deck.show_deck()

		try:
			self.first_distribution()
			self.show_both_cards_and_points()
			self.players_run()
			try:
				self.croupiers_run()
				self.show_both_cards_and_points()
			except (CroupierWin, ExceededLimit, DrawException) as exception:
				self.show_both_cards_and_points()
				print(exception)
		except (DrawException, BlackJack, ExceededLimit) as exception:
			self.show_both_cards_and_points()
			print(exception)
