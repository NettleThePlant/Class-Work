'''
Author: Abigail Duda
Date: 17/10/25
Description: asking the user for their first and last name, joining
them together with a space. Displaying their full name and the length of their full name
'''

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')

full_name = (first_name + ' ' +last_name)

print(full_name)

print('The length of your full name is ', len(full_name), 'letters and a space.')
#telling the user the space is included in the length of their name