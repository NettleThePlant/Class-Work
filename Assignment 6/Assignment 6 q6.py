'''
Author: Abigail
Date: 6/10/15
Description: Taking in numbers from the user, continueing taking numbers until the total amount of numbers entered is greater than 50
'''

i = input('Enter a number: ')
i = int(i)

total = 0
count = 0

while i >= 0:
 total += i
 count += 1
 i = input('Enter a number ')
 i = int(i)

 n = total+count
 if n > 50:
    break