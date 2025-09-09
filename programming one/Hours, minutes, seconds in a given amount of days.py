#Author: Abigail
#Date:1st September
#Description: Calculating the amount of hours, minutes and seconds in a certain amount of days



numberOfDays = int(input('Please pick a random amount of days: '))
daysConvertedToHours = (numberOfDays*24)
daysConvertedToMinutes = (daysConvertedToHours*60)
daysConvertedToSeconds = (daysConvertedToMinutes*60)
print('There are', daysConvertedToHours,' hours ', daysConvertedToMinutes,'minutes and', daysConvertedToSeconds, ' seconds in ', numberOfDays, 'days')


