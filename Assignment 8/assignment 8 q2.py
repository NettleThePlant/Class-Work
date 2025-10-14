'''
Author: Abigail
Date: 14/10/25
Description: taking n(n>20) as an input. Printing numbers from 11 to n. if n is a multiple of 3, printing 'tipsy', if n is a multiple of
7, printing 'topsy'. if n is a multiple of both, printing 'tipsy topsy'.
'''

n = input('Enter a number that is greater than 20: ')
n = int(n)

for i in range(11, n):
    print(i)

if n %3 ==0:
    print('Tipsy')
if n%7==0:
    print('Topsy')
    
if n < 20:
    print('Not high enough')
