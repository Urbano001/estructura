class Restaurante:
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print(f"agregar restaurant...{self.nombre}")
    
    def mostrar_restaurantes(self):
        print(f"el nombre del restaurante es...{self.nombre}")

# Instanciar la clase
restaurante = Restaurante()
restaurante.agregar_restaurante("el pollo loco")
restaurante.mostrar_restaurantes()

#puedo crear diferentes objetos

restaurante2 = Restaurante()
restaurante2.agregar_restaurante("el hamburguesas rojas")
restaurante2.mostrar_restaurantes()

#imprimir los objetos
print(f'el nombre del restaurante es...{restaurante.nombre}')
print(f'el nombre del restaurante es...{restaurante2.nombre}')
#También puedo agregar funcionalidades más complejas a la clase Restaurante, como métodos para agregar y eliminar platos, etc.