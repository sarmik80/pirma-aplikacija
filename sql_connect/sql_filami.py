import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="filmai")
    
except :
    # print(e)
    print("Prisijungimo klaida")

cur = cnx.cursor()

sarasas = cur.execute(f"SELECT * FROM filmas")
print(sarasas)

# veiksmas = input("pasirinkite, ka norite atlikti:\nN - Naujas įrašas\nE - Įrašo redagavimas\nD - Įrašo ištrynimas\nĮveskite pasirinkta simbolį")

# sukurti =
# redagaguoti =
# trinti =


# Kursoriaus sukūrimas
cur = cnx.cursor()
cnx.commit()
