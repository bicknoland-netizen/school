"""A module to place a bet and ensure
proper error handling"""

import db
import sys

def place_bet():

    while True:
        remainder = db.read_money()
        if float(remainder) < 5:
            add_funds(remainder)
            continue
        try:
            
            print(f"Money: {remainder}")
            bet_amount = float(input("Bet Amount: "))
            if bet_amount < 5:
                print("Error: Lowest bet is 5")
                continue
            elif bet_amount > 1000:
                print("Error: Maximum bet is 1000")
                continue
            elif bet_amount > remainder:
                print("Error: You don't have that many chips")
                continue

            remainder -= bet_amount
            db.write_money(remainder)
            return bet_amount
        
        except ValueError:
            print("Error: Bet must be a float value.")
            

"""A functio to allow player to purchase more chips or quit playing."""
        
def add_funds(remainder):
    print(f"Your current bank is {remainder}, which is less than the minimal bet of 5")
    get_more_chips = input("Would you like to purchase more chips? (y/n)?: ")
    if get_more_chips.lower() == "y":
        remainder += 100
        db.write_money(remainder)
    else:
        print("Not enough chips to continue. Terminating program.")
        sys.exit()