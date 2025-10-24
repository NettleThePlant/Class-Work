'''
Author: Abigail Duda
Date: 23/10/25
Description: Displaying the length of a string using a for loop and a while loop
'''

s = 'Apples are red.'
count = 0

for i in s:
    count = count+1
    print(count)
    
count = 0
while count<len(s):
    count= count+1
    print(count)