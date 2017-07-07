import random

print("Welcome to Hangman Game!")

wordsList = ["cow","donkey","monkey","pig"]
sample = ['_','_','_','_','_','_']
r = random.randint(0,3)

fail = 5
success = 0
print"It is a ",len(wordsList[r])," letter Word."

while fail > 0:
    letter = raw_input("\nGuess a Letter:")
    if letter in wordsList[r]:
        string1 = wordsList[r]
        sample[string1.index(letter)]=letter
        success += 1
        if success == len(wordsList[r]):
            print "\nYou WON!! The Word is:",wordsList[r]
            break
    else:
        fail -= 1
        print "You Have ",fail," guesses remaining!"
    for i in range(0, len(wordsList[r])):
        print sample[i],
if fail == 0:
    print "The Word was " , wordsList[r]
