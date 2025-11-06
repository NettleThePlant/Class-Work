'''
Author: Abigail Duda
Date: 4/11/25
Description: Asking the user for a string of digits and a step size. Going through the string and adding the first number plus
all the numbers at the step size
'''

string = input('Enter a string of digits: ')
step_size = input('Enter a step size: ')

step_size = int(step_size)

count = 0
string = str(string)

for i in range(0, len(string), step_size):
    count = count + int(string[i])
    
    print('The total  is equal to ',count)