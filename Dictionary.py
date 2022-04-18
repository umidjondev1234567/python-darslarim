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

# en_uz = {'apple':'olma', 'beach':'sohil', 'fix':'tuzatmoq', 'if':'agar'}
# nom =input("so'z kiriting: ").lower()
# print(en_uz.get(nom.lower(), "Bunaqasi bizda yo'q"))
# print(en_uz.items())

# for key, value in en_uz.items():
#     print("Kalit:",key)
#     print("Qiymat:"+ value +'\n')

# talaba_0 = {
#     'ism':'alijon',
#     'yosh':"22",
#     'kurs':'4'
#      }
# print(talaba_0.items())
# for k, q in talaba_0.items():
#     print("kalit "+ k)
#     print("qiymat "+ q)
#     print(f"{k.title()} {q.upper()}")
    

# Amaliyot

# # 1-mashq
# izohli_lugat = {
#     'if':'agar',
#     'else':'bo\'lmasa',
#     'for':'uchun',
#     'in':'ichida',
#     'print':'Konsolga chiqarish',
#     'key':'kalit',
#     'value':'qiymat',
#     'sort':'tahlash',
#     'float':'haqiqiy',
#     'int':'butun'
#     }
# for kalit, qiymat in sorted(izohli_lugat.items()):
#     print(kalit +" - " + qiymat )

# # 2-mashq
# davlatlar = {
#     "uzbekistan":"tashkent",
#     "saudia arabia":"arriyad",
#     'aqsh':"vashington"
#     }
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.title())
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# # 3-mashq
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

# 4-mashq
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")