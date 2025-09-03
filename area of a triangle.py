'''
Author: Abiagil
Date: 3rd September
Description: Findint the area of a triangle
'''

base_question = (float(input('Please enter the base measurement of your triangle (in cm): ')))
height_question = (float(input('Please enter the height measurement of your triangle (in cm): ')))

multiply = float(base_question*height_question)
divide = float(multiply/2)

print('The area of your triangle is ', divide)