import math
# kiekis = 11
# kaina = 19.99
# pavadinimas = "Gera įmonė"

# print(type(kiekis))
# print(type(kaina))
# print(type(pavadinimas))

# print(8 * 4 + 2)

# print(8 * (4 + 2))

# print(48 / 4)

# print(3 + 6 * 2)

# pirmas_skaicius = 22
# antras_skaicius = 54
# rezultatas = pirmas_skaicius + antras_skaicius

# print(pirmas_skaicius)
# print(antras_skaicius)
# print("rersultatas yra: " + str(rezultatas))

# 1. Susikurkite tris kintamuosius skaičiams saugoti. Į juos
# įrašykite norimus skaičius. Raskite šių skaičių suma,
# skirtumą, sandaugą ir dalmenį. Atsakymus išveskite kartu su
# atliekamu veiksmu (pvz 8 + 2 + 4 = 14).
# 2. Susikurkite du kintamuosius skaičiams saugoti. Į juos
# įrašykite norimus skaičius. Pirmąjį kintamąjį padidinkite
# 5-iais. Antrajį padidinkite 2 kartus. Išveskite visus atsakymus
# (pradines reikšmes ir pakeistas reikšmes).

number_1 = 10
number_2 = 11
number_3 = 12
rezultatas = number_1 + number_2 + number_3

print("\n")

print("Sprendimas: ")

print("\n")

print(str(number_1) + " + " + str(number_2) + " + " + str(number_3)+ "=" + str(rezultatas))
print("skaiciu suma: " + str(number_1 + number_2 + number_3))
print("\n")
print(str(number_1) + " - " + str(number_2) + " - " + str(number_3)+ "=" + str(rezultatas))
print("skaiciu skirtumas: " + str(number_1 - number_2 - number_3))
print("\n")
print(str(number_1) * " * " + str(number_2) + " * " + str(number_3)+ "=" + str(rezultatas))
print("skaiciu sandauga: " + str(number_1 * number_2 * number_3))
print("\n")
print("skaiciu dalmuo: " + str(number_1 / number_2 / number_3))

print("\n")

skaicius_1 = 21
skaicius_2 = 25

print("pirmas skaicius: " + str(skaicius_1))
print("antras skaicius: " + str(skaicius_2))

print("\n")

print("pirmas skaicius padidintas penkiais kartais: " + str(skaicius_1 ** 5))
print("antras skaicius padidintas dviem kartais: " + str(skaicius_2 ** 2))

print("\n")

# Priskirkite savo pasirinktus skaičius kintamiesiems
# • Raskite šių skaičių sandaugą, pakelkite juos savo pasirinktu
# laipsniu;
# • Ištraukite iš šių skaičių pasirinkto laipsnio šaknį
# • Suraskite šių skaičių dalybos liekaną (dalinkite didesnį iš
# mažesnio)

pirmas_skaicius = 15
antras_skaicius = 17
pirmas_skaicius_pakeltas_laipsniu = pirmas_skaicius ** 6
antras_skaicius_pakeltas_laipsniu = antras_skaicius ** 7

print("Trecios uzduoties sprendimas: " )

print("\n")

print("Pirmo ir antro skaiciaus sandauga pakelta penktuoju laipsniu: " + str((pirmas_skaicius * antras_skaicius) ** 5))

print("\n")

print("Pirmo skaiciaus saknis: " + str( math.sqrt(pirmas_skaicius_pakeltas_laipsniu)))
print("Antro skaiciaus saknis: " + str( math.sqrt(antras_skaicius_pakeltas_laipsniu)))

print("\n")

print(" Abieju skaiciu dalybos liekana: " + str(antras_skaicius  // antras_skaicius))