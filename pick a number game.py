import random

number = random.randint(1, 10)
guess = 0
tries = 0


while guess != number:
    guess = int(
        input(
            "I have a number between 1 and 10. Pick a number and try to guess it, youngblood"
        )
    )
    tries = tries + 1

    if guess != number:
        print("You kinda suck at this game. For the " + str(tries) + " time already")
    else:
        print("there you go! You guessed it in " + str(tries) + " tries")
