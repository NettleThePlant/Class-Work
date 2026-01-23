'''
Abigail
23/1/26
Question 7 (c)
'''

lst = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'

length = len(alphabet)

for i in range(length):
    lst.append(alphabet[i]*(i+1))
    print(lst)