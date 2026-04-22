'''
Abigail
ExamCraft mock 2023 b
'''

import random
words = ['cat','mat','can','man','pool','tool','mule','pat','tan','rule']
print('The list of words is: ', words)
random_word = words [random.randint(0,len(words)-1)]

length = len(random_word)
firstLetter = random_word[0]
print('The length of the word is: ', length)
print('The first letter of the word is: ', firstLetter)

turn = 3

for i in range(turn):
    guess = input('Please guess what the word may be: ')
    
    if guess == random_word:
        print('Correct!')
        break
    else:
        print('Wrong, try again')
else:
    print('The word was: ', random_word)
    

