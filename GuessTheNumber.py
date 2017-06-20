#This is a Guess The Number Game

import random

print('Hello. What is your Name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20')
secret = random.randint(1 , 20)

count = 1

while(count <= 6):
    print('Take a Guess')
    guess = input()
    if(int(guess) < secret):
        print('Your Guess is Low')
    elif(int(guess) > secret):
        print('Your Guess is High')
    else:
        print('Good Job, ' + name + '! You guessed the number in ' + str(count) + ' guesses!')
        break;
    count += 1

if(count == 7):
    print('Nope.The Number I was thinking of was ' + str(secret))
