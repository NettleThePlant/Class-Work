'''
Author: Abigail
Date: 3rd September
Description: returning a given number after putting it in the forms of squared, cubed, and the power of four
'''

Number_question = int(input('Please enter a number: '))

squared = (int(Number_question*Number_question))
cubed = (int(Number_question*Number_question*Number_question))
power_of_four = (int(Number_question*Number_question*Number_question*Number_question))

print('Your number is ', squared, 'when squared ', cubed, 'when cubed, and ', power_of_four, 'when put to the power of four.')