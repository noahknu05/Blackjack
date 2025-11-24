import random
from card import Card

class Deck:
    def __init__(self, num_decks = 1):
        self.num_decks = int(num_decks)
        self.cards = []
        self._build()
        self._shuffle()
    

    def _build(self):
        ranks = [str(i) for i in range(2, 11)] + ["A", "K", "Q", "J"]
        suits = ["♠", "♥", "♦", "♣"]
        for _ in range(self.num_decks):
            for suit in suits:
                for rank in ranks:
                    card = (Card(rank, suit))
                    self.cards.append(card)

    def _shuffle(self):
        random.shuffle(self.cards)

    def reshuffle_treshold(self):
        if (self.num_decks * 52) * 0.3 > self.cards_left:
            self.cards = []
            self._build()
            self._shuffle()
            print("Dealer is reashuffeling... under deck.py -reshuffle:_treshold")
        

    @property
    def draw(self):
        self.reshuffle_treshold()
        return self.cards.pop()
    
    @property
    def cards_left(self):
        return len(self.cards)


    

if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)
    print(deck.draw)
    print(deck.cards)
    print(deck.cards_left)

    print(deck.cards)
    print(deck.draw)
    print(deck.cards)
    print(deck.cards_left)
    for _ in range(40):
        deck.draw
        print(deck.cards)
        print(deck.cards_left)
