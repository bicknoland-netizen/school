import db
import create_deck
import place_bet
import deck_handler
import sys

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    
    
    while True:
        player_points = 0
        dealer_points = 0
        player_hand = []
        dealer_hand = []
        deck = create_deck.create_deck()
        
        #Display chips at the beginning of the round and take player bet.
        bank = db.read_money()

        #Save the bet in case of win.
        bet = place_bet.place_bet()
        
        
        #Dealers show card
        deck_handler.dealer_draw_card(deck, dealer_hand, dealer_points)
        print("DEALER'S SHOW CARD:")
        deck_handler.show_hand(dealer_hand)
        print()
        
        
        #Enter players turn loop
        deck_handler.player_turn(deck, player_hand)
        
        #Enter dealer turn loop
        deck_handler.dealer_turn(deck, dealer_hand)
        
        #Determine Victor
        victory_check(player_hand,dealer_hand, bet)
        
        
        
        
        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            print("Come back soon!\nBye!")
            break
        
        

if __name__ == "__main__":
    main()