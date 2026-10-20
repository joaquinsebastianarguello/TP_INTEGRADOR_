#https://elpythonista.com/json-python-leer-escribir , de aca saque la informacion para convertir la informacion json, no habia conocimiento previo
#una vez mas, la lista es la misma de la web, para tener un marco en el que trabajar
from cancion import *
from album import *
from usuario import *
from arboles_auxiliares import *
import json
import time

with open('datos.json', 'r', encoding='utf-8') as datos:
    datos = json.load(datos)

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

raizArbolGeneral = nodo_arbol_general("Biblioteca por categorias")
for cancion in bibliotecaCanciones:
    agregarCancionPorGenero(raizArbolGeneral, cancion)

while True:
# Mostramos el menú de opciones
    print("\n=== DISCOTECA ===")
    print("1. BUSCADOR") #mostrar todo, acceder a informacion de una cancion en especifico
    print("2. BIBLIOTECA")#mostrar playlists, buscar entre ellas, abrirlas, agregar/eliminar cancion en playlist
    print("3. CREAR PLAYLIST")#crea una playlist vacia y la agrega a biblioteca
    print("4. FAVORITOS")#playlist default,muestra las canciones que se hayan en favoritos, buscar, agregar
    print("5. EXPLORAR CANCIONES")#muestra todo, filtrar por genero/rating
    print("6. EXPLORAR CATEGORIAS")#mustra las categorias del arbol general
    print("7. SALIR")

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
            print(f"Tiempo de búsqueda: {tiempo:.4f} segundos")
            print("Complejidad: O(n)")

        elif tipobusqueda == "2":
            inicio = time.perf_counter()
            resultado = buscarNodo(raizArbol, buscar)
            fin = time.perf_counter()
            if resultado != None:
                print(resultado)
            else:
                print("NO SE ENCONTRO NINGUNA CANCION") #me molestaba un poco todos los espacion en medio, al menos asi separo los bloques

            tiempo = (fin - inicio) * 1000

            print(f"Tiempo de búsqueda: {tiempo:.4f} segundos")
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
        opcion2 = input("INGRESE UNA OPCION: ")

        if opcion2 == "1":
            buscar = input("INGRESE LA CANCION")
            encontrado = False
            for cancion in bibliotecaCanciones:
                if buscar.lower().strip() == cancion._titulo.lower().strip(): #esto sale de cancion.py
                    print(cancion)
                    encontrado = True
            if not encontrado:
                print("NO SE ENCONTRO NINGUNA CANCION")

        elif opcion2 == "2":
            if len(biblioteca) == 0:
                print("NO HAY PLAYLISTS A EXAMINAR")
            else:
                buscarPlaylist = input("INGRESE LA PLAYLIST A EXAMINAR:")
                encontrado = None
                for playlist in biblioteca:
                    if playlist._nombre.lower().strip() == buscarPlaylist.lower().strip(): #esto sale de album.py
                        encontrado = playlist
                if encontrado:
                    encontrado.listar()
                else:
                    print("NO SE ENCONTRO DICHA PLAYLIST")

        elif opcion2 == "3":
            if len(biblioteca) == 0:
                print("NO HAY PLAYLISTS A EXAMINAR")
            else:
                buscarPlaylist = input("INGRESE LA PLAYLIST A LA QUE AÑADIR UNA CANCION:")
                playlistencontrado = None
                for playlist in biblioteca:
                    if playlist._nombre.lower().strip() == buscarPlaylist.lower().strip():#esto sale de album.py igual que arriba
                        playlistencontrado = playlist
                if playlistencontrado:
                    agregar = input("INGRESE EL TITULO DE LA CANCION A AÑADIR: ")#pasos extra para buscar la camcion de cancion.py
                    encontrado = None
                    for cancion in bibliotecaCanciones:
                        if cancion._titulo.lower().strip() == agregar.lower().strip():
                            encontrado = cancion
                    if encontrado:
                        playlistencontrado.agregarCancion(encontrado)
                        print("CANCION AGREGADA A LA PLAYLIST.")
                    else:
                        print("NO SE ENCONTRO DICHA CANCION.")
                else:
                    print("NO SE ENCONTRO DICHA PLAYLIST.")

            pass

        elif opcion2 == "4":
            if len(biblioteca) == 0:
                print("NO HAY PLAYLISTS A EXAMINAR")#esto es lo mismo que la opcion de arriba pero a la inversa, tmb de album.py
            else:
                eliminarPlaylist = input("INGRESE LA PLAYLIST DE LA QUE REMOVER UNA CANCION:")
                playlistencontrado = None
                for playlist in biblioteca:
                    if playlist._nombre.lower().strip() == eliminarPlaylist.lower().strip():
                        playlistencontrado = playlist
                if playlistencontrado:
                    eliminar = input("INGRESE EL TITULO DE LA CANCION A ELIMINAR: ")
                    encontrado = None
                    for cancion in bibliotecaCanciones:
                        if cancion._titulo.lower().strip() == eliminar.lower().strip():
                            encontrado = cancion
                    if encontrado:
                        playlistencontrado.eliminar_cancion(encontrado)
                        print("CANCION ELIMINADA DE LA PLAYLIST.")
                    else:
                        print("NO SE ENCONTRO DICHA CANCION.")
                else:
                    print("NO SE ENCONTRO DICHA PLAYLIST.")
            pass
    
        else:
            opcion2 == "5"
            pass


    elif opcion == "3":
        print("PARA SALIR DE ESTE MENU, INGRESE '1'")
        crear = input("INGRESE UN NOMBRE PARA LA NUEVA PLAYLIST (o '1' para salir): ")
        if crear == "1":
            break
        else:
            usuario.crearPlaylist(crear)
            print("PLAYLIST AÑADIDA")

    elif opcion == "4":
        favoritos = usuario._favoritos
        if len(favoritos) == 0:
            print("NO HAY ELEMENTOS EN LA BIBLIOTECA")
        else:
            for i in favoritos:
                print (i)#muestra
        print("="*30)
        print("1. BUSCADOR")
        print("2. AGREGAR CANCION A FAVORITOS")
        print("3. ELIMINAR CANCION DE FAVORITOS")
        print("4. SALIR")
        opcion4 = input("INGRESE UNA OPCION: ")

        if opcion4 == "1": #iba a hacer un buscador, pero ahora no estoy tan seguro de que tan necesario sea, o que funcion realmente agregaria
            #que fuese realmente importante, a lo mejor hay que darle unas vueltas a eso o descartarlo
            pass

        elif opcion4 == "2":
            agregar = input("INGRESE LA CANCION QUE BUSCA AGREGAR: ")
            encontrado = None # como no tengo el valor a encajar en la lista, hago esto, como en las listas enlazadas
            for cancion in bibliotecaCanciones:
                if cancion._titulo.lower().strip() == agregar.lower().strip():
                    encontrado = cancion
                    usuario.agregarFavoritos(cancion)
                    print("CANCION AGREGADA")
                else:
                    print("NO SE ENCONTRO DICHA CANCION")

        elif opcion4 == "3":
            eliminar = input("INGRESE LA CANCION QUE BUSCA ELIMINAR: ")
            encontrado = None
            for cancion in bibliotecaCanciones:
                if cancion._titulo.lower().strip() == eliminar.lower().strip():
                    encontrado = cancion
                    usuario._favoritos.remove(cancion)
                    print("CANCION ELIMINADA")
                else:
                    print("NO SE ENCONTRO DICHA CANCION")

        elif opcion4 == "4":
            pass
        

    elif opcion == "5":
        for cancion in bibliotecaCanciones:
            print (cancion)
        print("="*30)
        print("1.FILTRAR POR GENERO")
        print("2. FILTRAR POR CALIFICACION")
        print("3. SALIR")
        filtrar = input("ELIJA UNA OPCION: ")
        if filtrar == "1":
            filtrarGenero = input("INGRESE EL GENERO A BUSCAR: ")
            encontrado = False
            for cancion in bibliotecaCanciones:
                if cancion._genero.lower().strip() == filtrarGenero.lower().strip():
                        print(cancion)
                        encontrado = True
            if not encontrado:
                print ("NO SE ENCONTRO NINGUNA CANCION.")
        elif filtrar == "2":
            filtrarcalificacion = int(input("INGRESE LA CALIFICACION:"))
            encontrado = False
            for cancion in bibliotecaCanciones:
                if cancion._calificacion== filtrarcalificacion:
                        print(cancion)
                        encontrado = True
            if not encontrado:
                print ("NO SE ENCONTRO NINGUNA CANCION.")

    elif opcion == "6":
        print("CATEGORÍAS:")
        print("="*15)
        mostrarArbolGeneral(raizArbolGeneral)

    elif opcion == "7":
        print("Saliendo del programa...")
        break
# Si el usuario introduce una opción que no existe
    else:
        print("Opción inválida")

