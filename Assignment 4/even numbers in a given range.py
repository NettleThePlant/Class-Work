'''
Author: Abigail
Date: 08/09/2025
Description:Printing the even numbers in a given range
'''

startRange = int(input("Enter the start of the range: "))
endRange = int(input("Enter the end of the range: "))

print("Even numbers between {startRange} and {endRange}:")

for n in range(startRange, endRange + 1):
    if n % 2 == 0:
        print(n)
