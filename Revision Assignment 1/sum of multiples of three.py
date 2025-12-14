'''
Abigail
sum of multiples of three between one and 50
'''

total = 0
for i  in range(1, 51):
    if i%3==0:
        total = total+i
print(total)