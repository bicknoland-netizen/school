"""A module to place a bet and ensure
proper error handling"""

#Todo: Must add ability for player to purchase more money.

def place_bet(money):
    while True:
        print(f"Money: {money}")
        try:
            bet_amount = float(input("Bet Amount: "))
            if bet_amount < 5:
                print("Error: Lowest bet is 5")
                continue
            return bet_amount
        except ValueError:
            print("Error: Bet must be a float value.")