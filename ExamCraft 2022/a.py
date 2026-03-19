'''
Abigail Duda
13/3/26
Examcraft 2022 - OL
'''

print('This progam can find the perimeter or area of a quadrilateral')

length = float(input('Please Enter the length: '))
width = float(input('Please enter the width: '))

userName = input('Please enter your user name: ')
choice = input('Do you want to find the (p)erimeter or (a)rea?')

if choice == 'p':
    print('A quadrilateral with the length of ',length,'and the width of',width,' has a perimeter of:',length*2 + width*2)
elif choice == 'a':
    print('A quadrilateral with the length of ',length,'and the width of',width,' has an area of:',length*width)

print('Thank you for using the program', userName)
