#memanggil fungsi berantai
# #cara tidak pythonic
# def tambah(a,b):
#      return a+b
# def kali (a,b):
#     return a*b
# a,b = 20,10
# kondisi = False
# if kondisi:
#     print(tambah(a,b))
# else:
#     print(kali(a,b))

# cara pythonic:
def tambah(a,b):
     return a+b
def kali (a,b):
    return a*b
a,b = 20,10
kondisi = True
hasil = (tambah if kondisi else kali)(a,b) #tambah akan dipanggil apabila benar, dan jika tidak kali akan dipanggil
print(hasil)
