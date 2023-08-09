class Player
    def __init__(self, name):
        # str representing the player's name
        self.name = name
        # list to hold card objects in the player's hand
        self.hand = []

    def draw_card(self):
        # removes + returns top card from the player's hand, if no cards returns None
        ...

    def take_card(self, cards)
        # adds one(/more) won cards to the bottom of the player's hand
        ...

    def has_cards(self):
        # returns True if the player has any remaining cards, false otherwise
        ...

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []
        self.initialize()

    def initialize(self):
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']