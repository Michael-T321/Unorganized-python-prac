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


        


    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()




"""class Values(Deck):
    def __init__(self, card_val):
        Deck.__init__(self)
        if value
        self.card_val = {'Cards': [cards]}
        value = 1
        # for card in deck.cards:
            # self.card_val = {f'{card}: {value}'}
            # value += 

    
values = Values(Deck)

"""

# print(values.card_val[1])

# deck.shuffle()

count = 1

"""for card in deck.cards:
    print(f'{count}. {card}')
    count += 1
"""




user_card = (deck.cards[51])
print(f'Your card is {user_card}')
# print(dir(shuffled_deck))

deck_list = [str(card) for card in deck.cards]
card_val = [1,2,3,4,5,6,7,8,9,10,11]
deck_val = dict(zip(card_val, deck_list))
print(deck_val)



