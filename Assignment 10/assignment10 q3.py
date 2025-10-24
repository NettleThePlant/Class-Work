'''
Author: Abigail Duda
Date: 23/10/25
Description: replaying the first letter occurance with a '$', while keeping the first letter
'''

s = input(' Enter a string: ')

firstLetter = s[0]

restOfString= s[1:]
restOfStringM = restOfString.replace(firstLetter, '$')
print(firstLetter + restOfStringM)