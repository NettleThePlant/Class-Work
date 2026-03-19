'''
Abigail Duda
13/3/26
Examcraft 2022 - OL
'''
#(b)

import random

computer_options= ['rock','paper','scissors']

computer_choice = computer_options[random.randint(0,2)]

print('Welcome to rock, paper, scisors!')
player_choice = input('Enter rock, paper or scissors: ')

print('You chose:', player_choice)
print('Computer chose:', computer_choice)

if player_choice == 'rock':
    if computer_choice == 'scissors':
        print('You win!')
    elif computer_choice == 'paper':
        print('Computer wins!')
    elif computer_choice == player_choice:
        print('Draw!')
        
if player_choice =='paper':
    if computer_choice == 'scissors':
        print('Computer wins!')
    elif computer_choice == 'rock':
        print('You win!')
    elif computer_choice == player_choice:
        print('Draw!')
        
if player_choice =='scissors':
    if computer_choice == 'rock':
        print('Computer wins!')
    elif computer_choice == 'paper':
        print('You win!')
    elif computer_choice == player_choice:
        print('Draw!')