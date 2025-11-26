from card import Card
from deck import Deck

class Hand:
    def __init__(self):
        self._cards = []
        self.aces = 0
        self.busted = False
        self.is_soft = False
        self.is_bust = False
        self.is_blackjack = False
        self.is_twenty_one = False

    
    
    def __str__(self):
        return " ".join(str(card) for card in self._cards)
        #else:
            #return " ".join(str(card) for card in self._cards) + f"\n(Value: {self.value - 10}/{self.value})"
    
    def reset_cards(self):
        self._cards = []
        self.aces = 0
        self.busted = False
        self.is_soft = False
        self.is_bust = False
        self.is_blackjack = False
        self.is_twenty_one = False


    def add_card(self, card):
        self._cards.append(card)

        #Checks for aces
        if card.is_ace():
            self.aces += 1
            
        if self.value > 21:
            self.is_busted = True

    def first_card(self):
        return self._cards[0]
    

    @property
    def value(self):
        total_val = 0
        aces = 0
        for card in self._cards:
            val = card.value   # Card.value is a property
            total_val += val
            if card.is_ace():
                aces += 1

        # Adjust for aces (count some as 1 instead of 11 if needed)
        while total_val > 21 and aces > 0:
            total_val -= 10
            aces -= 1
        
      
        #Update booleans
        self.is_soft = aces > 0
        self.is_bust = total_val > 21
        self.is_blackjack = len(self._cards) == 2 and total_val == 21
        self.is_twenty_one = total_val == 21 and len(self._cards) > 2

        return total_val
    


    

if __name__ == "__main__":
    c1 = Card("A", "S")
    c2 = Card("5", "S")
    deck = Deck()
    hand1 = Hand()
    hand1.add_card(c1)
    print("Cards:", hand1._cards)
    print("Handvalue", hand1.value)
    hand1.add_card(c2)
    print("Cards:", hand1._cards)
    print("Handvalue", hand1.value)
    hand1.add_card(deck.draw)
    print("Cards:", hand1._cards)
    print("Handvalue", hand1.value)
    hand1.add_card(deck.draw)
    print("Cards:", hand1._cards)
    print("Handvalue", hand1.value)
    hand1.add_card(deck.draw)
    print("Cards:", hand1._cards)
    print("Handvalue", hand1.value)
    print(hand1.busted)

