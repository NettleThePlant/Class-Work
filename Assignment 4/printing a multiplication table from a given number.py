'''
Author: Abigail
Date: 08/09/2025
Description: printing a multiplication table from a given number
'''

mNumber = int(input('Please enter a number: '))

for n in range(13):
    result = mNumber*n
    print(mNumber, 'x', n, '=',result) 
