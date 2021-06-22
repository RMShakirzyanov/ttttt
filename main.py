elepfant = int(input("введите массу слона в килограммах: "))
crocodile = int(input("введите массу крокодила в килограммах: "))
giraffe = int(input("введите массу жирафа в килограммах: "))
GAZ = 1500
ZIL = 5000

ecg_GAZ = elepfant + crocodile + giraffe <= GAZ
ec_GAZ = (elepfant + crocodile <= GAZ) and (giraffe <= ZIL)
eg_GAZ = (elepfant + giraffe <= GAZ) and (crocodile <= ZIL)
cg_GAZ = (crocodile + giraffe <= GAZ) and (elepfant <= ZIL)
ecg_ZIL = elepfant + crocodile + giraffe <= ZIL
ec_ZIL = (elepfant + crocodile <= GAZ) and (giraffe <= GAZ)
eg_ZIL = (elepfant + giraffe <= GAZ) and (crocodile <= GAZ)
cg_ZIL = (crocodile + giraffe <= GAZ) and (elepfant <= GAZ)

print(ecg_GAZ or ec_GAZ or eg_GAZ or cg_GAZ or ecg_ZIL or ec_ZIL or eg_ZIL or cg_ZIL) 
