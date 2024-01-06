import random

from termcolor import colored, cprint #for coloured printing

# function to check if character is in the word and in the right spot
def checkIfGreen(guess, word, index):
    return guess[index] == word[index]

# function to check if character is in the word and in the wrong spot
def checkIfYellow(guess, word, index):
    return guess[index] != word[index] and guess[index] in word

print("Welcome to Wordle!")
print("A 5-letter word has been randomly generated.")

# open file with list of all 5 letter words
file =  open('5_letter_words.txt')
words = file.read().splitlines()
# choose random word
word = random.choice(words)
file.close()

print("You have 6 guesses.")

wordFound = False

# loop 6 times
for i in range(6):

    #prompt user to enter guess until valid word is entered
    guess = input("Guess #" + str(i+1) + ": ")
    guess = guess.upper()
    
    while guess not in words:
        print("Invalid word. Please try again.")
        guess = input("Guess #" + str(i+1) + ": ")
        guess = guess.upper()
    
    #create copy of word and guess
    wordcpy = str(word)
    guesscpy = str(guess)
    
    colours = 'bbbbb' # string that represents colours of characters for each guess
    
    # loops through string to find all the green characters
    for index in range(0, len(guesscpy)):
        if checkIfGreen(guesscpy, wordcpy, index):
            colours = colours[:index] + 'g' + colours[index+1:] # updates colours string
            # replaces character in word by an asterisk, to mark as found, and to avoid characters from mistakenly being marked as yellow in the future
            wordcpy = wordcpy[:index] + '*' + wordcpy[index + 1:] 
    # loops through string to find all the yellow characters and updates colours string
    for index in range(0, len(guesscpy)):
        if checkIfYellow(guesscpy, wordcpy, index):
            if colours[index] != 'g': # checks if character is not already green
                colours = colours[:index] + 'y' + colours[index+1:] # updates colours string
                # replaces character in word by an asterisk, to mark as found, and to avoid characters from mistakenly being marked as yellow in the future
                wordcpy = wordcpy.replace(guesscpy[index], '*', 1) 
    
    # prints out guess with the proper colours using the colours string
    for index in range(0, len(guess)):
        if colours[index] == 'g':
            print(colored(guesscpy[index], 'green'), end = '')
        elif colours[index] == 'y':
            print(colored(guesscpy[index], 'yellow'), end = '')
        else:
            print(guesscpy[index], end = '')
            
    print('\n')
    if guess == word:
        wordFound = True
        break
    
if wordFound:
    print("Congrats! You guessed it right!")
else:
    print("You're out of guesses. The word was " + word + ".")