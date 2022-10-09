# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 04:37:31 2022

@author: User
"""

# son = int(input('Son kiriting: '))
# while son <= 5:
#     print(son)
#     son += 1
# print("Dastur tugadi")

# print("Kiritilgan sonni kvadratini hisoblayman.")
# savol = 'Istalgan son kiriting'
# savol += '(exit-chiqish): '
# qiymat = ""
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)


# print("Kiritilgan sonni kvadratini hisoblayman.")
# savol = 'Istalgan son kiriting'
# savol += '(exit-chiqish): '
# ishora = True
# while ishora:
#     qiymat = input("Son kiriting: ")
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur tugadi")


# print("Kiritilgan sonni kvadratini hisoblayman.")
# savol = 'Istalgan son kiriting'
# savol += '(exit-chiqish): '
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat) ** 2)
        

# sonlar = list(range(1,10))
# for son in sonlar:
#     if son == 5:
#         break 
#     else: print(son ** 2)


# sonlar = list(range(1,10))
# for son in sonlar:
#     if son == 5:
#         continue
#     else: print(son ** 2)

# son = 0
# while son < 10:
#     son += 1
#     if son % 3 != 0:
#         continue
#     else: print(son)


# # AMALIYOT
# shart = 'Yaxshi ko\'rgan kitobingizni yozing '
# shart += "(stop-to'xtatish): "
# while True:
#     kitob = input(shart)
#     if kitob == 'stop':
#         break

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh == 'quit':
#         break
#     yosh = int(yosh)
    
#     if yosh <= 7:
#         narh = 1000
#     elif yosh > 7 and yosh <= 18:
#         narh = 2000
#     elif yosh > 18 and yosh <= 65:
#         narh = 3000
#     elif yosh <= 0:
#         continue
#     elif yosh > 65 and yosh <= 100:
#         narh = 'tekin'
#         print(f"Chipta narhi: {narh}so'm")
#     else: print("Parkda balo bormi sizga")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat =='exit':
        continue
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
