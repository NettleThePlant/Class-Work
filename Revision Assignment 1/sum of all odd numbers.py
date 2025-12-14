'''
Abigail
sum of all odd numbers between 1 and n, where n is inputed by the user
'''

n = input('Enter a range: ')
n = int(n)
n = n+1

total = 0
for i  in range(1, n):
    if i%2!=0:
        total = total+i
print(total)