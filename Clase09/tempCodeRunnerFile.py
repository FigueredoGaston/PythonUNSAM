def __str__(self):
        str_con_el_resultado = 'Objeto de deportes: '
        for deporte in self.contenido_marsupio.item():
            print(deporte)
            str_con_el_resultado += "\n  * {}".format(deporte)
        return str_con_el_resultado