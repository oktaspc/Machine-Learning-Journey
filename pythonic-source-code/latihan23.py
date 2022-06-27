#fungsi dengan  mengembalikan sekumpulan nilai/ lebih dari 1 nilai
# def fungsiku():
#     nama = 'okta'
#     nim = 'D021191019'
#     ipk = 3.50
#     siswa  = (nama, nim, ipk)
#     return siswa
#
# hasil = fungsiku()
# print(f'hasil 1 : {hasil[0]}')
# print(f'hasil 2 : {hasil[1]}')
# print(f'hasil 3 : {hasil[2]}')

def fungsiku():
    nama = 'okta'
    nim = 'D021191019'
    ipk = 3.50
    return nama,nim,ipk #auto packing

a,b,c = fungsiku() #auto unpacking
print(f'a : {[a]}')
print(f'b : {[b]}')
print(f'c : {[c]}')