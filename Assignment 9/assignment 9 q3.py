'''
Author: Abigail Duda
Date: 17/10/25
Description: asking the user to enter a word and making the following modifications:
> If the word starts with a vowel, adding 'way' at the end
>If the word starts with a consonant, moving the firstletter to the end and adding 'ay'
'''

word = input('Please enter your word: ')

n = ''
if word[0] in 'aeiou':
    print(word + 'way')
else:
    for i in range(1, len(word)):
        n = n+word[i]
    n = n+word[0]+'ay'
    print(n)