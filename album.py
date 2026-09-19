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

class  Playlist(Album):
    def __init__ (self, nombre):
        super().__init__(nombre) 
        #hereda todos los metodos de album, de momento es preferible que playlist sea una version de la clase album con un par de funcionalidades extra

    def nombrar(self):
        nombrenuevo = input("ingrese el nombre de la playlist: ")
        self._nombre = nombrenuevo

    def eliminar_cancion(self, cancion):
        if cancion in self._canciones:
            self._canciones.remove(cancion)
            return ("la cancion fue eliminada")
        else:
            return ("La cancion no fue encontrada")

