#fungsi unzip
#memecah sekumpulan nilai pada list
siswa = [('001','bejo',111),
         ('002','bayu',222),
         ('003','gaga',333)]
nim, nama, ipk = zip(*siswa)
print(f'nim :{nim} \nnama :{nama} \nipk :{ipk}')