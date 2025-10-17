'''
Author: Abigail Duda
Date: 17/10/25
Description:
'''

string = input('Please enter your string: ')
counter = input('Enter the character you wish to count: ')

count = 0

string = str(string)

for i in string:
    if i == counter:
        count += 1
print(count)