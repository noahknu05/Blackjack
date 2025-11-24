from dealer import Dealer 
from player import Player
from card import Card
import time

from ui import *

class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

        self.table_message = None
        self.player_actions = {"h": "| Hit", "s": "Stand", "dd": "Double Down", "sp": "Split", "sur": "Surrender"}
       
        self.outcome = None
        self.player_finished = False
        self.round_finished = False
        self.round_push = False

    def start_deal(self):
        for _ in range(2):
            self.dealer.deal_player(self.player)
            self.dealer.deal_self()

    def start_round(self, amount):
        self.player.place_bet(amount)
        self.start_deal()
        self.remove_invalid_actions()

    def prep_new_round(self):
        self.table_message = None
        self.player_actions = {"h": "| Hit", "s": "Stand", "dd": "Double Down", "sp": "Split", "sur": "Surrender"}
        self.outcome = None
        self.player_finished = False
        self.round_finished = False
        self.round_push = False
        self.player.hand.reset_cards()
        self.dealer.hand.reset_cards()



        


    
    #Circumstances
    
    def check_outcome(self):
        dealer_bj = self.dealer.hand.is_blackjack
        dealer_value = self.dealer.hand.value

        player_bj = self.player.hand.is_blackjack
        player_value = self.player.hand.value
        
        

        #Checks for blackjack
        if dealer_bj or player_bj:

            if player_bj and dealer_bj:
                self.table_message = "Both player and Dealer have Blackjack."
                self.outcome = "push"

            elif player_bj:
                self.table_message = "BlackJack - You win!"
                self.outcome = "win"

            else:
                self.table_message = "Dealer got blackjack you loose."
                self.outcome = "loss"
            
            self.round_finished = True

        if self.dealer.hand.is_bust:
            self.table_message = "Dealer busted."
            self.outcome = "win"
            self.round_finished = True
        
        if self.player.hand.is_bust:
            self.table_message = "You busted."
            self.outcome = "loss"
            self.player_finished = True
            self.round_finished = True

        if self.player.hand.is_twenty_one:
            self.round_finished = True

            
            
        
        elif self.round_finished and self.outcome == None:
            if dealer_value > player_value:
                self.outcome = "loss"
            
            elif dealer_value == player_value:
                self.outcome = "push"
            
            else:
                self.outcome = "win"
    
        


    
    def show_table(self):
        print("Dealer")
        print(f"{self.dealer.name}'s hand")

        #------------Print DEALERS CARDS----------------
        #One card hidden
        if self.player_finished == False and self.round_finished == False:
                print(self.dealer.first_card, "?")
                print(f"Value: {self.dealer.first_card.value}")
        
        
        #Show all cards
        else:
            print(self.dealer.hand)
            print(f"Value: {self.dealer.hand.value}")
        #=============================================

            
        #------------Player SHOW CARDS----------------


        #If it is soft hand
        if self.player.hand.is_soft == True and self.player.hand.value < 21:
            str_value = f"{self.player.hand.value - 10} / {self.player.hand.value}"

        #If it is blackjack
        elif self.player.hand.is_blackjack == True:
            str_value = "21 - Blackjack!"

        #Normal hand
        else:
            str_value = f"{self.player.hand.value}"


       #=============================================

        print(f"\n{self.player.name}'s hand")
        print(self.player.hand)
        print(f"Value: {str_value}")
        if self.table_message:
            print(f"\n{self.table_message}\n")


    def remove_invalid_actions(self):
        if len(self.player.hand._cards) > 2 or self.player.chips < self.player.bet_amount:
            if "dd" in self.player_actions:
                self.player_actions.pop("dd")
            if "sp" in self.player_actions:
                self.player_actions.pop("sp")
        
        elif self.player.hand._cards[0].rank != self.player.hand._cards[1].rank:
            if "sp" in self.player_actions:
                self.player_actions.pop("sp")

    

    def player_turn(self, action):
        self.remove_invalid_actions()
        if action == "h":
            self.player.hit(self.dealer.draw_card())

            if self.player.hand.is_twenty_one:
                self.player_finished = True
            
        
        elif action == "s":
            self.player.is_stand = True
            self.player_finished = True


        elif action == "sp":
            pass

        elif action == "dd":
            self.player.dobble_down(self.dealer.draw_card())
            self.player_finished = True
        
        elif action == "sur":
            self.outcome = "loss"
            self.player_finished = True

        else:
            print("ERROR")


        #Rules
    
    
    
    def dealer_turn(self):
        if not self.player.hand.is_bust:
            while self.dealer.hand.value < 17:
                self.dealer.deal_self()
        
        self.round_finished = True
                

    def settle_bets(self):
        if self.outcome == "win":
          self.player.win_bet()
        
        if self.outcome == "push":
            self.player.push_bet()
        
        if self.outcome == "loss":
            self.player.lose_bet()
        



def give_dealer_cards(game):
    ans = input("Dealer card: ").upper()
    for letter in ans:
        card = Card(letter, "H")
        game.dealer.hand.add_card(card)

    
    
def give_player_cards(game):
    ans = input("Dealer card: ").upper()
    for letter in ans:
        card = Card(letter, "H")
        game.player.hand.add_card(card)

def test_restart():
    dealer = Dealer()
    player = Player("Noah")
    game = Game(player, dealer)
    return game

    

if __name__ == "__main__":
    dealer = Dealer()
    player = Player("Noah")
    game = Game(player, dealer)

    AH = Card("A", "H")
    KH = Card("K", "H")
    AS = Card("A", "S")
    QH = Card("Q", "H")
    JS = Card("J", "S")

    menu = """1. add dealer card
2. add player card
3. Check table
4. Player turn 
5. Restart
Command: """


    while True:
        print("----------START-------------")
        
        ans = int(input(menu))
        print("---------")
        if ans == 1:
            give_dealer_cards(game)
            print("\n--------TABLE-----------")
            game.show_table()
            
        
        if ans == 2:
            give_player_cards(game)
            game.show_table()
            
        if ans == 3:
            #game.player_turn("s")
            game.check_outcome()
            print("\n--------TABLE-----------")
            game.show_table()

        if ans == 4:
            print(f"\n{'-' *30}\n")
            game.show_table()
            print(" ")
            print(game.outcome)
            game.outcome()
            if game.outcome == None:
                game.player_turn(input_player_action(game.player_actions))
            
            else:
                print(game.outcome)
        
        if ans == 5:
                dealer = Dealer()
                player = Player("Noah")
                game = Game(player, dealer)

        print("-----------------------")




