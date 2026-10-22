book = open('book.txt','r')
bread = book.read()
bread = bread.lower()
bread = bread.split()

some_dict = {}

for x in bread:
    if x in some_dict:
        some_dict[x] += 1
    else:
        some_dict[x] = 1

def sorting(x):
    return x[1]
sorted_dict = sorted(some_dict.items(),key = sorting, reverse = True)[:10]

print(dict(sorted_dict))
book.close()