#POLIMORFISMO
#ES LA CAPACIDAD DE UN OBJETO DE COMPORTARSE DE DIFERENTES MANERAS 
#VA A TENER DEFIRENTES COMPORTAMIENTO DE LA SITUACION


class restaurante:
    def __init__(self, nombre, categoria, precio ):
        print("Initialized")
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print(f"agregar restaurant...{self.nombre}")
    
    def mostrar_restaurantes(self):
        print(f"el nombre del restaurante es...{self.nombre} y su categoria es...{self.categoria}")
    
restaurant = restaurante("El pollo loco", "Comida casual", 50)

restaurant.mostrar_restaurantes()

#Herencia
class hotel(restaurante):
    def __init__(self, nombre, categoria, precio, num_habitaciones, piscina):
        super().__init__(nombre, categoria, precio) #con el Super() solo declarar los atributos de la clase padre
        self.num_habitaciones = num_habitaciones
        self.piscina = piscina #Almacenar como booleano

    def get_piscina(self):
        return self.piscina

#Reescribir el metodo mostrar_restaurantes y debe llamarse igual
    def mostrar_restaurantes(self):
      super().mostrar_restaurantes()
      print(f'Numero de habitaciones: {self.num_habitaciones}')
      print(f'Tiene piscina: {'Si' if self.piscina else 'No'}')

restaurant = restaurante("el pollo loco", "Comida casual", 50)
restaurant.mostrar_restaurantes()

hotel = hotel("El hotel del pollo loco", "5 estrella", 500, 100, True)

hotel.mostrar_restaurantes()
