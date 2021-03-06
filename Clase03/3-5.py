import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    i=0
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        registro={}
        for fila in filas:
            registro = {
                        encabezado[0] : fila[0],
                        encabezado[1] : int(fila[1]),
                        encabezado[2] : float(fila[2])
                        }
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
