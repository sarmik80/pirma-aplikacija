import mysql.connector
import requests
from bs4 import BeautifulSoup

# Prisijungimas prie serverio:
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="parser")

cur = cnx.cursor()

url = "https://sutarta.lt/skelbimai/garso-vaizdo-foto-technika/vaizdo-video-technika"

data = requests.get(url)

data = data.text

# print(data)



html = BeautifulSoup(data, "html.parser")


for listing in html.select(".list li") :
    if listing.select_one(".list-media") :
        continue
    

    patalpinimo_laikas = listing.select_one("div.list-date").text
    nuotrauka = listing.select_one("img")
    nuotrauka = nuotrauka.attrs['src'] if nuotrauka else ""
    pavadinimas = listing.select_one("div.desc-title a").text
    kaina = listing.select_one(" div.desc > div.section").text
    kategorija = listing.select_one(".section-category a").text
    miestas = listing.select_one(" div.cat-geo.clean-links > div:nth-child(2) > a").text
    tipas = listing.select_one("div.cat-geo.clean-links > div.section.action-type").text

    cur.execute(f"INSERT INTO sutarta (laikas, nuotrauka, pavadinimas, kaina, kategorija, miestas, tipas) VALUES ('{patalpinimo_laikas}', '{nuotrauka}', '{pavadinimas}', '{kaina}', '{kategorija}', '{miestas}', '{tipas}')")
    
    cnx.commit()
    



    # print(tipas)


# print(f"INSERT INTO sutarta (laikas, nuotrauka, pavadinimas, kaina, kategorija, miestas, tipas) VALUES ('{patalpinimo_laikas}', '{nuotrauka}', '{pavadinimas}','{kaina}'), '{kategorija}, '{miestas}, '{tipas}')")
