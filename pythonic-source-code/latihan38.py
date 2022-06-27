#cara tidak pythonic
# def jumlahkan(Psatu,Pdua):
#     return Psatu+Pdua
# listku = [10,20]
# dictku={'Psatu' : 100,'Pdua' : 200}
# hasil_list = jumlahkan(listku[0],listku[1])
# print(f'hasil dari listku :{hasil_list}')
# hasil_dict = jumlahkan(dictku['Psatu'], dictku['Pdua'])
# print(f'hasil dari dictku : {hasil_dict}')

#cara pythonic
def jumlahkan(Psatu,Pdua):
    return Psatu+Pdua

listku = [10,20]
dictku={'Psatu' : 100,'Pdua' : 200}
hasil_list = jumlahkan(*listku)
print(f'hasil dari listku :{hasil_list}')
hasil_dict = jumlahkan(**dictku)
print(f'hasil dari dictku : {hasil_dict}')