import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="dainos")
    
except :
    # print(e)
    print("Prisijungimo klaida")

# Kursoriaus sukūrimas
cur = cnx.cursor()

# Operacijos nurodymas:

ivestis = input("jeigu nortie prideti nauja daina iveskite raide 'p': ")

if ivestis == "p":
    pavadinimas = input("iveskite dainos pavadinima: ")
    atlikejas = input("iveskite atlikeja: ")
    zanras = input("iveskite zanra: ")
    cur.execute(f"INSERT INTO daina (pavadinimas, atlikejas, zanras) VALUES ('{pavadinimas}', '{atlikejas}', '{zanras}')")
    print("jusu daina prideta")

else:
    
    cur.execute(f"SELECT * FROM daina")

    song_list = cur.fetchall()

    for index in song_list:
        print(index)

   
cnx.commit()

# Prisijungimo uždarymas
cnx.close()