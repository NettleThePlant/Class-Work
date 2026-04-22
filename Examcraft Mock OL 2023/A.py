'''
Abigail
ExamCraft mock 2023 a
'''

option = input('Would you like to (a)dd, (s)ubtract, (m)ultiply or (d)ivide?')

num1 = float(input('Please enter your first number: '))
num2 = float(input('Please enter your second number: '))

if option == 'a':
    answer= num1+num2
    answer = round(answer,2)
    print(num1,'+', num2, '=', answer)
elif option =='s':
    answer= num1-num2
    answer = round(answer,2)
    print(num1,'-', num2, '=',answer)
elif option == 'm':
    answer= num1*num2
    answer = round(answer,2)
    print(num1,'x', num2, '=',answer)
else:
    answer= num1/num2
    answer = round(answer,2)
    print(num1,'÷', num2, '=',answer)
    
