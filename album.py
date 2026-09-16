from cancion import Cancion

class Album:
    def __init__(self, nombre):
        self._nombre = nombre
        self._canciones = [] #aplicar con playlists

    def agregarCancion(self, cancion):
        self._canciones.append(cancion)

    def listar(self):
        for cancion in self._canciones:
            print(cancion)
        return

    def filtrar(self):
        resultado = []
        coincidencias = False
        genero = input("ingrese el genero a filtrar: ")
        for cancion in self._canciones:
            if cancion._genero.lower() == genero.lower():
                resultado.append(cancion)
                coincidencias = True
        if coincidencias == False:
            return ("no se encontraron coincidencias")
        else:
            return(resultado)


    def buscar(self):
        resultado = []
        coincidencias = False
        titulo = input("ingrese el titulo a buscar: ")
        for cancion in self._canciones:
            if cancion._titulo.lower() == titulo.lower():
                resultado.append(cancion)
                coincidencias = True
        if coincidencias == False:
            return ("no se encontro dicho elemento")
        else:
            return(resultado)

# PRUEBAS :

if __name__ == "__main__":
    # lista sacada online btw, generico hasta tener una base de datos
    c1 = Cancion("De Musica Ligera", "Soda Stereo", "Rock", "Ella durmio...", "5 estrellas")
    c2 = Cancion("Tratame Suavemente", "Soda Stereo", "Rock", "Alguien me dijo...", "5 estrellas")
    c3 = Cancion("Hello", "Adele", "Pop", "Hello, it's me...", "5 estrellas")
    c4 = Cancion("Hello", "Lionel Richie", "Pop", "I've been alone...", "5 estrellas")

    album = Album("Colección Principal")
    album.agregarCancion(c1)
    album.agregarCancion(c2)
    album.agregarCancion(c3)
    album.agregarCancion(c4)

    print("LISTAR")
    album.listar()

    print("FILTRAR")
    print(album.filtrar())

    print("BUSCAR")
    # ver que hacer a futuro con repetidos. agregar un decorador para separar los resultados, o dejarlo mas prolijo
    print(album.buscar()) 
