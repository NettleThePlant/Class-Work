'''
Abigail
sum of the first n integers, where n is inputted by the user
'''

n = input('Please enter a range: ')
n = int(n)
n = n+1
total = 0

for i in range(1, n):
    total = total + i
print(total)