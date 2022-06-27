#string formatting
nama = 'anto'
nim = 111
print('nama saya '+ nama + ' nim saya adalah '+ str(nim))
print('nama saya adalah %s nim saya adalah %d' %(nama,nim)) #c++ style
print('nama saya adalah {0} nim saya adalah {1}'.format(nama,nim))
siswa = {
    'nama' : 'anto',
    'nim' : 111,
}
print('nama saya adalah {nama} nim saya adalah {nim}'.format(**siswa))
