# • Parašykite klasę, turinčią konstruktorių. Konstruktorius turi
# spausdinti pranešimą, jog objektas yra sukurtas.
# Sprendimas



# class Klase:
#     def __init__(self):
#         print("Objektas sukurtas!")
# objektas = Klase()


# Parašykite klasę, kuri turėtų konstruktorių, destruktorių. Abu
# turi spausdinti informacinį pranešimą, jog objektas yra
# sukurtas/sunaikintas.

# Sprendimas

# class Car():
#     def __init__ (self):
#         print("Object was created")

#     def __del__ (self):
#         print("Object was deleted")
        
# for i in range(1):
#     item = Car()

# Parašykite klasę, kuri turėtų vieną atributą. Pasiekite jo
# reikšmę, išveskite. Pakeiskite atributo reikšmę. Patikrinkite,
# ar reikšmė pakito.

# Sprendimas

# class Phone():
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color


# smartphone = Phone("Samsung")

# print(smartphone.brand)

# smartphone.brand = "Iphone"

# print(smartphone.brand)


# Prie ankstesnės klasės pridėkite metodus, skirtus išvesti
# atributo reikšmę, pakeisti atributo reikšmę. patikrinkite, ar jie
# veikia.


# class Phone():
#     def __init__(self, brand,):
#         self.brand = brand

#     def get_brand(self):
#         return self.brand

#     def set_brand(self, brand):
#         self.brand = brand


# smartphone = Phone("Samsung")

# print(smartphone.get_brand()) 

# smartphone.set_brand("Iphone")

# print(smartphone.get_brand())


# Aprašykite klasę “Televizorius” su nurodytomis savybėmis: 

# Gamintojas, 
# Kanalas 
# Garsas. 

# Gamintojo pavadinimą priskirkite konstruktoriuje kaip gautą parametrą. 
# Vos tik įjungus televizorių turėtų būti parinktas pirmas kanalas, o garso lygis 50. Sukurkite metodus kurie padidintų ir sumažintų televizoriaus garsą, 
# tačiau šis niekuomet negali būti žemiau nei 0 ir aukščiau nei 100. 
# Sukurkite metodą kuris keistų kanalą, tačiau atkreipkite dėmesį, kad gal televizorius jų turi tik 50,
# tad jei pultelyje įvesite didesnį skaičių, kanalas turi būti pakeičiamas į pirmajį.
# Sukurkite metodą, kuris atstatytų televizorių atgal į gamyklinius parametrus.
# Sukurkite metodą, kuris grąžintų eilutę “Televizorius ‘Sony’ šiuo metu rodo 8 kanalą. Garso lygis 76.”

class Televizorius:
    def __init__(self, gamintojas, kanalas, garsas):
        self.gamintojas = gamintojas
        self.kanalas = 1
        self.garsas = 50

    def pagarsinti(self):
        if self.garsas
    


