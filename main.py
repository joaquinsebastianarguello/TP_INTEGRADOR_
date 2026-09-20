#https://elpythonista.com/json-python-leer-escribir , de aca saque la informacion para convertir la informacion json, no habia conocimiento previo
#una vez mas, la lista es la misma de la web, para tener un marco en el que trabajar
from cancion import *
from album import *
from usuario import *
import json

with open('datos.json', 'r', encoding='utf-8') as datos:
    datos = json.load(datos)

usuario = Usuario("Luis")
bibliotecaCanciones = [] #home- un generico para mostrar todo
for i in datos:
    cancion_A = Cancion(i["titulo"], i["artista"], i["genero"], i["letra"], i["calificacion"])
    bibliotecaCanciones.append(cancion_A)
#paso la explicacion pq me costo una banda, pero como ya tenemos listas reservadas, añado el generico
#una vez tengo el generico, hago que "i" buscque cada valor en datos
#aparentemente, hay que hacer una transferencia para que el formato diccionario de json sea el valor de cancion.py
#entonces haces que cancion.py sea una variante, que toma el valor "i",
#y lo añade en la carpeta "bibliotecaCanciones" hasta quedar vacio (o lleno, depende como lo veas)
#anduve viendo trabajos y probando fuerza bruta hasta que salio, siendo sincero

while True:
# Mostramos el menú de opciones
    print("\n=== DISCOTECA ===")
    print("1. BUSCADOR")
    print("2. BIBLIOTECA")
    print("3. CREAR PLAYLIST")
    print("4. FAVORITOS")
    print("5. EXPLORAR CANCIONES")
    print("6. SALIR")

    opcion = input("INGRESE UNA OPCION: ")

    if opcion == "1":
        buscar = input("INGRESE EL NOMBRE DE LA CANCION: ").lower()
        encontrado = False
        for i in bibliotecaCanciones:
            if buscar in i._titulo.lower().strip():
                encontrado = True
                print (i)
            else:
                print("NO SE ENCONTRO NINGUNA CANCION.")


    elif opcion == "5":
        for cancion in datos:
            print (cancion_A)

    elif opcion == "6":
        print("Saliendo del programa...")
        break
# Si el usuario introduce una opción que no existe
    else:
        print("Opción inválida")
