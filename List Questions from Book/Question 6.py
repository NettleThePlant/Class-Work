'''
Abigail
20/1/26
'''

lst = [12,24,5,76,9,13,15,69,3,4,2,6]
print('The existing list is ',lst)

length = len(lst)
num = int(input('Enter the number you want checked: '))

for i in range(0,length):
    if num==lst[i]:
        print(num, ' is in the list at index ',i)
        break
else:
    print('The number you are serching for is not in the list.')