# Sugeneruokite sąrašą iš 10 elementų, kurio elementai būtų sąrašai iš 5 elementų su reikšmėmis nuo 5 iki 25.

# import random

# sarasas = []

# def ten_list_of_five(sarasas):
#     vidinis_sarasas = [random.randint(5, 25) for elementai in range(10)]
#     sarasas = ten_list_of_five(sarasas)

# print(sarasas)

# import random
# def ten_list_of_five():
#     sarasas = []
#     for _ in range(10):
#         vidinis_sarasas = [random.randint(5, 25) for elements in range(5)]
#         sarasas.append(vidinis_sarasas)
#     return sarasas 
# sarasas = ten_list_of_five()
# # print(sarasas)

# # Priimdami sąrašą kaip parametrą aprašykite funkcijas kurios:
# # Suskaičiuotų kiek sąrašuose yra elementų didesnių už 10;

# def higher_than_10(sarasas):
#      count = 0
#      for mini_listas in sarasas:
#         for elementas in mini_listas:
#             if number > 10:
#                 count += 1
#         return count
     
#      kintamas = higher_than_10(sarasas)

#      print(kintamas)


# count_greater_than_10 = 0
# for mini_listas in sarasas:
#     for element in mini_listas:
#         if element > 10:
#             count_greater_than_10 += 1
# print("Count", count_greater_than_10)



#Sugeneruokite sąrašą iš 10 elementų, 
# kurio elementai būtų sąrašai iš 5 elementų su reikšmėmis nuo 5 iki 25.

import random 
def ten_list_of_five():
    sarasas = []
    for x in range(10):
        vidinis_sarasas = [random.randint(5, 25) for x in range(5)]
        sarasas.append(vidinis_sarasas)
    return sarasas 
sarasas = ten_list_of_five()
print("Gavom sarašus: ", sarasas)
#Priimdami sąrašą kaip parametrą aprašykite funkcijas kurios:
# a)Suskaičiuotų kiek sąrašuose yra elementų didesnių už 10;
def higher_than_10(sarasas):
     count = 0
     for vidinis_listas in sarasas:
        for elementas in vidinis_listas:
            if elementas > 10:
              count += 1
     return count
sarasas1 = higher_than_10(sarasas)       
print(sarasas1)

# Rastų didžiausio elemento reikšmę;

def max_value(sarasas):
    max_values = []
    for vidinis_listas in sarasas:
        max_val = max(vidinis_listas)
        max_values.append(max_val)
    return max_values
max_list = max_value(sarasas)       
print(max_list)

# Suskaičiuotų kiekvieno antro lygio sąrašo su vienodais indeksais sumas (t.y. suma reikšmių turinčių indeksą 0, 1 ir t.t.)

def similar_index_values(sarasas):
    all_values = [sum(values) for values in zip(*sarasas)]
    return all_values

sum_similar_indexes = similar_index_values(sarasas)       
print(sum_similar_indexes)

# Visus antro lygio sąrašus“pailgintų” iki 7 elementų
def add_2random_numbers(sarasas):
    for vidinis_listas in sarasas:
        vidinis_listas.extend([random.randint(5, 25) for _ in range(2)])
    return sarasas
new_sarasas = add_2random_numbers(sarasas)
print(new_sarasas)

# Suskaičiuotų kiekvieno iš antro lygio sąrašų elementų sumas ir jas panaudotų kaip reikšmes sukuriant naują masyvą. 
# Pavyzdinis rezultatas:
# [48, 49]

def sum_of_sublists_values(sarasas):
    all_sum_values = []
    for vidinis_listas in sarasas:
        sum_value = sum(vidinis_listas)
        all_sum_values.append(sum_value)
    return all_sum_values
all_sum_values = sum_of_sublists_values(sarasas)
print(all_sum_values)