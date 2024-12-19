import mysql.connector
import requests
from bs4 import BeautifulSoup

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="parser")

cur = cnx.cursor()


url = "https://www.skelbimai.lt/skelbimai/nekilnojamasis-turtas/butai"

while True :
    data = requests.get(url)
    data = data.text
    html = BeautifulSoup(data, "html.parser")

    next = html.select_one('[rel="next"]')
    if next :
        next_url = html.select_one('[rel="next"]').attrs['href']
    else :
        break
    
    for skelbimai in html.select("#classifieds-list > a.classified"):


        pavadinimas = skelbimai.select_one("h2.sl").text
        aprasymas = skelbimai.select_one(".description").text
        atnaujinta = skelbimai.select_one(".modified").text
        miestas = skelbimai.select_one(".place").text
        kaina = skelbimai.select_one(".price").text

        cur.execute(f"INSERT INTO skelbimai (pavadinimas, aprasymas, atnaujinta, miestas, kaina) VALUES ('{pavadinimas}', '{aprasymas}', '{atnaujinta}', '{miestas}', '{kaina}')")
    
        cnx.commit()


    # print(atnaujinta)