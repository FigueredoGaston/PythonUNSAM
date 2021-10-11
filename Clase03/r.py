"""dicts = {"hello":"hey", "hello":"hi", "hey":"hi", "howdy":"hello", "yo":"hi", "hello":"howdy"}
from collections import Counter
keys = Counter(dicts.values())
mode = keys.most_common(1)
"""
''' from collections import Counter
xs = [{'date': 1}, {'date': 1}, {'date': 2}, {'date': 1}, {'date': 4}]
date_counts = Counter(d['date'] for d in xs)
print({'date': date_counts.most_common(1)[0][0]}) '''

''' import pprint

dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]

pprint.pprint(dct_arr) '''

from collections import Counter

lista_a = ["A", "A","A", "A", "B", "B", "B", "B", "B", "C", "C", "D", "D", "D"]
lista_b = [23, 4, 345, 32, 534, 6, 323, 5, 323, 13, 17, 19, 23, 7]

res = dict.fromkeys(lista_a, 0)
tree_counts = Counter(d[0] for d in lista_a)
print(tree_counts)
for a, b in zip(lista_a, lista_b):
   res[a] += b / tree_counts[a]

print(*(f"{key}, {value}" for key, value in res.items()), sep="\n")

 list_local = sorted([(date['nombre_com'], date['inclinacio']) for date in list], key=lambda date: date[0])
    #Con esto trasformo la lista de diccionarios en una lista de tuplas ordenada

def mean_species_most_inclined(list):
    list_aux1 = []
    list_aux2 = []
    for tree in list:
        list_aux1.append(tree['nombre_com'])
        list_aux2.append(tree['inclinacio'])
    res = dict.fromkeys(list_aux1, 0)
    tree_counts = Counter(d[0] for d in list_aux1)
    for a, b in zip(list_aux1, list_aux2):
        if tree_counts[a] != 0:
            res[a] += b / tree_counts[a]
        else:
            res[a] += b
    return res
