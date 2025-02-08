playlist = {}
playlist['canciones'] = [] #Cree un diccionario


def menu():
 bucle = True
 while bucle:   
    print('1. Agregar playlist')
    print('2. Agregar una cancion')
    print('3. Eliminar una cancion')
    print('4. Mostrar Resumen')
    print('5. Salir')

    opcion = input('Elige una opcion:\n')
    if opcion == '1':
        app()
    elif opcion == '2':
        agregar_canciones()
    elif opcion == '3':
        eliminar_canciones()
    elif opcion == '4':
        mostrar_resumen()
    elif opcion == '5':
        print('Adiós!')
        bucle = False

    
def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar tu playlist:\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist 
            agregar_playlist = False  #Ya tienes un nombre desactivamos el true
            agregar_canciones()
            mostrar_resumen()


def agregar_canciones():
    print('Agregando canciones a la Playlist:', playlist['nombre'])
    while True:
        cancion = input('Ingresa el nombre de una canción (o presiona "X" para salir):\n')
        if cancion.lower() == 'x':

            break #Dejar de agregar canciones
        playlist['canciones'].append(cancion)

        print('Cancion agregada:', cancion)
    print('!Playlist completa')
    print(playlist)

def eliminar_canciones ():
    print('Eliminando canciones de la playlist:', playlist['nombre'])
    while True:
        cancion_eliminar = input('Ingresa el nombre de una canción a eliminar (o presiona "X" para salir):\n')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist['canciones']:
            playlist['canciones'].remove(cancion_eliminar)
            print('Cancion eliminada:', cancion_eliminar)
        else:
            print('No se encontro la canción:', cancion_eliminar)
    print('!Playlist Actualizada')
    print(playlist)

def mostrar_resumen():
    print(f'Resumen de la playlist:', playlist['nombre'])
    print('Canciones:', playlist['canciones'])
    print('Cantidad de canciones:', len(playlist['canciones']))
    for cancion in playlist['canciones']:
        print(cancion)
        
menu() #Inicia la app


    