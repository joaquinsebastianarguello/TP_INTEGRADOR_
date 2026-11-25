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

ranking = MaxHeap()
for cancion in bibliotecaCanciones:
    ranking.insert(cancion)

grafoMain = Graph()
mapaVertices = {}
for cancion in bibliotecaCanciones:
    vertice = grafoMain.insert_vertex(cancion) #se crea un vertice por cada cancion de biblioteca
    mapaVertices[cancion] = vertice#se crean los vertices
for cancion in bibliotecaCanciones:
    for cancion2 in bibliotecaCanciones: #si, es un for anidado (0n**2) y va a bajar el rendimiento, pero es lo
                                        #unico que se me ocurrio para poder mostrarlo, si hay tiempo lo hay que cambiar
        if cancion != cancion2:#que la cancion no se compare consigo misma
            mismoArtista = cancion._artista.lower().strip() == cancion2._artista.lower().strip()
            mismoGenero = cancion._genero.lower().strip() == cancion2._genero.lower().strip()
            if mismoArtista or mismoGenero:#buscamos el conector comun para las canciones (vertices)
                vertice1 = mapaVertices[cancion] #con el [] consultamos los vertices en el diccionario
                vertice2 = mapaVertices[cancion2]
                if mismoArtista:
                    comun = f"Mismo Artista ({cancion._artista})"
                else:
                    comun = f"Genero: {cancion._genero}"
                if grafoMain.get_edge(vertice1, vertice2) is None: #verificamos si hay aristas, si no, las crea
                    grafoMain.insert_edge(vertice1, vertice2, comun)
while True:
# Mostramos el menú de opciones
    print("\n=== DISCOTECA ===")
    print("1. BUSCADOR") #mostrar todo, acceder a informacion de una cancion en especifico
    print("2. BIBLIOTECA")#mostrar playlists, buscar entre ellas, abrirlas, agregar/eliminar cancion en playlist
    print("3. CREAR PLAYLIST")#crea una playlist vacia y la agrega a biblioteca
    print("4. FAVORITOS")#playlist default,muestra las canciones que se hayan en favoritos, buscar, agregar
    print("5. EXPLORAR CANCIONES")#muestra todo, filtrar por genero/rating
    print("6. EXPLORAR CATEGORIAS")#mustra las categorias del arbol general
    print("7. TOP CANCIONES")
    print("8. BUSQUEDA DE CANCIONES RECOMENDADAS")
    print("9. SALIR")

    opcion = input("INGRESE UNA OPCION: ")

    if opcion == "1":
        print("PARA SALIR DE ESTE MENU, INGRESE 'SALIR'")
        #METODOS TEMPORALES; BORRAR DESPUES
        print("1. BUSQUEDA SECUENCIAL")
        print("2. BUSQUEDA DE ARBOL")
        tipobusqueda = input ("INGRESE EL TIPO DE BUSQUEDA A REALIZAR: ").lower()
        #METODOS TEMPORALES; BORRAR DESPUES
        buscar = input("INGRESE EL NOMBRE DE LA CANCION: ").lower()
        #METODO TEMPORAL; BORRAR DESPUES #SE TIENE QUE PONER EL NOMBRE EXACTO DE LA CANCION PARA QUE FUNCIONE

