'''
Author: Abigail
Date: 2/10/15
Description: Taking integers and returning the average
'''

n = -1
total = 0
count = 0
while n!='':
    n= input('Enter a number: ')
    if n.isdigit():
        total+= int(n)
        count +=1
print('average is', total/count)
