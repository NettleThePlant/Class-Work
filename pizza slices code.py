#Author: Abigail
#Date:September 1st
#Description: Calculating left over pizza slices

pizzaSlices = int(input('How many slices of pizza did you start with? '))
pizzaEaten = int(input('How many slices of pizza did you eat? '))
leftOverSlices = (pizzaSlices - pizzaEaten)
print('You have', leftOverSlices, ' pizza slices left over.')