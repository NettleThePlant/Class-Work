'''
Author: Abigail
Date: 2/10/15
Description: 
'''

i = input('Enter a number ')

i = int(i)
total = 0
count = 0
 
while i >= 0:
 total += i
 count += 1
 i = input('Enter a number ')
 i = int(i)
print('The average grade is ', total/count)

average = total/count

if average >= 90:
    print('A - 90')
elif average <= 89:
    print('B - 89-80')
elif average <= 79:
    print('C - 79-70')
elif average <= 69:
    print('D - 69-60')
else:
    print('F - 59 or less')