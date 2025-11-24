from player import Player
from game import Game
from dealer import Dealer
from colors import Color
from ui import *

def run_player_turn(game):
    game.check_outcome()
    print("outcome", game.outcome)
    
    print(game.player_actions)

    while not game.player_finished and game.outcome == None:

        print(f"\n{'-' *30}\n")
        game.show_table()
        print(" ")

        #Take player input
        action = input_player_action(game.player_actions)
        game.player_turn(action)

        if game.check_outcome() != None:
            break
   

def run_dealer_turn(game):
    print(f"\n{'-' *30}\n")
    game.dealer_turn()
    game.check_outcome()
    game.show_table()




def normal_game(game):
    print("Current chips: ", game.player.chips)
    game.start_round(amount = input_player_bet(game.player.chips))
    run_player_turn(game)
    run_dealer_turn(game)
    game.settle_bets()
    

def run_main():
    player = Player("Vincent")
    dealer = Dealer()
    game = Game(player, dealer)
    while True:
        normal_game(game)
        game.prep_new_round()

run_main()

    