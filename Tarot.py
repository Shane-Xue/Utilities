"""
A (reassuringly boring) Tarot Card Picker,
Which is not smart enough to even show the definitions.
"""
from random import shuffle

def need():


def main():
    """
    Main function in which the user can choose arbitrary numbers of cards.
    It also offers draws in both Major and Minor Arcana decks.
    """
    print("Welcome to the Tarot House powered by SMITS, my friend.")
    print("For more command line programs, visit smits.com.cn.")
    print("What is thy need today?")
    print("1. A draw with the full tarot deck")
    print("2. A draw with solely Major Arcana")
    print("3. A draw with solely Minor Arcana")
    reply = input("Thy need, with a number, dear: ")
    draw(int(reply))

if __name__ == "__main__":
    main()