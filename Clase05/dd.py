import random

def mano_truco():
    tirada=[]
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]

    tirada.append(random.sample(naipes,k=3))
    random.shuffle(naipes)
    print(naipes)
    return tirada

#print(mano_truco())

lista = [(0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113), (0.46048787480573383, 0.640439706686113)]
adentro = list(i for i in lista if (i[0]**2 + i[1]**2)<1)
print(adentro)