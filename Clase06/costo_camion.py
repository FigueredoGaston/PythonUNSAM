### Ejercicio 3.9: La función zip()

import informe_funciones

def costo_camion(name_file):
    cost = 0.0
    lista = informe_funciones.leer_camion(name_file)
    for i in lista:
        cost += i['cajones'] * i['precio']
    return cost

if __name__=="__main__":
    total_cost = costo_camion('../Data/fecha_camion.csv')
    print(f"Costo total: {round(total_cost, 2)}")