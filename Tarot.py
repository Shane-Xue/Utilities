"""
A (reassuringly boring) Tarot Card Picker,
Which is not smart enough to even show the definitions.
"""
from random import shuffle, sample

# Global Variables for Maintainance

# User Error Dealing
_MAX_ERRORS = 3
_ERRORS = 0

# Quit (normal exit) Signal
_SIGQUIT = 3 # Note that this should be user number - 1

# Terminating Signal
_SIGTERM = "TERMINATE"

def fullDraw():
    lst=list(range(78))
    print(sample(lst, 3))

def majArcana():
    pass

def minArcana():
    pass

def draw(num):
    print(num)
    menu = [fullDraw,
            majArcana,
            minArcana]
    menu[num]()

def quit():
    print("Thanks for using the Tarot House! See you soon!~")

def abort():
    print("You toyed with me so much! I'm not playing with you anymore! [cry]")

def need():
    global _MAX_ERRORS,_ERRORS,_SIGTERM
    menu=[
        "1. A draw with the full tarot deck",
        "2. A draw with solely Major Arcana",
        "3. A draw with solely Minor Arcana",
        "4. Quit"
        ]
    for entry in menu:
        print(entry)
    reply = input("Thy need, with a number, dear: ")
    try:
        if int(reply) in range(1,len(menu) + 1):
            _ERRORS = 0 # reset _ERRORS to default
            return int(reply) - 1 # To comply with list indices
    except ValueError:
        _ERRORS += 1
        print("Woops! That isn't a number dear~\n")
        return need() if _ERRORS < _MAX_ERRORS else _SIGTERM
    else:
        _ERRORS += 1
        print("Sorry, dear, that's invalid~ Input again!\n")
        return need() if _ERRORS < _MAX_ERRORS else _SIGTERM

def main():
    """
    Main function in which the user can choose arbitrary numbers of cards.
    It also offers draws in both Major and Minor Arcana decks.
    """
    print("Welcome to the Tarot House powered by SMITS, my friend.")
    print("For more command line programs, visit smits.com.cn.\n\n")
    print("What is thy need today?")
    numNeed = need()
    if numNeed == _SIGTERM:
        return abort()
    if numNeed == _SIGQUIT:
        return quit()
    draw(numNeed)
    main()

if __name__ == "__main__":
    main()
