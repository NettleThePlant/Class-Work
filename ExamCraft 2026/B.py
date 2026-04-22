'''
Abigail
ExamCraft 2026 B
'''

print('Welcome to my weekly step tracker!')

monday = int(input('Please enter how many steps you took on Monday: '))
tuesday = int(input('Please enter how many steps you took on Tuesday: '))
wednesday = int(input('Please enter how many steps you took on Wednesday: '))
thursday = int(input('Please enter how many steps you took on Thursday: '))
friday = int(input('Please enter how many steps you took on Friday: '))
saturday = int(input('Please enter how many steps you took on Saturday: '))
sunday = int(input('Please enter how many steps you took on Sunday: '))

week_steps = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

print('The list of steps over the week are: ',week_steps)

total = 0
for i in week_steps:
    total += i
print('The total amount of steps you did this week is ',total)

average = total / 7
print('The average steps you took this week is: ', average)

smallest = min(week_steps)
largest = max(week_steps)

print('The largest amount of steps you took was ',largest)
print('The smallest amount of steps you took was ', smallest)