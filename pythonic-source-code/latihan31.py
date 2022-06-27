#klausa else pada for
kecepatan = [1,2,3,4,5,6,7,8,9,11,2]
ambang_batas = 33
for laju in kecepatan:
    if laju>ambang_batas:
        laju_normal =False
        print('melebihi ambang batas')
        break
else:
    print('laju kendaraan normal')