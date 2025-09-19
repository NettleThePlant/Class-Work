#Author:Abigail Duda
#Date: 18/9/2025
#Description:calculating the area and perimeter of a rectangle with a given length and width

length = float(input('Please enter your length in mm: '))
width = float(input('Please enter your width in mm: '))

area = float(length*width)
perimeter = float(length + width)
perimeter = float(perimeter*2)

print('The area is ', area, 'mm')
print('The perimeter is ', perimeter, 'mm')