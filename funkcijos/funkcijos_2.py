# # Sukurkite funkciją kuri priimtų vieną parametrą (sąrašą) ir grąžintų atgal kiek sąraše yra reikšmių didesnių už 10;

# import random

# def skaiciuGeneravimas(ilgis) :
#     skaiciai = []

#     for indeksas in range(ilgis) :
#         skaiciai.append(random.randint(5, 25))

#     return skaiciai

# skaiciai = skaiciuGeneravimas(30)

# print(skaiciai)

# def daugiau_nei_10(data):
#     sarasas = 0

#     for i in data:
#         if i > 10:
#             sarasas += 1
#     return sarasas

# funkcija = daugiau_nei_10(skaiciai)
# print(funkcija)


# c.  Sukurkite funkciją kuri suskaičiuotų visų porinių (lyginių) indeksų reikšmių sumą;

# def lyginiai(data):
#     suma = 0
#     for indexas, skaicius in enumerate(data):
#         if indexas % 2 == 0:
#             suma += skaicius
#     return suma

# poriniai = lyginiai(skaiciai)
# print(poriniai)

# d. Sukurkite funkciją kuri priimtų sąrašą ir grąžintų naują, kurio reikšmės būtų priimto sąrašo reikšmė minus indeksas;
# pvz [15, 21, 7, 8] rezultatas [15, 20, 5, 5]

# import random

# def skaiciuGeneravimas(ilgis) :
#     skaiciai = []

#     for indeksas in range(ilgis) :
#         skaiciai.append(random.randint(5, 25))

#     return skaiciai

# skaiciai = skaiciuGeneravimas(30)

# print(skaiciai)


# def fukcija(data):
#     sarasas = []
#     for indexas, skaicius in enumerate(data):
#         sarasas.append(skaicius - indexas)
#     return sarasas

# kintamasis = fukcija(skaiciai)
# print(kintamasis)


# E. Sukurkite funkciją kuri priimtų sąrašą ir grąžintų du naujus. Pirmas turi būti sudarytas iš neporinių indeksų reikšmių, 
# o kitas iš porinių; Aprašykite papildomą priimamą parametrą kurį perdavus reikšmės grąžinamuose sąrašuose būtų unikalios.



# def du_sarasai(data, data_2 = None):
#     listas_1 = []
#     listas_2 = []
#     for indexas, skaicius in enumerate(data):
#         if indexas % 2 == 0:
#             indexas += skaicius
#             listas_1.append(skaicius)
#         else:
#             listas_2.append(skaicius)
#     if data_2 == "d":
#         listas_1 = set(listas_1)
#         listas_2 = set(listas_2)
#     return  listas_1, listas_2

# sarasai = du_sarasai(skaiciai)
# print(sarasai)


# F. Sukurkite funkciją kuri priimtų sąrašą ir grąžintų jo elementus su poriniais indeksais pavertusi 0 jeigu reikšmė buvo didesnė už 15;
# pvz [18, 22, 5, 8, 16] rezultatas [0, 22, 5, 8, 0] 



# def poriniai_indexai (data):
#     sarasas = []
#     for indexas , skaicius in enumerate(data):
#         if skaicius >= 15 and indexas % 2 == 0:
#             sarasas.append(0)
#         else:
#             sarasas.append(skaicius)
#     return sarasas

# kintamasis = poriniai_indexai(skaiciai)
# print(kintamasis)


# G. Sukurkite funkciją kuri priimtų skaičius kaip parametrus (Ne kaip sąrašą) ir grąžintų pirmo skaičiaus indeksą kurio reikšmė
#  didesnė nei dešimt. Patalpinkite papildomą pasirenkamą parametrą,
#  kurį perdavus grąžinami visų skaičių kurie yra didesni nei dešimt indeksai.

# import random

# def skaiciuGeneravimas(ilgis) :
#     skaiciai = []

#     for indeksas in range(ilgis) :
#         skaiciai.append(random.randint(5, 25))

#     return skaiciai

# skaiciai = skaiciuGeneravimas(10)

# print(skaiciai)

# def parametrai( *data, daugiau = None):
#     indexai =[]
#     for indexas , skaicius in enumerate(skaiciai):
#         if skaicius > 10:
#             indexai.append(indexas)
#     return indexai

# dar_vienas_kintamasis = parametrai(skaiciai, True)


# print(dar_vienas_kintamasis)


# 3. Jums duotas stringas: “54 77 2 59 17 19 108”. Aprašykite funkciją kuri priima parametrą kaip stringą, sąrašą
#  arba argumentus perduotus per kablelį. Paimkite visus perduotus skaičius ir patikrinkite juos ar jie yra pirminiai.
#   T.y. ar natūralusis skaičius yra didesnis nei 1 ir be liekanos dalinasi tik iš savęs ir iš vieneto. 
# https://en.wikipedia.org/wiki/Prime_number 
# Funkcija turi grąžinti visus skaičius kurie yra pirminiai iš anksčiau perduotų.
# Rezultatas kurio tikimasi: [2, 59, 17, 19]

stringas = "54 77 2 59 17 19 108"


# print(string_listas)

# def rasti_pirminius_skaicius(data):
#     if 
#     string_listas = stringas.split()
#     for pirminiai in range(string_listas):


def pirminiaiSkaiciai(skaicius) :
    # 10

    for i in range(2, 10) :
        print(i)
    
pirminiaiSkaiciai(10)


