'''
Author: Abigail
Date: 10/10/25
Description: Converting a binary to a decimal number
'''

n = input('Enter your Binary number: ')

p = len(n)-1
total = 0

for digit in n:
    total = total + int(digit)*2**p
    p=p-1
    
    print(total)