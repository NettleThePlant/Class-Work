'''
Abigail
product of all even numbers between 1 to 50
'''

product = 1
for i  in range(1, 51):
    if i%2==0:
        product = product*i
print(product)