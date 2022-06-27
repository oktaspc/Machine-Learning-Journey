#menghitung jumlah ke kemunculan nilai
#cara ini tudak pythonic
# listku = [1,2,3,4,5,6,3,4,5,2,3]
# cari = 3
# total = 0
# for i in listku:
#     if i == cari:
#         total+=1
#
# print(total)
# print(listku)

listku = [1,2,3,4,5,6,3,4,5,2,3]
cari = 3
jumlah = listku.count(cari) #gunakan count
print(jumlah)