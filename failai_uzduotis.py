# Pirma sąlyga: 
# Išfiltruokite ir grąžinkite vartotojus kurių slaptažodžiuose nėra skaičių.



# data = open("zmoniu_duomenys.txt", "r")

# zmoniu_sarasas = data.readlines()

# psw_be_skaiciu = []

# for eilute in zmoniu_sarasas[1:]:
#     psw_data = eilute.split(";")
#     psw = psw_data[4]

#     ar_yra_skaitmuo = False
#     for simbolis in psw:
#         if simbolis.isdigit():
#             ar_yra_skaitmuo = True
#             break

#     if not ar_yra_skaitmuo:
#         psw_be_skaiciu.append(psw_data)

# for vartotojas in psw_be_skaiciu:
#     print(f"VARDAS:{vartotojas[0]}, SLAPTAŽODIS: {vartotojas[4]}")


# Antra sąlyga:
# Išfiltruokite vartotojus kurie neturi gimimo metų.


# data = open("zmoniu_duomenys.txt", "r")

# for line in data.readlines()[1:]:
#     l = line.split(";")

#     if l[3]:
#         print(line)


# Trečia sąlyga: 
# Išveskite visų vartotojų amžiaus vidurkį.

# data = open("zmoniu_duomenys.txt", "r")

# eilutes = data.readlines()
# amzius = []
# amziaus_suma = 0

# for eilute in eilutes[1:]:
#     zmogus = eilute.strip().split(";")

#     amziaus_suma += 2024 - int(zmogus[3]) if zmogus[3] else 0

# print(amziaus_suma / len(eilutes[1:]))


# Ketvirta sąlyga:
# Išfiltruokite vartotojus su neteisingais el. pašto adresais.

# def ar_el_pastas_neteisingas(el_pastas):
#   """
#   Patikrina, ar el. pašto adresas atrodo neteisingas.

#   Ši funkcija yra supaprastinta ir netikrina visų galimų klaidų,
#   bet tinka pradedantiesiems suprasti pagrindinę logiką.

#   Args:
#     el_pastas: El. pašto adresas (tekstas).

#   Returns:
#     True, jei el. pašto adresas atrodo neteisingas, kitaip False.
#   """
#   if "@" not in el_pastas or "." not in el_pastas:
#     return True  # El. pašto adresas turi turėti "@" ir "." simbolius
#   return False

# def filtruoti_vartotojus(failo_vardas):
#   """
#   Išfiltruoja vartotojus su neteisingais el. pašto adresais iš failo.

#   Args:
#     failo_vardas: Failo, kuriame yra vartotojų duomenys, pavadinimas.

#   Returns:
#     Sąrašas vartotojų su neteisingais el. pašto adresais.
#   """
#   neteisingi_vartotojai = []
#   with open("zmoniu_duomenys.txt", "r") as failas:
#     next(failas)  # Praleisti pirmąją eilutę (stulpelių pavadinimai)
#     for eilute in failas:
#       duomenys = eilute.strip().split(";")
#       zmogus = {
#           "vardas": duomenys[0],
#           "pavarde": duomenys[1],
#           "el_pastas": duomenys[2],
#           "gimimo_metai": duomenys[3],
#           "slaptazodis": duomenys[4],
#       }
#       if ar_el_pastas_neteisingas(zmogus["el_pastas"]):
#         neteisingi_vartotojai.append(zmogus)
#   return neteisingi_vartotojai

# # Pavyzdys
# failo_pavadinimas = "zmoniu_duomenys.txt"  # Pakeiskite į savo failo pavadinimą
# neteisingi_zmones = filtruoti_vartotojus(failo_pavadinimas)

# # Atspausdinkite žmonių su neteisingais el. pašto adresais sąrašą
# for zmogus in neteisingi_zmones:
#   print(f"{zmogus['vardas']} {zmogus['pavarde']} ({zmogus['el_pastas']})")




# Penkta sąlyga:
# Išfiltruokite vartotojus kurių slaptažodžiai yra trumpesni nei 5 simboliai.

# data = open("zmoniu_duomenys.txt", "r")

# for line in data.readlines()[1:] :
#     l = line.strip().split(";")
    
#     if len(l[4]) <= 5:
#         print(line[4])


# Šešta sąlyga:
# Išfiltruokite vartotojus kurie nėra įvedę pavardės.


