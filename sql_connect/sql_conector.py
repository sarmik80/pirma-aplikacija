import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="countrydata")
    
    # Kursoriaus sukūrimas
    cur = cnx.cursor()

    # Operacijos nurodymas:

    cur.execute("SELECT * FROM country_data")

    # Jeigu norime susigrąžinti daugiau nei vieną eilutę:
    data = cur.fetchall()
    # print(data)

    # Jeigu norime susigrąžinti tik vieną eilutę:
    cur.execute(f"SELECT country_name FROM country_data WHERE gdpp = 17100")
    
    # Grąžinamas vienas rinkinys:
    data = cur.fetchone()

    # print(data)

    gdpp_data = int(input("Įveskite norimą bendrą vidaus produktą:"))
    income_data = int(input("Įveskite norimas pajamas:"))

    # Jeigu norime susigrąžinti tik vieną eilutę:
    cur.execute(f"SELECT country_name FROM country_data WHERE gdpp < {gdpp_data} and income > {income_data} ")

    data = cur.fetchall()
    
    for name in data :
        print(name[0])


    letter = str(input("Įveskite norimą raidę:"))
    
    cur.execute(f"SELECT inflation FROM country_data WHERE country_name LIKE %{letter}% ")

    data_1 = cur.fetchall()
    
    for country_name_1 in data_1 :
        print(name[0])

        
except ConnectionError as e :
    # print(e)
    print("Prisijungimo klaida")