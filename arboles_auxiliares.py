
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

class nodo_arbol_general:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []# reemplaza izquierda derecha
        self.canciones = []# lista de canciones de esta categoría

def insertarCategoria(raiz, nombre_categoria):#busca si ya existe la categoría hija, o la crea y la devuelve
    for hijo in raiz.hijos:
        if hijo.nombre.lower().strip() == nombre_categoria.lower().strip():
            return hijo
    nuevo_nodo = nodo_arbol_general(nombre_categoria)#si no hay hijos
    raiz.hijos.append(nuevo_nodo)
    return nuevo_nodo

def agregarCancionPorGenero(raiz, cancion): # Clasifica la canción según su género en el árbol general
    canciones_genero = cancion._genero.lower().strip()
    #me gusto como salio esta parte, asi que la voy a explicar
    #para no tener que meter genero por genero en el arbol general, tenia que pensar como implementar la jerarquia
    #al principio pense en numeros o rating, pero creo que la mejor forma es seleccionar una categoria particular
    #y elegir palabras claves que buscar, asi heredan del padre (rock > rock pesado > rock nacional)
    if "rock" in canciones_genero:#vamos a buscar por cada cancion estas palabras claves, y usamos la funcion anterior
        categoria_rock = insertarCategoria(raiz, "ROCK")
        if "español" in canciones_genero:
            subcategoria = insertarCategoria(categoria_rock, "ROCK ESPAÑOL")
        else:
            subcategoria = insertarCategoria(categoria_rock, "ROCK INTERNACIONAL")
        subcategoria.canciones.append(cancion)
    elif "pop" in canciones_genero or "synthpop" in canciones_genero:
        categoria_pop = insertarCategoria(raiz, "POP")
        subcategoria = insertarCategoria(categoria_pop, "POP Y SYNTHPOP")
        subcategoria.canciones.append(cancion)
    else:
        categoria_otros = insertarCategoria(raiz, "OTROS GENEROS")
        categoria_otros.canciones.append(cancion)

def mostrarArbolGeneral(raiz, nivel=0):#recorrido recursivopara mostrar la jerarquía
    espacio = "     " * nivel
    print(espacio + ">" + raiz.nombre)
    for cancion in raiz.canciones:
        print(espacio + ">" + str(cancion))
    for hijo in raiz.hijos:#recorre recursivamente a los hijos
        mostrarArbolGeneral(hijo, nivel + 1)
        #este formato lo saque de un video, para que quede mas prolijo a la hora de presentar y se parezca mas a lo propuesto en el tp