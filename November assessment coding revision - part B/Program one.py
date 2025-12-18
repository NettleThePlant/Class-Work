'''
Abigail
15/12/25
Program 1
'''

string = input('Enter a number: ')

#Step 1
last_digit = string[-1]       
no_lastDigit = string[0:-1]

#Step 2
reverseNo_lastDigit = no_lastDigit[::-1]   

#Step 3
odd_indecies = reverseNo_lastDigit[1::2]   
even_indecies = reverseNo_lastDigit[0::2]

#print('Odd',odd_indecies)

oddTotal = 0

for i in odd_indecies:
    oddTotal = oddTotal +int(i)
#print(oddTotal)

#print('even',even_indecies)
evenTotal = 0

for i in even_indecies:
    evenTotal = evenTotal + int(i)
#print(evenTotal)

#Step 4
last_digit = int(last_digit)

finalTotal = evenTotal + oddTotal
result = finalTotal + last_digit

#print(result)

#Step 5

if result%10==0:
    print('Card is valid')
else:
    print('Card is not valid')