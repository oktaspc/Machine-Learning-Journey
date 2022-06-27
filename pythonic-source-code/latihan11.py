#cara tidak pythonic
#listku = [1,3,5,7,9,15]
#listmu = []
#for item in listku:
#    if item >= 10:
#        listmu.append(item)
#print(f'listmu = {listmu}')
#print(f'listku = {listku}')

#CARA PYTHONIC
listku = [1,3,5,7,9,15]
listmu = [item for item in listku if item >= 10] #untuk tiap item di dalam listku jika >10 maka masukkan listku keladalm listmu
print(f'listku = {listku}')
print(f'listmu = {listmu}')
