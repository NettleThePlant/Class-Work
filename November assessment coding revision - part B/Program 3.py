'''
Abigail Duda
17/12/25
Program 3
'''

string = input('Enter our number: ')

#Step 1
NoLast_digit = string[0:-1]
last_digit = string[-1]

last_digit = int(last_digit)

#Step 2
reverse_string = ''

for char in NoLast_digit:
    reverse_string = char+reverse_string
    
#Step 3

evenTotal = 0
oddTotal = 0

for i in range(len(reverse_string)):
    digit = int(reverse_string[i])
    if i %2==0:
        evenTotal = evenTotal +digit
    else:
        oddTotal = oddTotal + digit
#print(evenTotal,  oddTotal)
    
#Step 4
finalTotal = oddTotal + evenTotal
result= finalTotal + last_digit

#print(result)

#Step 5
if result%10==0:
    print('Card is valid')
else:
    print('Card is not valid')

    
