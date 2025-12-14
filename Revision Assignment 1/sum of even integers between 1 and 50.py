'''
Abigail
sum of even integers between 1 and 50
'''

total = 0
for i  in range(1, 51):
    if i%2==0:
        total = total+i
print(total)