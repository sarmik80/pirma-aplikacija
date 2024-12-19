# zodis_1 = "labas, "
# zodis_2 = "pasauli"

# print("\n")
# print(zodis_1.upper())
# print("\n")

# tekstas = "puikus rytas "
# print(tekstas.split())
# print(tekstas.replace("rytas" , "vakaras"))
# print(tekstas.replace("r" , "l"))
# print("\n")
# print(len(tekstas))
# print("\n")

# print(tekstas[0:5])

# Suskaičiuoti, kiek simbolių yra jūsų varde, pavardėje;

print("\n")
vardas = "Šarūnas Mikšys"
print("Vardo ir pavardės simboliai : ", len(vardas))

# • Suskaičiuoti, kiek simbolių yra pačio pirmojo delfi.lt straipsnio;
# antraštėje
delfi = "Po vaiko mirties – netikėtos problemos tėvams: mus informavo, kad tam reikalinga notaro pažyma"
print("Delfi antraštės simboliai: ", len(delfi))
print(vardas.casefold())
print("\n")

# Iš delfi antraštės atrinkite pirmus 10 simbolių; 
print(delfi[0:10])

# Iš delfi antraštės atrinkite paskutinius 10; 
print(delfi[84:94])

# Iš delfi antraštės atrinkite kas antrą; 
print(delfi[0:94:2])

# iškirpkite tekstą nuo 10-to iki 20-to simbolių;
print(delfi[9:19])
print("\n")

# Kiek delfi antraštėje yra "a" simbolių?
print('Delfi antraštėje yra "a" simbolių: ', delfi.count("a"))

# Kurioje pozicijoje yra pirmąkart sutinkamas šis simbolis?
print('Sioje pozicijoje yra pirmąkart sutinkamas šis simbolis: ', delfi.index("a"))

# Iš teksto txt="Labas rytas!" išveskite tekstą be pirmo simbolio; be paskutinio; be pirmo ir be paskutinio;
txt = "Labas rytas!"
print("Teksto ilgis: " , len(txt))
print(txt[1:])
print(txt.replace("rytas!" , "rytas"))
print(txt.replace("Labas rytas!" , "abas rytas"))

# Sukurti kintamąjį su stringu: “An American in Paris”.
# Jame visas “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.
kintamasis = "An American in Paris"
print(kintamasis.replace("A","*").replace("a","*").replace("a","*"))

# Sukurti kintamąjį su stringu: “An American in Paris”. Suskaičiuoti visas “a” (didžiąsias ir mažąsias) raides. Rezultatą atspausdinti.
print(kintamasis.count("A") + kintamasis.count("a"))

#Sukurti kintamąjį su stringu: “An American in Paris”. Jame ištrinti visas balses. 
# Rezultatą atspausdinti. 
# Kodą pakartoti su stringais: “Breakfast at Tiffany's”, “2001: A Space Odyssey” ir “It's a Wonderful Life”.
print(kintamasis.replace("a","").replace("i","").replace("A","").replace("A","").replace("e",""))
stringas = "Breakfast at Tiffany's"
print(stringas.replace("a","").replace("e","").replace("y","").replace("i",""))
stringas_1 = "2001: A Space Odyssey"
print(stringas_1.replace("a","").replace("e","").replace("A","").replace("y","").replace("O",""))
stringas_2 = "It's a Wonderful Life"
print(stringas_2.replace("a","").replace("e","").replace("u","").replace("o","").replace("I","").replace("i",""))