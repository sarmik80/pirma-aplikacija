
def amziaus_vidurkis(failas = "vardai.txt"):  # Numatytasis failo vardas

  amzius_suma = 0
  zmoniu_skaicius = 0

  with open(failas, "r") as failas_vardai:
    for eilute in failas_vardai:
      duomenys = eilute.strip().split(";")
      if len(duomenys) == 3:
        amzius = int(duomenys[2])
        amzius_suma += amzius
        zmoniu_skaicius += 1

  if zmoniu_skaicius > 0:
    vidurkis = amzius_suma / zmoniu_skaicius
    return vidurkis
  else:
    return 0  # Grąžiname 0, jei faile nėra duomenų

# Nereikia keisti failo vardo čia, nes funkcija turi numatytąjį
vidurkis = amziaus_vidurkis()  
print(f"Amžiaus vidurkis: {vidurkis}")