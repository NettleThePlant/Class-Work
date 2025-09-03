'''
Author: Abigail
Date: 3rd September
Description: Converting centimeters to inches and feet
'''

height_question = float(input('Please enter your height in centimeters: '))

inches = (float(height_question/2.54))
feet = (float(inches/12))

print('You are ', feet, 'feet and ', inches, 'inches!')