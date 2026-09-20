from cancion import *
from album import *

class Usuario:
    def __init__(self, nombre):
        self._nombre = nombre
        self._favoritos = [] #este queda para una playlist default de favoritos.
        self._biblioteca = [] #este queda para guardar playlists cdentro de una lista

    def crearPlaylist(self, nombre):
        nueva_playlist = Playlist(nombre)
        self._biblioteca.append(nueva_playlist)

    def agregarFavoritos(self, cancion):
        self._favoritos.append(cancion)