# pirma uzduotis
# Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius
# yra didesnis arba lygus 18-ai, jei taip - išveskite “jūs galite
# balsuoti”.

# amzius = int(input("iveskite savo amziu: "))

# if amzius >= 18:
#     print("jus galite balsuoti")
# else:
#     print("jus esate per jaunas")

# Antra uzduotis. 

# Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui,
# jūs nusimatote 3-is kintamuosius, tai leidžiate padaryti 3
# įvedimus). Raskite šių pažymių vidurkį. Patikrinkite ar
# vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip -
# išveskite 'vidurkis teigiamas'.

# pazymys_1 = int(input("Iveskite pirma pazymi: "))
# pazymys_2 = int(input("Iveskite antra pazymi: "))
# pazymys_3 = int(input("Iveskite trecia pazymi: "))
# pazymys_4 = int(input("Iveskite ketvirta pazymi: "))
# pazymys_5 = int(input("Iveskite penkta pazymi: "))

# vidurkis = (pazymys_1 + pazymys_2 + pazymys_3 + pazymys_4 + pazymys_5) / 5

# if vidurkis >= 5:
#     print("pazymiu vidurkis yra teigiamas :", vidurkis)
# else:
#     print("vidurkis yra neigiamas: ", vidurkis)

# Trecia uzduotis

# Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti
# vartotojui.
# Atlikite šiuos patikrinimus ir veiksmus:
# 1. Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus
# daugybos lentelę nuo 1 iki 5.
# 2. Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir
# jį padalintą iš 2.
# 3. Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išvskite šio skaičiaus ir 7-to sumą, skirtumą,

# trecia uzduotis. 1.

# skaicius = float(input("iveskite norima skaiciu: "))

# if skaicius % 5 == 0:
#     print( "skaicius dalinasi is 5")
# else:
#     print("skaicius nesidalina is 5")

# trecia uzduotis. 2.

# skaicius = float(input("iveskite norima skaiciu: "))

# if skaicius % 2 == 0:
#     print("skaicius yra: ", int(skaicius),",", "Skaiciaus kvadratas: ", int(skaicius ** 2), "," , "skaicius padalintas is 2: ", int(skaicius / 2))
# else:
#     print("skaicius nelyginis")

# trecia uzduotis. 3.

# skaicius = int(input("iveskite norima skaiciu: "))

# if skaicius % 7 != 0:
#     print(" Suma: ", int(skaicius + 7), "Skirtumas : ", int(skaicius - 7))
# else:
#     print("skaicius dalinasi is 7")

 
# 4 uzduotis

# Parašyti programą, kuri paklaustų dviejų skaičių, ir juos
# palygintų.

# skaicius_1 = int(input("iveskite pirma skaiciu: "))
# skaicius_2 = int(input("iveskite antra skaiciu: "))

# if skaicius_1 > skaicius_2:
#     print("Pirmas skaicius yra didesnis uz antra")
# elif skaicius_2 > skaicius_1:
#     print("Antras skaicius yra didesnis uz pirma")
# else:
#     print("Skaiciai yra lygus")


# 5 uzduotis 
# • Paklausti teksto, ir patikrinti, ar tas tekstas yra sakinyje
# "Vilnius yra UNESCO paveldas nuo 1996 metų."

# tekstas = str(input(" iveskite norima teksta: "))
# stringas = "Vilnius yra UNESCO paveldas nuo 1996 metų."

# if tekstas in stringas:
#     print("ivestas tekstas yra stringe: Vilnius yra UNESCO paveldas nuo 1996 metų")
# else:
#     print("ivesto teksto nera stringe: Vilnius yra UNESCO paveldas nuo 1996 metų")


# 6 uzduotis

# Patikrinti įvestą skaičių, ar jis yra tarp 10 ir 20. Pavyzdžiui,
# įvedus 15, turi spausdinti: "15 yra tarp 10 ir 20"

# skaicius = int(input("iveskite norima skaiciu: "))

# if skaicius >= 10 and skaicius <= 20:
#     print(f"{skaicius} yra tarp 10 ir 20")
# else:
#     print(f"'{skaicius}' skaiciaus nera tarp 10 ir 20")

# 7 uzduotis

# Patikrinti, ar vartotojo įvestas skaičius yra lyginis, ar ne.

# skaicius = int(input("iveskite norima skaiciu: "))
# if skaicius % 2 == 0:
#     print("skaicius yra lyginis")
# else:
#     print("skaicius yra nelyginis")

# 8 uzduotis

# parašyti programą 'FizzBuzz'. Įvedus skaičių, kuris dalinasi
# iš 3, spausdinamas žodis "Fizz", jei dalinasi iš 5 - "Buzz", o jei
# dalinasi ir iš 3 ir iš 5 - "FizzBuzz". Jei nesidalina nei iš 3, nei iš
# 5 - spausdinamas įvestas skaičius.

# skaicius = int(input("iveskite norima skaiciu: "))

# if skaicius % 5 == 0 and skaicius % 3 == 0:
#     print("FizzBuzz")
# elif skaicius % 3 == 0:
#     print("Fizz")
# elif skaicius % 5 == 0:
#     print("Buzz")
# else:
#     print(f"jusu ivestas skaicius {skaicius}")

# 9 uzduotis

