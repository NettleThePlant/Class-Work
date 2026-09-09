'''
AbigailDuda
09/09/2026
'''

lst = [5,4,2]
lst2 = []

while lst:
    lstSmall = lst[0]

    for x in lst:
        if x < lstSmall:
            lstSmall = x
    lst2.append(lstSmall)
    lst.remove(lstSmall)

print(lst2)