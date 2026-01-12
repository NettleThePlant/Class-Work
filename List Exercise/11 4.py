myl = [2,4,6]
print('Existing list is: ', myl)
n = eval(input('enter a number or a list to be appended: '))
if type(n)==type([]):
    myl.extend(n)
elif type(n)==type(1):
    myl.append(n)
else:
    print('Please enter either an iteger or a list.')
print('Appended list is: ', myl)
