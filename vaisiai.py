import random

class Vaisius:
    def __init__(self):
        self.dydis = random.randint(5, 25)
        self.id = random.randint(1000000, 9999999)
        self.prakastas = False

    def prakasti(self):
        self.prakastas = True

class Krepšys:
    vaisiai = []

    @staticmethod
    def pripildyti():
        while len(Krepšys.vaisiai) < 20:
            Krepšys.vaisiai.append(Vaisius())
        Krepšys.vaisiai.sort(key=lambda x: x.dydis, reverse=True)

    @staticmethod
    def isimti():
        if Krepšys.vaisiai:
            return Krepšys.vaisiai.pop(0)
        else:
            return None

grauztukai = {}

# Sukuriame krepšį ir jį pripildome
Krepšys.pripildyti()

# Išimame kelis vaisius ir pridedame juos į grauztukai
for _ in range(5):
    vaisius = Krepšys.isimti()
    if vaisius:
        vaisius.prakasti()
        grauztukai[vaisius.id] = vaisius

# Vėl pripildome krepšį (turi papildyti iki 20, o ne perrašyti)
Krepšys.pripildyti()

# Patikrinimai
print("Krepšyje yra", len(Krepšys.vaisiai), "vaisiai")
print("Graužtukuose yra", len(grauztukai), "vaisiai")

# Išvedame grauztukus
for id, vaisius in grauztukai.items():
    print(f"Vaisius ID: {id}, dydis: {vaisius.dydis}, prakastas: {vaisius.prakastas}")