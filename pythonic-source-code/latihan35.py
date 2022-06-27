#Cara1
# def costum_key(nama):
#     return nama.split()[-1]
#
# siswa = ['karti susanto', 'tejo purnawan', 'bejo rahmadi']
# print(f'sebelum : {siswa}')
# terurut = sorted(siswa,key=costum_key)
# print(f'terurut : {terurut}')

#menggunakan lambda expresion
siswa = ['karti susanto', 'tejo purnawan', 'bejo rahmadi']
print(f'sebelum : {siswa}')
terurut = sorted(siswa,key=lambda x:x.split()[-1])
print(f'terurut : {terurut}')
