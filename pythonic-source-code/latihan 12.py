#list comperantion and fungsi zip
#nama = ['anto', 'banu', 'caca']
#nim  = [1,2,3]
#listku = []
#for i in range(len(nama)):
#    listku.append([nama[i], nim[i]])
#
#print(f'listku : {listku}')
#cara diatas tidak pythonic
#cara dibawah pythonic
nama = ['anto', 'banu', 'caca']
nim  = [1,2,3]
listku  = [[d_nama, d_nim] for d_nama, d_nim in zip(nama,nim)]
print(f'listku : {listku}')
