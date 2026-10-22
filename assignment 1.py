print('		Welcome to sentance sorter!')
user_sent = input('~Please enter sentance: ')
choice = input('~Enter 1, if you want to sort by word, enter 2 if you want to sort by letter: ')

user_sent = user_sent.lower()
some_dict = {}

if choice == '1':
    user_sent = user_sent.split()
else:
    for x in user_sent:
        if x == ' ':
            continue
        
for x in user_sent:
    if x in some_dict:
        some_dict[x] += 1
    else:
        #some_dict.update({x:1})
        some_dict[x] = 1
        
print('Word:count')
print(some_dict)