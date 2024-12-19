import mysql.connector
import requests
from bs4 import BeautifulSoup

url = "https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/4"

data = requests.get(url)

data = data.text

# print(data)

html = BeautifulSoup(data, "html.parser")


for box in html.select("li id") :

    patalpinimo_laikas = listing.select_one(".list-date").text
    nuotrauka = listing.select_one("").text
    pavadinimas = listing.select_one("").text
    kaina = listing.select_one("").text
    kategorija = listing.select_one("").text
    miestas = listing.select_one("").text
    tipas = listing.select_one("").text
    
    print(patalpinimo_laikas)

# print(html)

# cnx = None

# try :
#     # Prisijungimas prie serverio:
#     cnx = mysql.connector.connect(
#         host="127.0.0.1",
#         port=3306,
#         user="root",
#         password="",
#         database="parser")
# except :
#     # print(e)
#     print("Prisijungimo klaida")

# cur = cnx.cursor()
    
# cur.execute(f"INSERT INTO pars (title, address, description, phone) VALUES ('{title_1}', '{address}', '{description}','{phone}')")

# cnx.commit()

# cnx.close()
