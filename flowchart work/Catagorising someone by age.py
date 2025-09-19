#Author:Abigail Duda
#Date: 19/9/2025
#Description: Catagorising the user using age 

age = int(input('Please enter your age: '))

if age <13:
    print('You are a child')
elif age >= 13 and age >= 20:
    print('You are a teenager')
else:
    print('You are an adult')