'''
Author: Abigail
Date: 08/09/2025
Description: printing the sum of all the odd numbers in a given range 
'''

rangeSumOdd = int(input("Enter the range: "))
total =  0
 
for n in range(rangeSumOdd + 1):
    if n % 2 != 0:
        total+= n
print(total)
    