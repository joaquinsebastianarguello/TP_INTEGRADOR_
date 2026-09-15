class Cancion:

    def __init__ (self, titulo, artista, genero, letra, calificacion):
        self._titulo = titulo
        self._artista = artista
        self._genero = genero
        self._letra = letra
        self._calificacion = calificacion

    def GetTitulo(self):
        return(f"{self._titulo}")

    def __repr__(self): #aparentemente el metodo NO FUNCIONA sin escribirlo como repr
        return f"{self._titulo}, {self._artista}, {self._genero}, {self._letra}, {self._calificacion}"