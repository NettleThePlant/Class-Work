#Author:Abigail Duda
#Date: 19/9/2025
#Description: Checking if a year is a leap year

year = int(input('Please Enter your year: '))

if year%4 == 0:
    print(year, 'is a leap year')
else:
    print(year,'is not a leap year')
 