'''
Author: Abigail Duda
Date: 24/10/25
Description: Displaying the sum of digits from an inputed string
'''


s = input('Enter a random string of characters: ')
count = 0
s = str(s)

for i in s:
    count = count+1
    print('The sum of the digits in the string is: ', count)
