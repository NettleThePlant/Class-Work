'''
Author: Abigail
Date: 3/10/15
Description: Printing integers while skipping multiples of five
'''

n = input('Please enter a number: ')

n = int(n)
i = 0

while i < n :
    if i %5 == 0:
        i= i+1
        continue
    else:
        print(i)
        i= i+1
