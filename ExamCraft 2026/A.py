'''
Abigail
Examcraft 2026 a 
'''

print('Welcome to the Step Tracker App!')

user_name = input('Please enter your name: ')
steps_today = int(input('Enter the number of steps you walked today: ')) #This is where the user enters the number of steps

if steps_today < 0:
    print('Number of steps cannot be nagative.')
elif steps_today >= 10000:
    print('Well done ', user_name, '! You reached your goal!')
elif steps_today <9999>5000:
    print('Good effort ',user_name, '!. Almost there!')
elif steps_today < 5000>0:
    print('Try to be more active today ', user_name, '!')
