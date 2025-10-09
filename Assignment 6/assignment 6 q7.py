'''
Author: Abigail
Date: 9/10/15
Description: asking the user for a number between 10 and twenty, if the number is less than 10, print too low, if
the number is more than 20 printing too high. repeating the question until desired number is inputed and printing thank you
'''


valid = False

while not valid:
    n = input('Please Enter a number between 10 and 20: ')
    n = int(n)
    if n < 10:
        print('Too low')
    elif n > 20:
        print('Too high')
    else:
        print('Thank you')
        valid = True
        