""""This is a module that will use nested
loops in order to generate a deck of cards"""


def create_deck():
    deck = []
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    
    for suit in suits:
        for rank in ranks:
                if rank == "ace":
                    deck.append([suit, rank, [1, 11]])
                elif rank in ("jack", "queen", "king"):
                    deck.append([suit, rank, 10])
                else:
                    deck.append([suit, rank, int(rank)])
    return deck