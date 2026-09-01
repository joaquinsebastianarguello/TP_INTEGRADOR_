# (1)Nombre del proyecto : Discoteca

## Dominio elegido y por qué.

Música.
Elegimos este dominio por que nos permite trabajar y programar de forma simple y comprensible las distintas entregas del trabajo práctico, sumado al interés que tenemos en el grupo sobre los distintos gustos y géneros, los cuales pueden ser reflejados mediante el uso de listas, el uso de funciones de pila o cola para representar cómo se añaden datos a las playlists, o métodos de ordenamiento para las recomendaciones de géneros y artistas.

## (2)Problema que resolver.

El proyecto resuelve un problema de organización a través de listas de reproducción, sumado a la búsqueda,descubrimiento de géneros o canciones que podrían ser de interés para el usuario.

## (3)Usuario objetivo.

Luis, un profesor de música, busca exponer a sus alumnos a distintos géneros musicales, permitir la colaboración de los mismos en cuanto a canciones y álbumes en los que quieran trabajar y encontrar más canciones que se adecuen a sus gustos respectivamente.

## (4)Cinco funcionalidades iniciales.

F1- Buscar canciones
F2- crear playlists
F3- añadir/borrar canciones de las playlists
F4- mostrar información de una canción
F5- recomendar canciones/artistas del mismo género

## (5) Un ejemplo de interacción.

```text
___________
Discoteca
___________
1-buscador
2-biblioteca
3-crear playlist
4-recomendaciones
5-salir
___________
[!] SELECCIONE UNA OPCIÓN: 1

[!] Ingrese el nombre de la canción: Fanky

resultado:

[1] Fanky (Charly Garcia)
[2] …
[3] …

[!] Seleccione una canción/Álbum: 1

______________
[Fanky]
__________
artista: Charly Garcia
album: “Como Conseguir Chicas”
género: Rock
__________
Canciones similares:

[A], por (artista)
[B], por (artista)
[C], por (artista)

1- Volver atrás
2- Volver al menú inicial
3- Añadir a la playlist
4- Explorar recomendados
__________

## (6) Requerimientos
RF1: El sistema debe permitir la búsqueda de canciones, álbumes, artistas o géneros.

RF2: El sistema debe permitir la creación de playlists personalizadas por el usuario.

RF3: Del mismo modo, el sistema debe permitir la eliminación o incorporación de elementos a la playlist.

RF4: El sistema debe mostrar los datos relacionados a una canción, álbum, o artista.

RNF: El sistema debe devolver resultados en tiempos óptimos acerca de grandes listas de datos.
