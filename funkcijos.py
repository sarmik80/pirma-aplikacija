# Parašyti funkciją, kurioje sugeneruojamos dvi skaičių sekos
# (jos gali būti skirtingo dydžio), programa turi grąžinti sąrašą
# skaičių, kurie sutampa tarp dviejų sugeneruotu sąrašų,
# galutiniame sąraše neturi būti skaičių dublikatų. PVZ: x =[1, 1,
# 2, 3, 1] y = [1, 3, 5, 6] atsakymas = [1,3]

# import random

# def bendri_elementai():
#     # Sugeneruojame dvi atsitiktines skaičių sekas
#     x = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
#     y = [random.randint(1, 10) for _ in range(random.randint(5, 10))]

#     # Randame bendrus elementus ir pašaliname dublikatus
#     bendri = list(set(x) & set(y))

#     return bendri

# # Pavyzdys
# atsakymas = bendri_elementai()
# print("Bendri elementai:", atsakymas)

# Pirma dalis: Aprašykite funkciją kuri patikrinintų duomenis ir grąžintų visų produktų kainos sumą, bei įvertinimo vidurkį.

# Antra dalis, iš vieno iš produktų žodyno pašalinkite kainos raktažodį su reikšme. Modifikuokite funkciją, jog iš išmestų klaidą (assert), jeigu prie duomenų truksta bent vienos nurodytos kainos.

duomenys = [
    {
        "pavadinimas": "3-jų lentynų komplektas Tobi 3P, baltas",
        "kaina": 49.41,
        "ivertinimas": 3.7
    },
    {
        "pavadinimas": "Pakabinama sieninė lentyna Bilbao 4P, balta matinė",
        "kaina": 508.22,
        "ivertinimas": 4.8
    },
    {
        "pavadinimas": "Lentyna R60, balta",
        "kaina": 47.41,
        "ivertinimas": 2.5
    }
]

def tikrinimo_funkcija(duomenys):
    kainos = 0
    ivertinimai = 0
    produktai = len(duomenys)

    for produktas in duomenys:
        kainos += produktas["kaina"]
        ivertinimai += produktas ["ivertinimas"]

    vidurkis = ivertinimai / produktai

    return {"kainu suma": kainos, "vidurkis": vidurkis}

rezultatas = tikrinimo_funkcija(duomenys)
print(rezultatas)