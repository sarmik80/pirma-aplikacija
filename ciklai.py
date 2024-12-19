# Pirma zuduotis:

# Paprašykite vartotojo įvesti simbolį bei skaičių. Išveskite
# kvadratą, sudarytą iš įvesto simbolio ir kurio kraštinė būtų
# lygi įvestam skaičiui. Pvz.: įvesta '@' ir 5. Rezultatas:
# @@@@@
# @@@@@
# @@@@@
# @@@@@
# @@@@@

# Sprendimas:

# skaicius = int(input("iveskite skaiciu: "))
# simbolis = (input("iveskite simoboli: "))

# for kvadratas in range(skaicius):
#     print(skaicius * simbolis)

# Antra uzduotis:

# Duotas sąrašas:
# miestai = ['Vilnius', 'Kaunas', 'Alytus', 'Rokiškis','Ūla', 'Mažeikiai', 'Akmena']
# Spausdinkite tik tuos miestus, kurių pavadinimai ilgesni nei 6 simboliai.

# Sprendimas:

# miestai = ['Vilnius', 'Kaunas', 'Alytus', 'Rokiškis','Ūla', 'Mažeikiai', 'Akmena']

# for print_miestai in miestai:
#     if len(print_miestai) > 6:
#         print(print_miestai)

# trecia uzduotis:

# Išspausdinkite ”pusinę” eglutę iš simbolio '*':
# Eglutės ilgį (eilučių kiekį) turi įvesti vartotojas. Eglutei naudojamą simbolį tegul įveda irgi vartotojas.

# Sprendimas:

# skaicius = int(input("iveskite skaiciu, ne mazesni, nei 5: "))
# simbolis = (input("iveskite simoboli *: "))

# skaicius = int(8)
# simbolis = "*"

# for eglute in range(skaicius):
#     print(eglute * simbolis)

# ketvirta uzduotis:

# • Išveskite po vieną simbolį iš teksto. Šalia nurodykite ir
# simbolio poziciją (indeksą) tekste.

# t = "Aš rytais mėgstu kavą su sumuštiniais ir arbatą"

# Sprendimas:

# t = "Aš rytais mėgstu kavą su sumuštiniais ir arbatą"

# for simboliai, indexas in enumerate(t):
#     print(simboliai, indexas)

# Išvesdami simbolį, spausdinkite didziosiomis rademis, jei jis
# yra lyginėje pozicijoje. Kitu atveju - mazosiomis.
# Sprendimas:-blogas

# t = "Aš rytais mėgstu kavą su sumuštiniais ir arbatą"
# for indexas, reiksme in enumerate(t):
#     print(indexas, reiksme)
#     if reiksme == " ":
#         continue
#     if indexas % 2 == 0:
#         print(reiksme.upper())
#     else:
#         print(reiksme.lower())

# Išveskite po vieną žodį.
# Sprendimas:

# t = "Aš rytais mėgstu kavą su sumuštiniais ir arbatą"
# sarasas = t.split()
# for zodziai in sarasas:
#     print(zodziai)


# Išveskite tik tuos žodžius, kurie yra ilgesni nei nurodytas
# simbolių kiekis, ir savyje turi nurodytą tekstą. Ilgį ir tekstą
# nurodo vartotojas.
# Sprendimas:

# tekstas = str(input("iveskite norima teksta: "))
# ilgis = str(input("iveskite teksto ilgi: "))
# print( "Jusu tekstas:", tekstas, "\n", "jusu zodziu  ilgis: ", ilgis)

# 2024-10-28 uzduotys
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, 
# atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.  
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

# Sprendimas:

# import random
# rezultatas = []

# for skaicius in range(301):
#     rezultatas.append(random.randint( 0, 301))
#     print(" ".join(rezultatas))
# if skaicius > 150:
#     print("Daugiau nei 150 yra skaiciu: " )

# atsitiktiniai_skaiciai = []
# didesni_uz_150 = 0

# for _ in range(301):
#     skaicius = random.randint(0, 301)
#     atsitiktiniai_skaiciai.append(skaicius)
#     if skaicius > 150:
#         didesni_uz_150 += 1

# # Atspausdiname skaičius su reikalaujamu formatavimu
# for skaicius in atsitiktiniai_skaiciai:
#     if skaicius > 275:
#         print(f"[{skaicius}]", end=" ")
#     else:
#         print(skaicius, end=" ")

# # Atspausdiname rezultatą - kiek skaičių yra didesnių už 150
# print(f"\nYra {didesni_uz_150} skaičių, didesnių už 150.")


skaicius = int(input("iveskite skaiciu, ne mazesni, nei 5: "))
simbolis = (input("iveskite simoboli *: "))

for eglute in range(skaicius):
    print(eglute * simbolis)