
# ARBOL AVL PARA DISCOTECA

class nodo_avl:
    def __init__(self, cancion):
        self.cancion = cancion
        self.izquierda = None
        self.derecha = None
        self.altura = 1


def obtenerAltura(raiz):
    if raiz is None:
        return 0
    return raiz.altura


def actualizarAltura(raiz):
    raiz.altura = 1 + max(
        obtenerAltura(raiz.izquierda),
        obtenerAltura(raiz.derecha)
    )


def factorEquilibrio(raiz):
    if raiz is None:
        return 0

    return (
        obtenerAltura(raiz.izquierda)
        - obtenerAltura(raiz.derecha)
    )


# ROTACION SIMPLE A LA DERECHA
def rotarDerecha(y):
    x = y.izquierda
    subarbol = x.derecha

    x.derecha = y
    y.izquierda = subarbol

    actualizarAltura(y)
    actualizarAltura(x)

    return x


# ROTACION SIMPLE A LA IZQUIERDA
def rotarIzquierda(x):
    y = x.derecha
    subarbol = y.izquierda

    y.izquierda = x
    x.derecha = subarbol

    actualizarAltura(x)
    actualizarAltura(y)

    return y


# INSERTAR CANCION Y EQUILIBRAR
def insertarAVL(raiz, cancion):
    if raiz is None:
        return nodo_avl(cancion)

    titulo = cancion._titulo.lower().strip()
    titulo_raiz = raiz.cancion._titulo.lower().strip()

    if titulo < titulo_raiz:
        raiz.izquierda = insertarAVL(raiz.izquierda, cancion)
    elif titulo > titulo_raiz:
        raiz.derecha = insertarAVL(raiz.derecha, cancion)
    else:
        # No insertar dos veces el mismo titulo
        return raiz

    actualizarAltura(raiz)
    equilibrio = factorEquilibrio(raiz)

    # CASO IZQUIERDA-IZQUIERDA
    if equilibrio > 1 and titulo < raiz.izquierda.cancion._titulo.lower().strip():
        return rotarDerecha(raiz)

    # CASO DERECHA-DERECHA
    if equilibrio < -1 and titulo > raiz.derecha.cancion._titulo.lower().strip():
        return rotarIzquierda(raiz)

    # CASO IZQUIERDA-DERECHA
    if equilibrio > 1 and titulo > raiz.izquierda.cancion._titulo.lower().strip():
        raiz.izquierda = rotarIzquierda(raiz.izquierda)
        return rotarDerecha(raiz)

    # CASO DERECHA-IZQUIERDA
    if equilibrio < -1 and titulo < raiz.derecha.cancion._titulo.lower().strip():
        raiz.derecha = rotarDerecha(raiz.derecha)
        return rotarIzquierda(raiz)

    return raiz


# BUSCAR CANCION
def buscarAVL(raiz, tituloBuscado):
    if raiz is None:
        return None

    titulo = raiz.cancion._titulo.lower().strip()
    busqueda = tituloBuscado.lower().strip()

    if busqueda == titulo:
        return raiz.cancion
    elif busqueda < titulo:
        return buscarAVL(raiz.izquierda, tituloBuscado)
    else:
        return buscarAVL(raiz.derecha, tituloBuscado)
