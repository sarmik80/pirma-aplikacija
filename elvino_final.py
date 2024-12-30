from bs4 import BeautifulSoup
import requests
from time import sleep

base_url = "https://elenta.lt"

next_url = "/skelbimai/kompiuterija"

def get_data(base, next) :  
    response = []
    kaina = 0
    bendra_sk_kiekis = 0

    data = requests.get(base + next)

    html = BeautifulSoup(data.text, "html.parser")

    list = html.select('.units-list li')
    
      
    for listing in list :
        title = listing.select_one('a.ad-hyperlink')
        title = title.text if title else ""
        bendra_sk_kiekis += 1

        price = listing.select_one('.price-box')
        price = price.text.strip() if price else "0"
        try:
            bendra_kaina = float(price.replace("€","").replace(",","").strip())
        except ValueError:
            bendra_kaina = 0
        kaina += bendra_kaina

        response.append({
            "title": title,
            "price": price
        })
     
         
    next = html.select_one('[rel="next"]')
  
    sleep(1)

    if next:
        next_href = next.attrs['href']
        next_data, next_bendra_kaina, next_bendra_sk_kiekis = get_data(base, next_href)
        response += next_data
        kaina += next_bendra_kaina
        bendra_sk_kiekis += next_bendra_sk_kiekis

    return response, kaina, bendra_sk_kiekis


f =  open("data.csv", "w", encoding="utf8")
f.write("Title;Price\n") 
data,kaina,bendra_sk_kiekis = get_data(base_url, next_url)

for listing in data:
    f.write(f"{listing['title']};{listing['price']}\n")

f.write(f"Bendra visu skelbimu kaina: {kaina} €")
f.write(f"Bendras visus skelbymu kiekis: {bendra_sk_kiekis}")