#fungsi zip dan unzip
# nim = [100,200,300,400]
# nama = ['aaa','bbb','ccc','ddd']
# ipk = [1,2,3,4]
# siswa = []
# for i in range(len(nim)):
#     siswa.append((nim[i], nama[i], ipk[i]))
# print(f'nama :{siswa[0]}')

nim = [100,200,300,400]
nama = ['aaa','bbb','ccc','ddd']
ipk = [1,2,3,4]
siswa = list (zip(nama,nim,ipk))
print(siswa)