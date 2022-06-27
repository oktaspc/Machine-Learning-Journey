#fungsi map
def lipat_ganda(x):
   return x*2

listku = [1,2,3,4,5]
listmu =list(map(lipat_ganda, listku))

print(f'listku = {listku}')
print(f'listmu = {listmu}')