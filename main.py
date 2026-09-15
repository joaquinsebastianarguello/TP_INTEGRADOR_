playlist = [] # Creamos la lista donde guardaremos las canciones

while True:
# Mostramos el menú de opciones
    print("\n=== MI PLAYLIST ===")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Calificar canción")
    print("4. Mostrar playlist")
    print("5. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")

        cancion = f"{nombre} - {artista}"
        playlist.append(cancion)

        print("Canción agregada correctamente")

    elif opcion == "2":
        nombre = input("Nombre de la canción a eliminar: ")
        print(f"Se eliminó '{nombre}'")

    elif opcion == "3":
        nombre = input("Nombre de la canción: ")
        nota = input("Calificación (1-5): ")
        print(f"'{nombre}' recibió {nota} estrellas")

    elif opcion == "4":
        print("=== PLAYLIST ===")
        if len(playlist) == 0:
            print("La playlist está vacía.")
        else:
            for cancion in playlist:
                print(cancion)

    elif opcion == "5":
        print("Saliendo del programa...")
        break
# Si el usuario introduce una opción que no existe
    else:
        print("Opción inválida")
