class carro:
    def agregar_carro(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = False
        print(f"Se agregó el carro {self.marca} {self.modelo} de color {self.color}")


def encender(self):
    self.encendido = True
    print(f"El carro {self.marca} {self.modelo} ha encendido")

def apagar(self):
    self.encendido = False
    print(f"El carro {self.marca} {self.modelo} ha apagado")

 
carros = carro()
carros.agregar_carro("Toyota", "Camry", "Negro")

carros2 = carro()

carros2.agregar_carro("Honda", "Accord", "Blanco")