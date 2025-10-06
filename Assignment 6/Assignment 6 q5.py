'''
Author: Abigail
Date: 6/10/15
Description: printing from 1 to n squared and stopping the loop if the count is 50
'''

n = input('Enter a number: ')
n = int(n)

i = 0
n = n*n

while i < n:
    i = i + 1
    print(i)
    if i > 49:
        break
    