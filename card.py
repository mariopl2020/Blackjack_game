"""module concerning playing card used in blackjack game """

from exceptions.card_exception import InvalidColour, InvalidName


class Card():
    """Class representing card of standard playing cards"""

    POSSIBLE_FIGURES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,\
                        "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    POSSIBLE_COLOURS = ["heart", "diamond"]#, "club", "spade"]

    def __init__(self, name, colour):
        """Initializing card object with appropriate parameters validation

        Args:
            name (str): figure name of card
            colour (str): kind of card's colour
        """

        if name not in self.POSSIBLE_FIGURES:
            raise InvalidName("Entered wrong card name")

        self.name = name
        self.value = self.POSSIBLE_FIGURES[name]

        if colour not in self.POSSIBLE_COLOURS:
            raise InvalidColour("Entered wrong card colour")

        self.colour = colour

    def __repr__(self) -> str:
        """String representation of  object from Class card. Includes its name and colour

        Returns:
            card_description (str): text description of card.py object
        """

        card_description = f"{self.name} {self.colour}"
        return card_description
