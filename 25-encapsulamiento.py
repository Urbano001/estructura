class carro:
    def __init__(self, marca, modelo, color): #Este es un constructor de  la clase. es un 
        self._marca = marca #PROTECTED unicamente en esta clase 
        self.__modelo = modelo #PRIVATE solamente a travez de los metodos de la clase
        self.color = color #PUBLIC VIENE POR DEFECTO 
        self.encendido = False

#GETTERS Y SETTERS SON LOS METODOS QUE NOS PERMITEN ACCEDER (GET)
# Y MODIFICARV(SET)
# LOS ATRIBUTOS DE UN OBJETO DESDE FUERA DE LA CLASE

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca): #SETTER me permite modificar el valor de un atributo
        self.__marca = marca

    def encender(self):
        self.encendido = True
        print(f'El carro {self.__marca} {self.__modelo} ha encendido')

    def apagar(self):
        self.encendido = False
        print(f'El carro {self.__marca} {self.__modelo} ha apagado')

    def acelerar(self):
        if self.encendido:
            print(f'El carro {self.__marca} {self.__modelo} se acelera')
        else:
            print('El carro debe estar encendido para acelerar')
mi_carro = carro("Toyota","Corolla", "Blanco")
mi_carro.marca = "nissan"
mi_carro.set_marca("COROLA")

print(mi_carro.marca)

#Llamar a un metodo del objeto

mi_carro.encender()
mi_carro.acelerar()

    