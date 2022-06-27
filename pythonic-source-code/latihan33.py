#tabel translasi untuk string mapping
# aiueo
# 12345
# string_i ='kota cirebon'
# string_o = ''
# translasi = {
#     'a' : '1',
#     'i' : '2',
#     'u' : '3',
#     'e' : '4',
#     'o' : '5'
# }
# for x in string_i:
#     val = translasi.get(x)
#     string_o += val if val else x
# print(string_o)

# cara diatas tidak pythonic

sumber = 'aiueo'
tujuan =  '41U30'
string_input = 'kota cirebon'
tabel_translasi = str.maketrans(sumber, tujuan)
string_output = string_input.translate(tabel_translasi)
print(f'hasil konversi : {string_output}')
