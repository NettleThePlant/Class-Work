'''
Author: Abigail
Date: 10/10/15
Description: Entering numbers until the user enters 0 and printing the count of negative and positive numbers
'''

n = input('Enter a number: ')
n = int(n)

count = 0

while n != 0:
    n = input('Enter a number: ')
    n = int(n)
    
    count+=1
    
    if n == 0:
        print('The total amount of numbers entered before zero was', count)