class Card:
    def __init__(self, rank, suit):
        # store attributes as "private" to discourage direct modification
        self._rank = rank
        self._suit = suit

    # read-only properties (immutable)
    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def is_ace(self):
        return self.rank == "A"
    @property
    def value(self):
        """Return Blackjack value: J/Q/K=10, A=11, else int(rank)."""
        if self.rank in ("J", "Q", "K"):
            return 10
        elif self.rank == "A":
            return 11
        return int(self.rank)
    
        

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self): #Added this 
        return str(self)   


    
if __name__ == "__main__":
    c1 = Card("A", "S")
    c2 = Card("K", "D")
    cards = [c1, c2]
    print(c1, c1.value) 
    for card in cards:
        print(card)
