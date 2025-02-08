playlist ={}

def crear_playlist():
    nombre_playlist = input("como deseas nombrar tu playlist")
    playlist[nombre_playlist] = []
    return nombre_playlist

def agregar_cancion(playlist_nombre):
    print('Agregando canciones a la playlist: ', playlist_nombre)
    while True:
        cancion = input('ingresa el nombre de la cancion o "salir" para terminar: ')
        if cancion.lower() == 'salir':
            break
        playlist[playlist_nombre].append(cancion)
        print('cancion agregada exitosamente!',cancion)

def eliminar_cancion(playlist_nombre):
    print('Eliminando canciones de la playlist: ', playlist_nombre)
    cancion_eliminar = input('ingresa el nombre de la cancion que deseas eliminar: ')
    if cancion_eliminar in playlist[playlist_nombre]:
        playlist[playlist_nombre].remove(cancion_eliminar)
        print('cancion eliminada exitosamente!', cancion_eliminar)
    else:
        print('cancion no encontrada en la playlist')

def mostrar_playlist(playlist_nombre):
   if not playlist:
        print('La playlist esta vacia')
    else:
        for nombre_playlist, canciones in playlist.items():
            print(f"Playlist: {nombre_playlist}")
            for cancion in canciones:
                print(f"-{cancion}") 

def main():
    while True:
        print('\n1. Crear playlist')
        print('2. Agregar canciones a playlist')
        print('3. Eliminar canciones de playlist')
        print('4. Mostrar playlist')
        print('5. Salir')
        opcion = input('Escoja una opcion: ')
        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_cancion(playlist_nombre)
        elif opcion == '2':
            playlist_nombre = input('ingrese el nombre de la playlist: ')
            if playlist_nombre in playlist 
            agregar_cancion(nombre_playlist)
        else:
            print('La playlist no existe')
        elif opcion == '3':
            nombre_playlist = input('ingrese el nombre de la playlist: ')
            if nombre_playlist in playlist:
            eliminar_cancion(nombre_playlist)
        else:
            mostrar_playlist(nombre_playlist)
            break
        elif opcion == '5':
            break
        else:
            print('opcion invalida')            

main()