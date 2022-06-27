#fungsi zip
nim = ['001', '002', '003']
nama = ['aya', 'budi', 'ceve']
hobi = ['makan', 'tidur', 'berak']
for d_nim, d_nama, d_hobi in zip(nim,nama,hobi):
    print(f'{d_nim}---{d_nama}---{d_hobi}')