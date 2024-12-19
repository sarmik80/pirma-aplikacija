import mysql.connector
import requests
from bs4 import BeautifulSoup

url = "https://www.1551.lt/automobiliu-atsargines-dalys-reikmenys/"

data = requests.get(url)

data = data.text

# print(data)

html = BeautifulSoup(data)


for box in html.select(".tm-result") :

    title = box.select_one(".uk-panel-title a span").text
    address = box.select_one(".uk-margin-right").text
    phone = box.select_one(".uk-text-right").text.replace('\n')
    description = box.select_one(".uk-width-medium-4-5 > .uk-margin").text


cnx = None

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="parser")
except :
    # print(e)
    print("Prisijungimo klaida")

cur = cnx.cursor()
    
cur.execute(f"INSERT INTO pars (title, address, description, phone) VALUES ('{title}', '{address}', '{description}','{phone}')")

cnx.commit()

cnx.close()
