import random

# (1) create a Card class
class Card:

    card_values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11  # You can adjust the value of 'A' based on the game rules
    }

    # initialise
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    # representation override
    def __repr__(self):
        return str(self.number) + " of " + self.suit

    # equality override
    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.suit == other.suit) and (self.number == other.number)
        return False

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            self._suit = suit.upper()
        else:
            print("That's not a suit!")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number.upper()
        else:
            print("That's not a number!")

    @property
    def value(self):
        return self.card_values[self.number] if self.number in self.card_values else None

### checking 
## my_card = Card("Hearts", "A")
## print(my_card)


# (2) create a Deck class
class Deck: 

    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"] # Alternative way of writing

        # card object - list comprehension
        self._cards = [Card(s,n) for s in suits for n in numbers]
    
    # shuffle cards
    def shuffle(self):
        random.shuffle(self._cards)

    # check if a card is in the deck
    def in_deck(self, target_card):
        return target_card in self._cards

    # dealing cards
    def deal(self, num_players, cards_per_player):
        if num_players * cards_per_player > len(self._cards):
            print("Not enough cards in the deck.")
            return None

        hands = [[] for _ in range(num_players)]

        for _ in range(cards_per_player):
            for i in range(num_players):
                card = self._cards.pop()
                hands[i].append(card)

        return hands

### checking
my_deck = Deck()             # deck in order


my_deck.shuffle()            # deck shuffled
print(my_deck._cards)        


### checking if a card is in the deck
target_card = Card("Hearts", "A")
if my_deck.in_deck(target_card):
    print(f"{target_card} is in the deck.")
else:
    print(f"{target_card} is not in the deck.")


### dealing an even number of cards to players
num_players = 4
cards_per_player = 5
hands = my_deck.deal(num_players, cards_per_player)

if hands:
    for i, hand in enumerate(hands):
        print(f"Player {i + 1}'s hand:", hand)


# (3) Hand class to model cards stored in a player's hand
class Hand:

    def __init__(self):
        self._cards = []
    
    def add_card(self, card):
        self._cards.append(card)

    def show_hand(self):
        for card in self._cards:
            print(card)

### checking
hand = Hand()

# assuming card instances
card1 = Card("Hearts", "A")
card2 = Card("Spades", "5")

# add cards to hand
hand.add_card(card1)
hand.add_card(card2)

# show cards in hand
print("Player's Hand:")
hand.show_hand()