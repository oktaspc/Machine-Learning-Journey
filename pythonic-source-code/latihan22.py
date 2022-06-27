#mengenal operator in, untuk memeriksa list
# listku = [10,20,30,40,50,60]
# cari = 50
# ketemu = False
# for i in listku:
#     if i == cari:
#         ketemu += True
#         break
# if ketemu:
#     print('ditemukan')
# else:
#     print('tidak ditemukan')

listku = [10,20,30,40,50,60]
cari = 54
if cari in listku:
    print('ditemukan')
else:
    print('tidak ditemukan')