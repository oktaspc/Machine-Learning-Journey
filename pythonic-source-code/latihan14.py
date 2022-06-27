#reverse a list
#cara ini tidak pythonic
# listku = [1,2,3,4,5,6]
# listmu = []
#
# for i in range(len(listku)):
#    reverse_i = len(listku) -  i -1
#    listmu.append(listku[reverse_i])
# print(f'listku : {listku}')
# print(f'listmu : {listmu}')

#cara berikut pythonic
listku = [1,2,3,4,5,6,7]
listmu = listku[::-1]

print(f'listku : {listku}')
print(f'listmu : {listmu}')