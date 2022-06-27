#splitting
#cara ini tidak pythonic
# text = 'belajar python asik'
# listku = []
# kata = ''
# for huruf in text:
#     if huruf != ' ':
#         kata += huruf
#     else:
#         listku.append(kata)
#         kata = ''
# listku.append(kata)
# print(text)
# print(f'listku : {listku}')

#cara berikut pythonic
text = 'belajar python asik'
listku = text.split() #splitting text berdasarkan spasi
print(text)
print(f'listku : {listku}')