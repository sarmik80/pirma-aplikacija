# list = ["Vilius", 
#         "Asta", 
#         "Tomas",
#         "Aras",
#         123456
# ]

# print(list[2])
# print(len(list))
# print("\n")

# list.append("Rasa")
# print(list)

# list.insert(0,"Simonas")
# print(list)

# list.pop(5)
# print(list)

# list.insert(1,"Simonas")
# print(list.count("Simonas"))


# print(list[1:3])

# text = "Iš namų įpratusiems dirbti žmonėms ekspertai siunčia žinią: verta pagalvoti, ar nedarote sau žalos"
# print(text.split(":"))

# 1. Paprašykite vartotojo įvesti 5-is savo pažymius. Paskaičiuokite pažymių vidurkį. Išveskite atsakymą.

# pazymys_1 = input("iveskite pirma gauta pazymi: ")
# pazymys_2 = input("iveskite antra gauta pazymi: ")
# pazymys_3 = input("iveskite trecia gauta pazymi: ")
# pazymys_4 = input("iveskite ketvirta gauta pazymi: ")
# pazymys_5 = input("iveskite penkta gauta pazymi: ")
# pažymiu_suma = int(pazymys_1) + int(pazymys_2) + int(pazymys_3) + int(pazymys_4) + int(pazymys_5)
# pazymiu_vidurkis = int(pažymiu_suma) / 5

# print("Jusu pazymiu vidurkis: " + str(pazymiu_vidurkis))

# 2. Leiskite vartotojui įvesti metrus. Išveskite, kiek tai gaunasi centimetrais, milimetrais ir kilometrais.
# atstumas_metrais = input("Iveskite atstuma metrais: ")
# atstumas_centimetrais = int(atstumas_metrais) * 100
# atstumas_milimetrais = int(atstumas_metrais) * 1000
# atstumas_kilometrais = int(atstumas_metrais) / 1000

# print("jus ivedete :" + atstumas_metrais + " m") 
# print("konvertavus gauname :" + str(atstumas_centimetrais) + " cm") 
# print("konvertavus gauname :" + str(atstumas_milimetrais) + " mm")
# print("konvertavus gauname :" + str(atstumas_kilometrais) + " km")

# 3. Leiskite vartotojui įvesti du norimus skaičius. Išveskite kokia gaunasi liekana padalinus vieną skaičių iš kito.

# pirmas_skaicius = input("Iveskite pirma norima skaiciu: ")
# antras_skaicius = input("Iveskite antra norima skaiciu: ")

# liekana = int(pirmas_skaicius) % int(antras_skaicius)

# print("liekana padalinus vieną skaičių iš kito gaunasi: " + str(liekana))

# 4. Leiskite vartotojui įvesti du skaičius. Išveskite kiek gautųsi vieną skaičių pakėlus 
# kito skaičiaus laipsniu (pvz, pirmas skaičius eina už pagrindą, o antras skaičius yra laipsnis,kuriuo ir keliame).

# pirmas_skaicius = input("Iveskite pirma norima skaiciu: ")
# antras_skaicius = input("Iveskite antra norima skaiciu: ")
# skaicius_pakeltas_laipsniu = int(pirmas_skaicius) ** int(antras_skaicius)

# print("pirmas skaicius pakeltas laipsniu is antro: " + str(skaicius_pakeltas_laipsniu))



# Uždaviniai su list
# 1 uzdavinys

# • Išveskite pirmą, paskutinį elementus
# • Išveskite kas antrą elementą
# • Išveskite priešpaskutinio elemento tipą
# • Patikrinkite, ar pirmasis sąrašo elementas yra tekstas, ir kiek simbolių jis turi.

# lst = ["Python", "yra", "lengva", "programavimo", "kalba"]

# pirmas = lst[0]
# antras = lst[4]

# print(pirmas +" "+ antras)
# print(lst[::2])
# print(lst[3])
# print(type(lst[0]))
# print(len(lst[0]))

# # 2 uzdavinys Suskaičiuokite, kiek šiame tekste yra žodžių. Išveskite tekstą be kas antro žodžio

# txt = "Aš rytais mėgstu kavą su sumuštiniais ir arbatą su pyragu"
# txt_list = txt.split()
# print(txt_list)
# zodziu_kiekis = len(txt_list)
# print("tekste yra: " + str(zodziu_kiekis) + " zodziu")

# # Išveskite tekstą be kas antro žodžio
# print(txt_list[::2])

# # # 3 uzdavinys. Sąrašai gali turėti savyje bet kokį objektą, kad ir kitą sąrašą
# (sudėtinis sąrašas (nested list)).

# • Išveskite Vilniaus paminėjimo metus, žodį ”Vilnius”
# didžiosiomis raidėmis


l = ["Vilnius", 1323, ["Nupirkti maisto", "PABėgioti"], 8, "Rytas"]
# vilnius = l.pop(0)
# metai = l.pop(0)

# print("Vilniaus paminėjimo metai, žodis ”Vilnius” didžiosiomis raidėmis: " + str(vilnius.upper()) + " " + str(metai))

# # • Išveskite žodžio ”maisto” paskutines tris raides didžiosiomis.
# task_2 = l.pop(0)
# maisto = task_2.pop(0)
# did_3_maist = maisto[0:11] + maisto[12:15].upper()

# print(did_3_maist)

# • Užrašykite kodą, kuris patikrintų, ar žodžio ”Pabėgioti” pirmi trys simboliai yra didžiosios raidės.
print(l.isupper())