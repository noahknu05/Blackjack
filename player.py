import random
from card import Card
from hand import Hand
from deck import Deck
from colors import Color

class Player:
    def __init__(self, name, chips = 10000):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.bet_amount = 0
        self.split_hands = []
        

    def place_bet(self, amount):
        self.bet_amount = amount
        self.chips -= amount

    
    def win_bet(self):
        if self.hand.is_blackjack:
            win = self.bet_amount * 1.5
            self.chips += self.bet_amount * 2.5
        
        else:
            win = self.bet_amount
            self.chips += self.bet_amount * 2
        
        
        print(Color.green + f"{self.name} wins {win} chips!\n" + Color.reset)

    def lose_bet(self):
        print(Color.red + f"{self.name} loses {self.bet_amount} chips.\n" + Color.reset)

    def push_bet(self):
        self.chips += self.bet_amount
        print(Color.yellow + f"{self.name} pushes. Bet returned.\n" + Color.reset)

    def split_hand(self):
        if self.chips < self.bet_amount:
            print(Color.red + "Not enough chips to split." + Color.reset)
            return False
        
        #Create new hand
        splitted_hand = Hand()
        card_to_move = self.hand._cards.pop()
        splitted_hand.add_card(card_to_move)
        
        #Adjust aces count
        if card_to_move.is_ace():
            self.hand.aces -= 1
            splitted_hand.aces += 1
        
        #Add a card to each hand will be handled in game logic after this method is called

        #Add new hand to split_hands
        self.split_hands.append(splitted_hand)

        #Deduct chips for new bet
        self.chips -= self.bet_amount

        print(Color.blue + f"{self.name} splits the hand!" + Color.reset)
        return True

    def reset_hand(self):
        self.hand = Hand()
        self.split_hands = []
    

    #Player Actions
    def hit(self, card):
        self.hand.add_card(card)
        

    def dobble_down(self, card):
        self.chips -= self.bet_amount
        self.bet_amount = self.bet_amount * 2
        self.hand.add_card(card)
    
        
        
        
    



            


if __name__ == "__main__":
    player1 = Player("Noah")
    player1.bet()
    player1.win_bet()
    print(player1.chips)