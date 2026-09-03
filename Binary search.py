'''
Abigail Duda
03/09/2026
Binary Search
'''

numbers = [2,5,8,12,16,56,23,72,38,91]

numbers.sort()

target = 23

low = 0
high = len(numbers)-1

while low <= high:
    middle = (low+high)//2
    
    if numbers[middle] == target:
        print('Element found at index:',middle)
        break
    elif numbers[middle]< target:
        low = middle+1
    else:
        high = middle-1
else:
    print('Element not found')