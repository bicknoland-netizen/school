"""Store the functions for writing and reading 
the money amount to a file any time the data 
is changed."""

import sys

def read_money():
    try:
        with open("money.txt", 'r') as file:
                contents = file.read()
                return float(contents)
    except FileNotFoundError:
        print("Error: money.txt has not been found")
        print("Tarminating program.")
        sys.exit()


def write_money(amount):
        with open("money.txt", 'w') as file:
                file.write(f"{amount}")