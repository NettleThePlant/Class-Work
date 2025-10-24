'''
Author: Abigail Duda
Date: 24/10/25
Description: removing all odd index values in a given string
'''

s = input('Enter a string: ')
count =  0

while count< len(s):
    if count %2==0:
        print(s[count])
        
    count = count+1