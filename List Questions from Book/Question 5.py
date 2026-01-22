'''
Abigail
20/1/26
'''

lst = eval(input('Input a list of strings:'))

lst2 = []
for i in lst:
    lst2.append(i[1:])
    print(lst2)