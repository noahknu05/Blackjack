import random
from card import Card
from hand import Hand
from deck import Deck
from player import Player

class Dealer:
    def __init__(self):
        dealer_names = ["Gloria Vega", "Frankie DeLuca", "Jack O'Hara", "Lucky Liu", "Deckard Stone"]
        ran_num = random.randint(0, len(dealer_names) - 1)
        
        self.name = dealer_names[ran_num]
        self.hand = Hand()
        self.deck = Deck()
    
    def deal_player(self, player):
        card = self.deck.draw
        player.hand.add_card(card)
        #(print(f"\n{self.name} deal {card} to {player.name}.\n"))
    
    def draw_card(self):
        card = self.deck.draw
        return card
    
    def deal_self(self):
        card = self.deck.draw
        self.hand.add_card(card)

    @property
    def first_card(self):
        first_card = self.hand._cards[0]
        return first_card

    #def first_deal(self, player):
        #self.deal_player(player)
       # self.deal_self()
       # #self.deal_player(player)
       # self.deal_self()
        
        

if __name__ == "__main__":
    player1 = Player("Noah")
    dealer = Dealer()
    dealer.deal_player(player1)
    dealer.deal_self()
    dealer.deal_player(player1)
    dealer.deal_self()

    print("Dealers hand")
    fcard = dealer.show_first_card()
    print(fcard)
    print(fcard.value)

    print(dealer.hand.value)
    

    print(f"{player1.name}'s hand:")
    print(player1.hand._cards)
    print(player1.hand.value)
    
