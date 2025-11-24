"""This module will handle all the different deck handling functions."""
import random

def player_draw_card(deck, hand, points):
    select_card = random.randint(0, len(deck) - 1)
    selected_card = deck[select_card]
    if selected_card[1]== "ace":
        selected_card[2] = ace_handler(points)
    hand.append(selected_card)
    deck.pop(select_card)



def dealer_draw_card(deck, hand, points):
    select_card = random.randint(0, len(deck) - 1)
    selected_card = deck[select_card]
    if selected_card[1]== "ace":
        if points < 11:
            selected_card[2] = 11
        else:
            selected_card[2] = 1
    hand.append(selected_card)
    deck.pop(select_card)


def player_turn(deck, hand):
        player_points = check_value(hand)
        player_draw_card(deck, hand, player_points)
        
        player_points = check_value(hand)
        player_draw_card(deck, hand, player_points)
        
        show_hand(hand)
        while True:
            hit_or_stand = input("\nHit or stand? (hit/stand): ")
            if hit_or_stand.lower() == "hit":
                player_points = check_value(hand)
                player_draw_card(deck, hand, player_points)
                player_points = check_value(hand)
                if player_points > 21:
                    print("\n\nPlayer went bust with the following hand\n===================")
                    show_hand(hand)
                    print(f"Players Points: {check_value(hand)}")
                    break
                else:
                    show_hand(hand)
                    continue
                    
            elif hit_or_stand.lower() == "stand":
                break
                
    



def check_value(hand):
    total_value = 0
    for card in hand:
        total_value += int(card[2])
    return total_value
                
            


def show_hand(hand):
    for card in hand:
        print(f"{card[1]} of {card[0]}")
        
        
        
def ace_handler(points):
    print("You have drawn an Ace")
    if points < 11:
        while True:
            choice = int(input("Do you want this ace to be 1 or 11?: "))
            try:
                if choice == 1:
                    return 1
                elif choice == 11:
                    return 11
                else:
                    print("You must choose 1 or 11.")
                    continue
            except ValueError:
                print("Invalid entry, requires integer.")
    else:
        return 1