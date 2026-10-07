from util import mostrar_menu
lista = [
    "1 para comprar comida"
    "2 para mostrar precios"
    "3 para salir"
 ]
opcion = mostrar_menu(lista)
print(f"elejiste la opcion {opcion}")
from util import buscar
lista_nombres = [
    "Ana",
    "Bruno",
    "Carla",
    "Diego",
    "Elena",
    "Fabio",
    "Gabriela",
    "Hugo",
    "Ines",
    "Juan",
    "Laura",
    "Marcos",
    "Natalia",
    "Oscar",
    "Paula",
    "Ricardo",
    "Sofía",
    "Tomas",
    "Valeria",
    "Walter"
]
nombre = input("Ingrese un nombre a buscar: ")
if buscar(lista_nombres, nombre):
    print("Encontrado")
else:
    print("No encontrado")