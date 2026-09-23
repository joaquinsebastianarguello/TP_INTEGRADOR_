#https://elpythonista.com/json-python-leer-escribir , de aca saque la informacion para convertir la informacion json, no habia conocimiento previo
#una vez mas, la lista es la misma de la web, para tener un marco en el que trabajar
from cancion import *
from album import *
from usuario import *
import json
import time

with open('datos.json', 'r', encoding='utf-8') as datos:
    datos = json.load(datos)

#SEPARADOR
# ubico aca el arbol, dentro de las opciones no funciona
class nodo_arbol:   #clase nodo arbol
    def __init__ (self, cancion):  #crea un nodo con la informacion cargada
        self.cancion = cancion
        self.izquierda = None
        self.derecha = None

def arbolVacio(raiz):
    return raiz == None
                 
def insertarNodo(raiz,cancion): #inserto el dato en el arbol
    if arbolVacio(raiz):
        raiz = nodo_arbol(cancion)
    elif raiz.cancion._titulo.lower() <= cancion._titulo.lower():
        raiz.derecha = insertarNodo(raiz.derecha, cancion)
    else:
        raiz.izquierda = insertarNodo(raiz.izquierda, cancion)
    return(raiz)

def buscarNodo(raiz, tituloBuscado):
    if arbolVacio(raiz):
        return None    
    titulo = raiz.cancion._titulo.lower().strip()
    busqueda = tituloBuscado.lower().strip()
    if busqueda == titulo:
        return raiz.cancion
    elif busqueda < titulo:
        return buscarNodo(raiz.izquierda, tituloBuscado)
    else:
        return buscarNodo(raiz.derecha, tituloBuscado)

# SEPARADOR


usuario = Usuario("Luis")
bibliotecaCanciones = [] #home- un generico para mostrar todo
for i in datos:
    cancion_A = Cancion(i["titulo"], i["artista"], i["genero"], i["letra"], i["calificacion"])
    bibliotecaCanciones.append(cancion_A) #NO TOCAR!!!!!!!!!
#paso la explicacion pq me costo una banda, pero como ya tenemos listas reservadas, añado el generico
#una vez tengo el generico, hago que "i" buscque cada valor en datos
#aparentemente, hay que hacer una transferencia para que el formato diccionario de json sea el valor de cancion.py
#entonces haces que cancion.py sea una variante, que toma el valor "i",
#y lo añade en la carpeta "bibliotecaCanciones" hasta quedar vacio (o lleno, depende como lo veas)
#anduve viendo trabajos y probando fuerza bruta hasta que salio, siendo sincero

raizArbol = None
for cancion in bibliotecaCanciones:
    raizArbol = insertarNodo (raizArbol, cancion) 
#recordatorio, a futuro cambiar los valores de busqueda por palabras que den a entender el codigo, en lugar de solo una letra

while True:
# Mostramos el menú de opciones
    print("\n=== DISCOTECA ===")
    print("1. BUSCADOR") #mostrar todo, acceder a informacion de una cancion en especifico
    print("2. BIBLIOTECA")#mostrar playlists, buscar entre ellas, abrirlas, agregar/eliminar cancion en playlist
    print("3. CREAR PLAYLIST")#crea una playlist vacia y la agrega a biblioteca
    print("4. FAVORITOS")#playlist default,muestra las canciones que se hayan en favoritos, buscar, agregar
    print("5. EXPLORAR CANCIONES")#muestra todo, filtrar por genero/rating
    print("6. SALIR")

    opcion = input("INGRESE UNA OPCION: ")

    if opcion == "1":
        print("PARA SALIR DE ESTE MENU, INGRESE 'SALIR'")
        #METODOS TEMPORALES; BORRAR DESPUES
        print("1. BUSQUEDA SECUENCIAL")
        print("2. BUSQUEDA DE ARBOL")
        tipobusqueda = input ("INGRESE EL TIPO DE BUSQUEDA A REALIZAR").lower()
        #METODOS TEMPORALES; BORRAR DESPUES
        buscar = input("INGRESE EL NOMBRE DE LA CANCION: ").lower()
        #METODO TEMPORAL; BORRAR DESPUES #SE TIENE QUE PONER EL NOMBRE EXACTO DE LA CANCION PARA QUE FUNCIONE

#Comparación: el árbol es más eficiente con muchos datos, mientras que la búsqueda secuencial es más simple para pocos datos.

        if tipobusqueda == "1":
            inicio = time.perf_counter()

            encontrado = False

            for i in bibliotecaCanciones:
                if buscar in i._titulo.lower().strip():
                    encontrado = True
                    print(i)

            fin = time.perf_counter()

            if not encontrado:
                print("NO SE ENCONTRO NINGUNA CANCION.")

            tiempo = (fin - inicio) * 1000

            print(f"Tiempo de búsqueda: {tiempo:4f} segundos")
            print("Complejidad: O(n)")

        elif tipobusqueda == "2":
            inicio = time.perf_counter()

            resultado = buscarNodo(raizArbol, buscar)

            fin = time.perf_counter()

            if resultado != None:
                print(resultado)
            else:
                print("NO SE ENCONTRO NINGUNA CANCION")

            tiempo = (fin - inicio) * 1000

            print(f"Tiempo de búsqueda: {tiempo:4f} segundos")
            print("Complejidad promedio: O(log n)")
            print("Complejidad peor caso: O(n)")
	

    elif opcion == "2":
        biblioteca = usuario._biblioteca
        if len(biblioteca) == 0:
            print("NO HAY ELEMENTOS EN LA BIBLIOTECA")
        else:
            for i in biblioteca:
                print (i)#muestra
                print("="*30)
                print("1. BUSCADOR")
                print("2. EXAMINAR PLAYLIST")
                print("3. AGREGAR CANCION A UNA PLAYLIST")
                print("4. ELIMINAR CANCION DE UNA PLAYLIST")
                print("5. SALIR")

    elif opcion == "3":
        print("PARA SALIR DE ESTE MENU, INGRESE 'SALIR'")
        crear = input("INGRESE UN NOMBRE PARA LA NUEVA PLAYLIST: ")
        if crear == "1":
            break
        else:
            usuario.crearPlaylist(crear)
            print("PLAYLIST AÑADIDA")

    elif opcion == "4":
        favoritos = usuario._favoritos
        if len(biblioteca) == 0:
            print("NO HAY ELEMENTOS EN LA BIBLIOTECA")
        else:
            for i in favoritos:
                print (i)#muestra
                print("="*30)
                print("1. BUSCADOR")
                print("2. AGREGAR CANCION A UNA PLAYLIST")
                print("3. ELIMINAR CANCION DE UNA PLAYLIST")
                print("4. SALIR")
        

    elif opcion == "5":
        for cancion in bibliotecaCanciones:
            print (cancion)
        print("="*30)
        print("1.FILTRAR POR GENERO")
        print("2. FILTRAR POR CALIFICACION")
        print("3. SALIR")

    elif opcion == "6":
        print("Saliendo del programa...")
        break
# Si el usuario introduce una opción que no existe
else:
        print("Opción inválida")

