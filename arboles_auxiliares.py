from cancion import *
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

#pude conseguir la mayoria de la informacion del powerpoint de la catedra, en caso de dudas
class MaxHeap:
    def __init__(self):
        self.heap = []

    def swapp(self, i, j): #intercambiamos los nodos del heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self, index): #Realiza el burbujeo hacia arriba para mantener la propiedad del MaxHeap.
      parent = (index - 1) // 2
      if index > 0 and self.heap[index]._calificacion > self.heap[parent]._calificacion:
        self.swapp(index, parent)
        self.sift_up(parent)

    def sift_down(self, index): #Realiza el burbujeo hacia abajo para mantener la propiedad del MaxHeap.
      left = 2 * index + 1
      right = 2 * index + 2
      largest = index # compara el hijo izquierdo con la calificacion
      if left < len(self.heap) and self.heap[left]._calificacion > self.heap[largest]._calificacion:
          largest = left
      if right < len(self.heap) and self.heap[right]._calificacion > self.heap[largest]._calificacion:
          largest = right
      if largest != index:
          self.swapp(index, largest)
          self.sift_down(largest)

    def insert(self, value): #Inserta un nuevo valor en el heap.
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def extract_max(self): #Extrae y devuelve el máximo valor del heap.
        if len(self.heap) == 0:
           return None
        if len(self.heap) == 1:
           return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return root

#mostrarlo costo un poco, pero hice una lista de la que sacar las canciones segun el total que haya
#y heap_mostrar conectado con maxheap, conectados con ranking. como ranking saca de biblioteca y heap_mostrar
#es = a ranking, maxheap() toma las canciones e inserta en listaheap, de la que se sacan las mejores calificadas
#(top 10, en este caso)
    def mostrar (self, total):
        listaheap = []
        heap_mostrar = MaxHeap()#muestra el heap, y como maxheap = mostrar y ranking, van a compartir esos datos
        for cancion in self.heap:
            heap_mostrar.insert(cancion)
        for i in range(total): #bucle por cada vuelta al total de canciones
            canciones = heap_mostrar.extract_max()
            if canciones != None:
                listaheap.append(canciones)
        return listaheap