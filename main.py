# Heath Hilton
# 11/06/2022

# Program: 4.1 - Number Guesser
# Project M02 Case Study

# The program is to basically play "Guess My Number" with itself

# Import the random module
import random

rando = random.randint(1, 10)

while True:
    randoGuess = random.randint(1, 10)
    if randoGuess == rando:
        print("The number was {}. You Got IT!" .format(str(rando)))
        break
    elif randoGuess > rando:
        print("Too High.")
    else:
        print("Too Low.")