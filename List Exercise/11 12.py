lst= eval(input('Enter a list: '))
ln= len(lst)
mx= max(lst)
ind = lst.index(mx)
if ind<=(ln/2):
    print('The maximum element ', mx, ' lies in the 1st half.')
else:
    print('The maximum element ', mx, ' lies in the 2nd half.')