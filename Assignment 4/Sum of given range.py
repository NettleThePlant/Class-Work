'''
Author: Abigail
Date: 08/09/2025
Description: printing the sum ofnall numbers from a given range
'''


rangeSum = int(input("Enter the range: "))
total =  0
 
for n in range(rangeSum + 1):
    total+= n
print("The sum of all number in the range of ", rangeSum, " is " , total)
