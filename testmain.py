from card import Card
from deck import Deck
from hand import Hand




    
def test():
    hand1 = Hand()
    hand1.add_card(deck.draw)
    print("Deck len: ",deck.len_)
    hand1.add_card(deck.draw)
    print("Hand cards: ", hand1._cards)
    hand1.add_card(deck.draw)
    print("Hand cards: ", hand1._cards)
    print("Hand value:", hand1.value)
    print("Hand is bust: ", hand1.is_bust())
    
deck = Deck()
hand1 = Hand()
hand1.add_card(deck.draw)
hand1.add_card(deck.draw)
print("Hand cards: ", hand1._cards)
print("Hand value:", hand1.value)

while True:
    ans = input("1. Hit\n0. stop")
    if hand1.is_bust:
        print("you busted")
        break

    if ans == "1":
        hand1.add_card(deck.draw)
        print("Hand cards: ", hand1._cards)
        print("Hand value:", hand1.value)

    if ans == "0":
        break