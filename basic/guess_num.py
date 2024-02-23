# choose random number
# function to set difficulty
# get uer guess
# check uer guess (function)
# trace turns and decrement 1 if wring
# repat while wrong

from random import randint
from guess_num_sol_art import logo

CHANCES_EASY = 10
CHANCES_HARD = 5

print(logo)

level = input("Enter 1 for Easy, 2 for Hard: ")


def check_guess(guess, number):
    """Check guess"""
    if number < guess:
        return "too high"
    return "too low"

def game():
    """Game trying discover random integer"""
    chances = CHANCES_EASY if level == "1" else CHANCES_HARD
    number = randint(1, 100)
    print(f"NUMBER test é {number}")
    while chances > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print ("certô miseravi!")
            return
        print(check_guess(guess, number))
        chances -= 1
        print(f"you still have {chances} chances!")
        if chances == 0:
            print("You lose")

game()
