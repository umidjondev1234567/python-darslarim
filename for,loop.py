# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 06:26:46 2022

@author: Ne'matov Umidjon
for loop
"""

# mehmonlar = ['Ali', 'Vali', 'Soli', 'Abdulloh']
# print("Assalomu alaykum ", mehmonlar[3])

# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print(mehmon)

# mehmonlar = ['Rustam', 'Lola', 'Ergash']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} sizni 12-aprel kuni nahorgi oshga taklif etamiz")
#     print("Hurmat bilan Musulmonlar oilasi")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(10))
# sonlar_kv = []
# for son in sonlar:
#     sonlar_kv.append(son**2)
# print(sonlar_kv)

# menyu = []
# print("Nima buyurasiz?")
# for n in range(1,3):
#     menyu.append(input(f"{n}-siga nima buyurasiz: "))
# print(menyu)
# print(f"Kod {n} marta takrorlandi")

# sonlar = list(range(10, 100, 10))
# for son in sonlar:
#     print(son**3)

kinolar = []

for n in range(int(input("Nechta kinoni yoqtirasiz: "))):
    kinolar.append(input(f"Yoqtirgan {n+1}-kinoingiz: "))
print("Demak siz yoqtirgan kinolar ro'yhati quyidagilar: \n", kinolar)
