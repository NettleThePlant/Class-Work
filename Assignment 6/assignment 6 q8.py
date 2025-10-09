'''
Author: Abigail
Date: 9/10/15
Description: Getting the user to guess a value set in the code. Telling the user if their guess is too high or too low, printing 'Well
done' if they guess corectly. repeating the question until they guess correctly
'''

value = 76
valid= False

while not valid:
    n = input('Guess the number:')
    n = int(n)
    
    if n < 76:
        print('Too low')
    elif n > 76:
        print('Too high')
    else:
        print('Well done')
        valid = True