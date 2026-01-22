'''
Abigail
15/1/2026
'''
lst = [2,4,5,11,13,26]
print('The exsisting list is: ', lst)

n = eval(input('enter a number or a list to be incremented: '))
if type(n)==type([]):
    lst.extend(n)
elif type(n)==type(1):
    lst.append(n)
else:
    print('Please enter either an iteger or a list.')
print('Incremented list is: ', lst)
