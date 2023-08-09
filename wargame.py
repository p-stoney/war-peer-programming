class Player
    def __init__(self, name):
        # str representing the player's name
        self.name = name
        # list to hold card objects in the player's hand
        self.hand = []

    def draw_card(self):
        # removes or returns top card from the player's hand
        ...

    def take_card(self, cards)
        # adds one(/more) won cards to the bottom of the player's hand
        ...

    def has_cards(self):
        # returns true if the player has any remaining cards, false otherwise
        ...