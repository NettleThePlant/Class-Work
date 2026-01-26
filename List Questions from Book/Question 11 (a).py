'''
26/01/2026
Abigail
Question 11(a)
'''

str_lst = ['apple','pinapple','kiwi','lemon']

length=len(str_lst[0])

for i in str_lst:
    if len(i)>length:
        length=len(i)
print(length)