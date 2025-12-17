'''
Abigail
17/12/25
program 2 
'''
 
string = input('Enter a number: ')

#step 1
NoLast_digit = string[0:-1]
last_digit = string[-1]

last_digit = int(last_digit)

#step 2 
reverse_string = ''

for char in NoLast_digit:
    reverse_string = char+reverse_string
#print(reverse_string)

#Step 3
even_indices = ''

for i in range(0, len(reverse_string), 2):     #Even indices
    even_indices += reverse_string[i]
#print(even_indices)

odd_indices = ''

for i in range(1, len(reverse_string), 2):     #Odd indices
    odd_indices += reverse_string[i]
#print(odd_indices)

#Adding even indices
evenTotal = 0
for i in even_indices:
    evenTotal = evenTotal + int(i)
#print(evenTotal)

#Adding odd indices
oddTotal = 0
for i in odd_indices:
    oddTotal = oddTotal + int(i)
#print(oddTotal)
    
#Step 4
finalTotal = oddTotal+evenTotal
result = finalTotal + last_digit

#print(result)

#Step 5
if result%10==0:
    print('Card is valid')
else:
    print('Card is not valid')
