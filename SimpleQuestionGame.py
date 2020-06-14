# This program is a simply question game that prompts the user to start playing
# by typing "roll" and then printing a question that corresponds to the number generated
# The answer is compared to the answer and the result will either announce a win or loss and
# then the program will restart

#What I learned:

# - How to print to the screen
# - Boolean operator (and, or, not)
# - Comparing two values with comparison operators
# - While loops
# - For loops
# - The use of If, elif, and else statements
# - Break and Continue
# - Range in a for loop
# - Import keyword

import random
# Creates an infinite loop to restart the game when the player wins
while True:
    # Sets roll as empty string
    roll = ''
    # Creates an infinite loop to ask player to type roll
    while True:
        print('~~~~~PLEASE TYPE "roll" TO START~~~~~~~~')
        roll = input()
        if roll != 'roll':
            continue
        if roll == 'roll':
            break
    # When player starts the game, a random number is generated and printed out
    num = random.randint(1,6)
    print('You rolled a ' + str(num))

    # A question is chosen based on the number, using some comparison operators and boolean operators

    # Question 1
    if num >= 1 and num <= 3:
        print('What color is the sky? (tip: use lowercase)')
        answer = input()
        realAnswer = 'blue'
        if answer == realAnswer:
            for i in range (3):
                print('You guessed correct! You won!!!')
        else:
            print('Incorrect, restarting program')
            
    # Question 2
    elif num == 4 or num == 5:
        print('Is Python a programming language or a snake? (tip: use lowercase)')
        answer = input()
        realAnswer = 'both'
        if answer == realAnswer:
            for i in range (3):
                print('You guessed correct! You won!!!')
        else:
            print('Incorrect, restarting program')

    # Question 3
    elif num == 6:
        print('Just type "i win" (tip: use lowercase)')
        answer = input()
        realAnswer = 'i win'
        if answer == realAnswer:
           for i in range (3):
                print('You guessed correct! You won!!!')
        else:
            print('Incorrect, restarting program')
            
    # The roll can only be between 1-6, so this will never be chosen
    else:
        print('you won because you rolled an impossible number!')

    print('#############THE PROGRAM WILL NOW RESTART###############')
