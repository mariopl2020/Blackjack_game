from exceptions.game_exceptions import  BlackJack

def check_if_black_jack():
	""""""
	a = "A"
	b = "A"
	current_score = 0


	if a == "A" and b == "A":
		current_score == 2
		print("aaa", current_score)
		raise BlackJack("You won! You have black jack")
	return current_score


check_if_black_jack()


#todo
#2 przerobić do tego testy
#3 usunac obiekt cards_deck utworzony na sztucznie