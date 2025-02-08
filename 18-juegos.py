#EJERCICIO 2

pregunta = input('Agrega un numero y te dire se es impar\r\n')
pregunta += '\r\n escribe "cerrar" para salir de la app'
pregunta = True

while True:
    numero = input('Ingresa un numero o escriba la "cerrar" para salir')
    if numero.lower() == 'cerrar':
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else:
            print(f'El número {numero} es impar')
    except ValueError:
        print('Debes ingresar un número válido')
