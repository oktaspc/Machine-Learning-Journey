#mengabaikan nilai dengan underscore
#mengabil fungsi
#underscore (_) dikenal dengan istilah dont care
# for _ i in range(3):
#     print("belajar pemrogramman")

listku = [1,2,3,4,5,6]
a, b, *_ = listku #memasukkan nilai lisku ke a dan b dan sisanya diabaikan
print(f'listku {listku}')
print(f'a:{a} b:{b}')