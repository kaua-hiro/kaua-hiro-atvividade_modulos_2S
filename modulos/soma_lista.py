def somar_lista_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + somar_lista_recursiva(lista[1:])