#Uso esto porque no me dejaba importar lo de arboles auxiliares por estar en otra carpeta
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from arbol_avl import insertarAVL, buscarAVL
from arboles_auxiliares import insertarNodo, buscarNodo

class CancionPrueba:
    def __init__(self, titulo):
        self._titulo = titulo


titulos = [
    "Back in Black",
    "Beat It",
    "Crimen",
    "Demonio",
    "Despacito",
    "Flaca",
    "Havana",
    "Hotel California",
    "Imagine",
    "Matador"
]

raiz_avl = None
raiz_bst = None

for titulo in titulos:
    cancion = CancionPrueba(titulo)

    raiz_avl = insertarAVL(raiz_avl, cancion)
    raiz_bst = insertarNodo(raiz_bst, cancion)
titulos_buscar = ["Flaca", "Despacito"]

def altura(raiz):
    if raiz is None:
        return 0

    return 1 + max(
        altura(raiz.izquierda),
        altura(raiz.derecha)
    )

print(" COMPARACION DE LOS ÁRBOLES ")
print("Cantidad de canciones:", len(titulos))
print("Altura del BST:", altura(raiz_bst))
print("Altura del AVL:", altura(raiz_avl))


for titulo in titulos_buscar:
    resultado = buscarAVL(raiz_avl, titulo)

    if resultado is not None:
        print("Cancion encontrada:", resultado._titulo)
    else:
        print("Cancion no encontrada:", titulo)
