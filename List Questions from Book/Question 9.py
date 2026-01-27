'''
Abigail
23/1/26
'''

lst = eval(input('Enter a list: '))

lst.insert(0, lst[-1])
lst.pop(-1)
print(lst)