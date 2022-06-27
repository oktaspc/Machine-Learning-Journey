#menyatukan dictionary
data1 = {'nama' : 'anto', 'nim' : '0023'}
data2 = {'IPK' : 3.4, 'semester' : 3}
datamarge = {**data1,**data2}
print(datamarge)