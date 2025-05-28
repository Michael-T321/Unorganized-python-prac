# Date: 4/11/25

import math
import random

class Card:

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit =  suit
        
    def get_rank(self):
        return self._rank
    
    def get_suit(self):
        return self._suit

    def __str__(self):
        return"{} of {}".format(self._rank, self._suit)

    
class Deck: # intention: create a deck of cards
    def __init__(self): # dones't need any other objects because we don't need a specif
        self.cards = []
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

        self.card_values = {}
        for card in self.cards:
            rank = card.get_rank()
            
            if rank in ['J', 'Q', 'K']:
                value = 10
            elif rank == 'A':
                value = 11  
            else:
                value = int(rank)
            
            self.card_values[str(card)] = value
                


    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()

deck.shuffle()

# for card_str, value in deck.card_values.items():
 #   print(f"{card_str}: {value}") 

for card in deck.cards:
    print(f"{card}: {deck.card_values[str(card)]}")

count = 1

"""for card in deck.cards:
    print(f'{count}. {card}')
    count += 1
"""




user_card = (deck.cards[51])
print(f'Your card is {user_card}')
# print(dir(shuffled_deck))

# card_dict = {}

# deck_list = [str(card) for card in deck.cards]
"""for i in range(len(deck_list)):
    if deck_list[i].startswith("2"):
        card_dict[card] = 2
"""


# print(deck_list)


# card_vals = {}
# card_vals['']
# deck_val = dict(zip(card_val, deck_list))
# print(deck_val)