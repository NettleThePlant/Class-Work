#Author: Abigail
#Date:1st September
#Description: Calculating how much each diner owes for their share of the bill

bill_price = float(input('How much was the total price of the bill? '))
diners = int(input('How many diners attented? '))

splitBill = (bill_price/diners)

print('Each person must pay', splitBill)
