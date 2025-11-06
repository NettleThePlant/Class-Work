'''
Author: Abigail Duda
Date: 3/11/25
Description: giving the user 7 tries to guess a set number. telling them if the number is higher or lower. Printing 'Game over' when
7 tries have failed
'''

n = 31
guess = input('Guess the number, you have 7 tries: ')

count = 0
while guess != n:
    guess = input('Guess the number: ')
    guess = int(guess)
    count = count+1
    
    if guess < 31:
        print('Too low')
    elif guess > 31:
        print('Too high')
    else:
        print('Well done!')


    if count == 6:
        break