'''
Author: Abigail
Date: 2/10/25
Description: Taking the users test scores and outputting the average while also returning a letter grade
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
elif average >= 80:
    print('B - 89-80')
elif average >= 70:
    print('C - 79-70')
elif average >= 60:
    print('D - 69-60')
else:
    print('F - 59 or less')


