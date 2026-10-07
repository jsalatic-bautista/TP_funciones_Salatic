def mostrar_menu(lista):
    for opcion in lista:
     print(opcion)
     opcion=int(input("Elije una opcion \n"))
    return opcion
def buscar(lista_nombres, valor_buscado):
    posicion = len(lista_nombres) - 1
    for i in range(len(lista_nombres)):
        if i > posicion:
            break
        if lista_nombres[i] == valor_buscado or lista_nombres[posicion] == valor_buscado:
            return True
        posicion = posicion - 1
    return False
        
        
    
    