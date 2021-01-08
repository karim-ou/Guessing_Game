import random

name = input("Hello what's your name: ")
# the player will chose the high number in the range
try:
    y = int(input(f"ok {name}, chose a number : "))
except ValueError:
    print("you did not enter a number,please try again")
    quit()

SecretNumber = random.randint(1, y)
# intro
print(f"Well, {name} i am thinking of a number between 1 and {y}")
# keep track of times the player will guess
for guessesTaken in range(1, 7):
    print("Take a guess")
    try:
        guess = int(input())
    except ValueError:
        print("you did not enter a number, try again")
        quit()
    # give a feedback to the player
    if guess < SecretNumber:
        print("your guess is too low")
    elif SecretNumber < guess:
        print("your guess is too high")
    else:
        break
# win !
if guess == SecretNumber:
    print(f"Good job, {name} you guess my number in {str(guessesTaken)} guesses")
# lose :(
else:
    print(f"NOPE, the number i was thinking of was {str(SecretNumber)}")
 
