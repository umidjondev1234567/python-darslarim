# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:58:40 2022

@author: Ne'matov Umidjon
Dictionary
"""

# car = {'model' : 'Damas', 'rang': 'oq'}
# print(car['model'])
# print(car['rang'])
# mmm = car.get(input("Tanglang: "), "Bundayi yo'q")
# nnn = car.get(input("Tanglang: "))
# print(mmm)
# print(nnn)

# en_uz = {'apple':'olma', 'beach':'sohil', 'fix':'tuzatmoq'}
# nom = input("Qaysi so'zni qidiryapsiz?\n>>>")
# print(en_uz[nom])

# mevalar = {'olma':'10000', 'behi':'15000'}
# meva = input("Qanday meva kerak? \n>>>")
# if meva in mevalar:
#     print(f"{meva}ning narxi {mevalar[meva]} so'm")
# else: print("Bu meva tugab qoldi uzr aka")


# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] =20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs")

# telefonlar = {
#     'orif':"olma",
#     'ali':"behi",
#     "vali":'nok'
#     }
# print(f"{telefonlar['vali']}")

en_uz = {'apple':'olma', 'beach':'sohil', 'fix':'tuzatmoq', 'if':'agar'}
nom =input("so'z kiriting: ").lower()
print(en_uz.get(nom.lower(), "Bunaqasi bizda yo'q"))
