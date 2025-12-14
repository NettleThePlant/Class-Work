'''
Abigail
product of all multiples of 5 between 1 and 50
'''

product = 1

for i in range(1,51):
    if i%5==0:
        product = product * i
print(product)