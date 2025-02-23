#3 Project -Guess the Number Game Python Project (user)
# Instrutor : furqan ali khan

import random
print ("Guess the number between 1 and 100!")
# generte random number
number = random.randint(1, 100)

while True:
    guess = int(input(" Enter your guess number"))
    if guess <number:
        print("to low Number!")
    elif guess > number:
        print("To High Number!")
    else:
       print("conrratulation You Got it Right Number You Win!")
       break
