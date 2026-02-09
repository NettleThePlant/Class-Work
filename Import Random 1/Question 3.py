'''
Abigail
9/2/2026
'''

import random

coin = ['heads','tails']
result = random.choice(coin)
#print(result)

user_guess = input('Heads or tails: ')

if user_guess == result:
    print('You win! :]')
else:
    print('You lose! :[')

print('Coin = ', result)
print('You = ',user_guess)