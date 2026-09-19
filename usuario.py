from cancion import *
from album import *

class Usuario:
    def __init__(self, nombre):
        self._nombre = nombre
        self._favoritos = []
        self._biblioteca = []

    def crearPlaylist(self, nombre):
        nueva_playlist = Playlist(nombre)
        self._biblioteca.append(nueva_playlist)

    def agregarFavoritos(self, cancion):
        self._favoritos.append(cancion)