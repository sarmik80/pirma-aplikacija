import requests

input_word = input("Please enter what you search: ")

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + input_word

print(url)

response = requests.get(url)

data = response.json()

for drink in data["drinks"]:
    file = "coctails.txt"
    with  open (file, 'w') as file:
        file.write(f"Pavadinimas: {drink["strDrink"]}, Tipas: {drink["strAlcoholic"]}")