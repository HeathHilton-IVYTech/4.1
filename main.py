# Heath Hilton
# 11/06/2022

# Program: 4.1 - Number Guesser
# Project M02 Case Study

# The program is to basically play "Guess My Number" with itself

# Import the random module
import random

secret = random.randint(1, 10)

while True:
    guess = random.randint(1, 10)
    if guess == secret:
        print("The number was {}. You Got IT!" .format(str(secret)))
        break
    elif guess > secret:
        print("Too High.")
    else:
        print("Too Low.")