# Patikrinkite vartotojo įvestą tekstą:
# • Ar vartotojas apskritai ką nors įvedė?
# • Ar jame vien tik skaičiai?
# • Ar jame vien tik raidės?
# • Ar jame nėra specialiųjų simbolių?
# • Kokiu registru parašytas tekstas?

# tekstas = str(input("iveskite norima teksta: "))

# if tekstas == "":
#     print(str(input("iveskite norima teksta: ")))
# elif tekstas.isnumeric():
#     print("tekste yra vien tik skaiciai")
# elif tekstas.isalpha():
#     print("tekste yra vien tik raides")
# elif tekstas.isupper():
#     print("tekstas parasytas diziosiomis raidemis")
# elif tekstas.islower():
#     print("tekstas parasytas mazosiomis raidemis")
# else:
#     print("klaida")

# 10 uzduotis 

# Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida,
# daugiau kaip 2000 vienetų- 4 % nuolaida. Parašykite programą, kuri skaičiuos žvakių kainą ir
# atspausdintų atsakymą kiek žvakių ir kokia kaina perkama. Žvakių kiekis įvedamas vartotojo (naudokite input funkciją).

# zvakes_kaina = 1
# kaina_3_proc = zvakes_kaina * 0.97
# kaina_4_proc = zvakes_kaina * 0.96

# perkamos_zvakes = int(input("Parasykite, kiek zvakiu noretumete pirkti: "))

# if perkamos_zvakes >= 1000 and perkamos_zvakes <= 2000:
#     print("Jus perkate ", perkamos_zvakes," zvakes/iu, vienos zvakes kaina: ", kaina_3_proc, "€,", "is viso moketi: ", perkamos_zvakes * kaina_3_proc, "€")
# elif perkamos_zvakes >= 2000:
#     print("Jus perkate ", perkamos_zvakes, " zvakes/iu, vienos zvakes kaina: ", kaina_4_proc, "€", "is viso moketi: ", perkamos_zvakes * kaina_4_proc, "€")
# else:
#     print("Jus perkate ", perkamos_zvakes, " zvakes/iu, vienos zvakes kaina:", zvakes_kaina, "€", "is viso moketi: ", perkamos_zvakes * zvakes_kaina, "€")

# # 11 uzduotis.

# Paprašykite vartotojo įvesti tris skaičius. Suskaičiuokite įvesčių aritmetinį vidurkį. 
# Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90. Abu vidurkius atspausdinkite. 

# skaicius_1 = int(input("Iveskite pirma skaiciu: "))
# skaicius_2 = int(input("Iveskite antra skaiciu: "))
# skaicius_3 = int(input("Iveskite trecia skaiciu: "))

# aritmetinis_vidurkis = float(skaicius_1 + skaicius_2 + skaicius_3)/3

# print("Aritmetinis vidurkis yra: ", aritmetinis_vidurkis)


# if skaicius_1 < 10 or skaicius_1 > 90:
#     print(f"apskaiciuotas vidurkis: {(skaicius_2 + skaicius_3)/2}" )
# elif skaicius_2 < 10 or skaicius_2 > 90:
#     print(f"apskaiciuotas vidurkis: {(skaicius_1 + skaicius_3)/2}" )
# elif skaicius_3 < 10 or skaicius_3 > 90:
#     print(f"apskaiciuotas vidurkis: {(skaicius_2 + skaicius_1)/2}" )
# else:
#     print("apskaiciuotas vidurkis: ", aritmetinis_vidurkis)

# 12 uzduotis

# Vartotojas įveda keturis skaičius, kurie privalo būti nuo 0 iki 2. Suskaičiuokite kiek yra įvesta nulių, vienetų ir dvejetų. 


# skaicius_1 = int(input("Iveskite pirma skaiciu nuo 0 iki 2: "))
# skaicius_2 = int(input("Iveskite antra skaiciu nuo 0 iki 2: "))
# skaicius_3 = int(input("Iveskite trecia skaiciu nuo 0 iki 2: "))
# skaicius_4 = int(input("Iveskite ketvirta skaiciu nuo 0 iki 2: "))

# nuliai = 0
# vienetai = 0
# dvejetai = 0


# if pirmas == 0 or pirmas == 0 or ppirmas == 2:
#     if skaicius_1 == 0:
#         nuliai +=1
#     if skaicius_1 == 0:
#         nuliai +=1


# sarasas = []

# sarasas.append(skaicius_1)
# sarasas.append(skaicius_2)
# sarasas.append(skaicius_3)
# sarasas.append(skaicius_4)

# count_0 = sarasas.count(0)
# count_1 = sarasas.count(1)
# count_2 = sarasas.count(2)

# print(f"Nulių yra: {count_0}")
# print(f"Vienetų yra: {count_1}")
# print(f"Dvejetų yra {count_2}")

# 13 uzduotis
# Vartotojas įveda tris skaičius. Raskite ir atspausdinkite vidurinį skaičių. 

# skaicius_1 = int(input("Įveskite skaičių:"))
# skaicius_2 = int(input("Įveskite skaičių:"))
# skaicius_3 = int(input("Įveskite skaičių:"))

# sarasas = [skaicius_1, skaicius_2, skaicius_3]
# sarasas.sort()
# print(f"Visi skaičiai: {sarasas}, vidurinis skaičius yra {sarasas[1]}")