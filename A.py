'''
Abigail
DEB 2023 OL a
'''

flight_num= input('Please enter your flight number: ')
dest = input('Please enter your destination: ')
ppl_num = int(input('Please enter the number of people travelling: '))
child = int(input('Please enter the amount of children travelling within the group: '))

print('The flight number is ', flight_num)
print('The destination is ', dest)
print('The amount of people travelling is ',ppl_num)

if flight_num == 'EI121' or 'ei121': 
    cost = 520
elif flight_num == 'EI125' or 'ei125':
    cost = 400
child_cost = child*50
cost = ppl_num*cost
cost = cost - child_cost
print('The total cost of your flights is  €',cost)