#Comparación: el árbol es más eficiente con muchos datos, mientras que la búsqueda secuencial es más simple para pocos datos.

        if tipobusqueda == "1":
            inicio = time.perf_counter()
            resultado = None
            for i in bibliotecaCanciones:
                if i._titulo.lower().strip() == buscar.strip():
                    resultado = i
                    print(i)
            fin = time.perf_counter()
            if resultado != None:
                print(resultado)
            else:
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
                print (f"{i._nombre}")#muestra
        print("="*30)
        print("1. BUSCADOR")
        print("2. EXAMINAR PLAYLIST")
        print("3. AGREGAR CANCION A UNA PLAYLIST")
        print("4. ELIMINAR CANCION DE UNA PLAYLIST")
        print("5. SALIR")
        opcion2 = input("INGRESE UNA OPCION: ")

        if opcion2 == "1":
            buscar = input("INGRESE LA CANCION: ")
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
                buscarPlaylist = input("INGRESE LA PLAYLIST A EXAMINAR: ")
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
                buscarPlaylist = input("INGRESE LA PLAYLIST A LA QUE AÑADIR UNA CANCION: ")
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
                eliminarPlaylist = input("INGRESE LA PLAYLIST DE LA QUE REMOVER UNA CANCION: ")
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
            pass
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
            filtrarcalificacion = int(input("INGRESE LA CALIFICACION: "))
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
        print("TOP 10 CANCIONES MEJOR CALIFICADAS:")
        print("="*15)
        top = ranking.mostrar(10)
        for cancion in top:
            print(f"Titulo: {cancion._titulo} / Artista {cancion._artista} / Calificacion {cancion._calificacion}")
            print("="*15)

    elif opcion == "8":
        print("CANCIONES RECOMENDADAS:")
        print("1. CANCIONES SIMILARES")
        print("2. RECOMENDACIONES SIMILARES")#bfs
        print("3. PLAYLIST RECOMENDADA SEGUN CANCION")#dfs
        opcion = input("INGRESE UNA OPCION: ")

        if opcion == "1":
            buscar = input("INGRESE EL TITULO DE LA CANCION PARA RECOMENDACIONES SIMILARES: ").lower().strip()
            verticeEncontrado = None
            for vertice in grafoMain.vertices():#se recorre todos los vertices del grafomain (canciones)
                if vertice.element()._titulo.lower().strip() == buscar:
                    verticeEncontrado = vertice
                    break #cortamos el codigo para continuar
            if verticeEncontrado:
                cancionActual = verticeEncontrado.element() #mostramos la cancion (vertice)
                print(f"RECOMENDACION: '{cancionActual._titulo}' / ARTISTA: {cancionActual._artista}")
                print("SIMILARES:")
                tieneConexiones = False
                for arista in grafoMain.incident_edges(verticeEncontrado):#recorremos las aristas para encontrar vertices
                    opuesto = arista.opposite(verticeEncontrado)#desde vertice origen a vertice opuesto conectados por la arista
                    cancionVertex = opuesto.element()
                    print(f"   > TITULO: '{cancionVertex._titulo}' ({arista.element()})")#presencacion simple
                    tieneConexiones = True 
                if not tieneConexiones:
                    print("   > (NO SE ENCONTRARON COINCIDENCIAS)")
            else:
                print("NO SE ENCONTRO ESA CANCION.")
            pass

        elif opcion == "2": # BFS, muestra recomendaciones cercanas (primer nivel)
            buscar = input("INGRESE EL TITULO DE LA CANCION PARA RECOMENDACIONES POR CERCANIA: ").lower().strip()
            verticeEncontrado = None
            for vertice in grafoMain.vertices():#se recorre todos los vertices del grafomain (canciones)
                if vertice.element()._titulo.lower().strip() == buscar:
                    verticeEncontrado = vertice
                    break #cortamos el codigo para continuar
            if verticeEncontrado:
                descubiertas = {verticeEncontrado: None}#clave, valor
                BFS(grafoMain, verticeEncontrado, descubiertas) #ejecuta BFS nivel por nivel desde la cancion elegida
                print(f"RECOMENDACIONES POR CERCANIA DE '{verticeEncontrado.element()._titulo}':")
                conexiones = False
                for descubierta, arista in descubiertas.items():#por cada cancion cercana y conexion en descubiertas 
                                                                #nos devuelve ambas (clave valor)
                    if arista: # omite el vertice inicial
                        if arista.opposite(descubierta) == verticeEncontrado: #revisa si la cancion encontrada conecta con lo buscado
                            cancionVertex = descubierta.element() #mostramos la cancion
                            print(f"   > TITULO: '{cancionVertex._titulo}' ({arista.element()})")
                            conexiones = True
                if not conexiones:
                    print("   > NO SE ENCONTRARON SIMILARES.")
            else:
                print("NO SE ENCONTRO ESA CANCION.")

        elif opcion == "3": #DFS muestra recomendaciones en profundidad (playlist de hasta 10)
            buscar = input("INGRESE EL TITULO DE LA CANCION PARA VER UNA PLAYLIST RECOMENDADA: ").lower().strip()
            verticeEncontrado = None
            for vertice in grafoMain.vertices(): #se recorre todos los vertices del grafomain (canciones)
                if vertice.element()._titulo.lower().strip() == buscar:
                    verticeEncontrado = vertice
                    break #cortamos el codigo para continuar
            if verticeEncontrado:
                descubiertas = {verticeEncontrado: None}
                DFS(grafoMain, verticeEncontrado, descubiertas) #DFS en profundidad desde la cancion elegida
                print(f"PLAYLIST RECOMENDADA, SIMILAR A '{verticeEncontrado.element()._titulo}':")
                conexiones = False
                contador = 0 #para limitar la playlist a 10 canciones
                for descubierta, arista in descubiertas.items():
                    if arista and contador < 10:
                        cancionVertex = descubierta.element()
                        print(f"   > TITULO: '{cancionVertex._titulo}' ({arista.element()})") #presencacion simple
                        conexiones = True
                        contador += 1
                if not conexiones:
                    print("   > NO SE ENCONTRARON SIMILARES.")
            else:
                print("NO SE ENCONTRO ESA CANCION.")

    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")

