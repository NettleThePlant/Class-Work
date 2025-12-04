'''
Author: Abigail Duda
Date: 17/11/2025
Description: Adding two Binary numbers
'''

b1 = input('Enter your first binary addition: ')
b2 = input('Enter your second binary addition: ')


lengofb1= len(b1)
lengofb2 = len(b2)

if lengofb1 < lengofb2:
    a = lengofb1
elif lengofb1 > lengofb2:
    a= lengofb2
else:
    a= lengofb1
    
carry = 0    
result = ''

for i in range(-1, -a-1, -1):
    print(b1[i], b2[i])
    
    total1 = int(b1[i]) + int(b2[i])+carry
    print(total1)
    
    if total1>=2:
        result = str(total1 - 2) +result 
        carry=1
    else:
        result= str(total1) +result
        carry=0
        
if carry> 0:
    result = str(carry) +result
print(result)
