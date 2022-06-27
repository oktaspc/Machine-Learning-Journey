#string concantenanio penggabungan string
# listku =['ayam', 'naga', 'dino']
# kalimat = ''
# for kata in listku:
#     kalimat += kata + ' '
#
# print(f'listku : {listku}')
# print(kalimat)

#cara diatas tidak pythonic
listku = ['ayam', 'naga', 'dino']
kalimat = ' '.join(listku)
print(f'listku : {listku}')
print(kalimat)