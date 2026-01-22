'''
Abigail
19/1/26
'''

lst = eval(input('Enter a list containing numbers between 1 and 12: '))

length = len(lst)

for i in range(0, length):
    if int(lst[i])>10:
        lst[i]=10
    else:
        lst[i] = int(lst[i])
print(lst)