'''
Author: Abigail
Date: 9/10/25
Description: checking if an given number is an armstriong number  
'''

total = 0
x = input('Enter your number: ')

num_digit = len(x)

for digit in x:
    total = total + int(digit) ** num_digit
    
if total == int(x):
    print('Armstrong number')

else:
    print('Not armstrong number')

