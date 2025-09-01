#Author:Abigail Duda
#Date: September 1st 2025
#Description: Program to request user name as input and return same with a greeting

user_name = input( 'Please enter your name: ')
user_surname = input('Please enter your surname: ')


greeting = 'Hello'


print(greeting, user_name, user_surname)

int1 = int(input('Please enter your first number: '))
int2 = int(input('Please enter your second number: '))

print(int1+int2)
sumOfAddition = (int1+int2)

print('The sum of ',int1, 'and ', int2, 'is ', sumOfAddition)

int3 = int(input('Please enter your third number: '))

sumOfMultiplication = (int3 * sumOfAddition)

print('The answer is: ', sumOfMultiplication)

pizzaSlices = int(input('How many slices of pizza did you start with? '))
pizzaEaten = int(input('How many slices of pizza did you eat? '))
leftOverSlices = (pizzaSlices - pizzaEaten)
print('You have', leftOverSlices, ' pizza slices left over.')

user_nameQ6 = input(' Please enter your full name: ')
user_age = int(input('Please enter your age: '))
                    
future_user_age = (user_age + 1)

print('Hello', user_nameQ6, 'Next year, you will be', future_user_age, ' years old!')

bill_price = float(input('How much was the total price of the bill? '))
diners = int(input('How many diners attented? '))

splitBill = (bill_price/diners)

print('Each person must pay', splitBill)

numberOfDays = int(input('Please pick a random amount of days: '))
daysConvertedToHours = (numberOfDays*24)
daysConvertedToMinutes = (daysConvertedToHours*60)
daysConvertedToSeconds = (daysConvertedToMinutes*60)
print('There are', daysConvertedToHours,' hours ', daysConvertedToMinutes,'minutes and', daysConvertedToSeconds, ' seconds in ', numberOfDays, 'days')


numberOfKilograms = float(input('Please enter your amount of kilograms: '))

convertedPounds = float((numberOfKilograms*2.204))

print('There are', convertedPounds, ' pounds in ',numberOfKilograms, 'kilograms')












