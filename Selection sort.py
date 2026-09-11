lst = [3,5,2,7,1]
size = len(lst)


for i in range(0, size):
    m = i
    for j in range(i+1,size):
        if lst[j]<lst[m]:
            m = j
            print(m)
    if m!= i:
        temp = lst[i]
        lst[i] = lst[m]
        lst[m] = temp

        
    print(lst)
    