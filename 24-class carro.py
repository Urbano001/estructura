class carro:
    def agregar_carro(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = False
        print(f"Se agregó el carro {self.marca} {self.modelo} de color {self.color}")

#es una convencion en python .self representa la instancia del obejto que se esta creando
def encender(self):
    self.encendido = True
    print(f"El carro {self.marca} {self.modelo} ha encendido")

def apagar(self):
    self.encendido = False
    print(f"El carro {self.marca} {self.modelo} ha apagado")

def acelerar(self):
    if self.encendido:
        print(f"El carro {self.marca} {self.modelo} se acelera")
    else:
        print("El carro debe estar encendido para acelerar")

 #cremos un objeto (instancia)
carros = carro()
carros.agregar_carro("Toyota", "Camry", "Negro")

carros2 = carro()

carros2.agregar_carro("Honda", "Accord", "Blanco")

#acceder a los atributos del objeto
print(carro.marca) #imprime Toyota

#llamar a un metodo del objeto

carros.encender()
carros.acelerar()