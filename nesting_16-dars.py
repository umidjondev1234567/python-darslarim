# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:17:27 2022

@author: User
"""

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'karobka':'mexanika',
#         'yil':'2013',
#         'narx':'10000$'}
# print(f"{car0['model']}, "
#       f"{car0['rang']} rang, "
#       f"{car0['narx']}")


# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'karobka':'mexanika',
#         'yil':'2013',
#         'narx':'10000$'}
# car1 = {
#         'model':'nexia',
#         'rang':'oq',
#         'karobka':'mexanika',
#         'yil':'2015',
#         'narx':'11000$'}
# car2 = {
#         'model':'cobalt',
#         'rang':'qora',
#         'karobka':'avtomat',
#         'yil':'2020',
#         'narx':'12000$'}
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model']}, "
#           f"{car['rang']} rang, "
#           f"{car['narx']}")
# print(cars[1]['rang'])


# malibus = []    
# for n in range(10):
#     car = {
#         'model':'malibu',
#         'rangi':None,
#         'yil':'2020',
#         'narh':None,
#         'karobka':'avto'
#         }
#     malibus.append(car)
# for malibu in malibus[:3]:
#         malibu['rangi']='qizil'
# for malibu in malibus[3:6]:
#     malibu['karobka']='mexanika'
# for malibu in malibus[4:]:
#     malibu['yil']='2022'
# for malibu in malibus:
#     if malibu['karobka']=='avto' and malibu['yil']=='2022':
#         malibu['narh']='40000$'
#     else: malibu['narh']='35000$'
# for malibu in malibus:
#     print(malibu)


# dasturchilar = {
#     'ali':['php', 'c#'],
#     'vali':['c++', 'sql'],
#     'hasan':['python', 'php'],
#     'husan':['html', 'css', 'js'],
#     'maryam':['java']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()}ning biladigan tillari: " , end = " ")
#     for til in tillar:
#         print(f'{til.upper()}' , end = " ")

# hamkasblar = {
#     'ali': {
#         'familiya':"valiyev",
#         'tyil':'2001',
#         'malumoti':'oliy',
#         'tillar':['php', 'c++']
#         },
#     'vali': {
#         'familiya':'aliyev',
#         'tyil':'2000',
#         'malumoti':'o\'rta',
#         'tillar':['python', 'c']
#         },
#     'hasan':{
#         'familiya':'husanov',
#         'tyil':'1997',
#         'malumoti': 'maxsus',
#         'tillar':['html', 'css', 'js']
#         }
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}. "
#           f"{info['tyil']}-yilda tug'ilgan."
#           f" Ma'lumoti: {info['malumoti'].capitalize()}")
#     print('Quyidagi tillarni biladi: ', end = " ")
#     for til in info['tillar']:
#         print(til.upper(), end = ", ")


# # AMALIYOT
# # 1-2-mashq
# sahoba1 = {
#     'ism': 'abukakr siddiq',
#     'xalifa':'1-xalifa',
#     'harf': ['a', 'b', 'c']
#     }
# sahoba2 = {
#     'ism': 'umar',
#     'xalifa': '2-xalifa',
#     'harf': ['b', 'c', 'd']
#     }
# sahoba3 = {
#     'ism': "usmon",
#     'xalifa': '3-xalifa',
#     'harf': ['c', 'd', 'e']
#     }
# sahoba4 = {
#     'ism': "ali",
#     'xalifa': '4-xalifa',
#     'harf': ['d', 'e', 'f']
#     }
# sahobalar = [sahoba1, sahoba2, sahoba3, sahoba4]
# for sahoba in sahobalar:
#     print( f"\n {sahoba['ism'].title()} rodiyallohu anhu "
#           f"{sahoba['xalifa']} bo'lgan." , end = "")
#     print('Shunchaki harf yozdim: ', end = "")
#     for xarf in sahoba['harf']:
#         print(xarf.upper(), end = " ")


# 4-mashq
# davlatlar = {
#     'uzbekistan': {
#         'capital': "tashkent",
#         'money': 'som',
#         'aholisi':'35mln'
#         },
#     'malayziya': {
#         'capital': 'kuala-lumpur',
#         'money': 'ringgit',
#         'aholisi': '25mln'
#         },
#     'russian': {
#         'capital': "moskva",
#         'aholisi': '144mln',
#         'money': "rubl"
#         }
#     }
# for kalit, qiymat in davlatlar.items():
#     if kalit.lower() == 'aqsh':
#         kalit = kalit.upper()
#     else: kalit = kalit.capitalize()
#     print(f" \n {kalit}ning poytaxti {qiymat['capital'].title()} shahri. "
#           f"\n Aholisi: {qiymat['aholisi']}."
#           f"\n Pul birligi: {qiymat['money']}.")

# 5-mashq
davlatlar = {
    'uzbekistan': {
        'poytaxt': "tashkent",
        'money': 'som',
        'aholisi':'35mln'
        },
    'malayziya': {
        'poytaxt': 'kuala-lumpur',
        'money': 'ringgit',
        'aholisi': '25mln'
        },
    'russian': {
        'poytaxt': "moskva",
        'aholisi': '144mln',
        'money': "rubl"
        }
    }
davlat = input("Qaysi davlat haqida malumot olishni hohlaysiz? \n>>> ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['money']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
    
    