# Abrir archivo 14.POO para ver detalles

class Persona():

    def __init__(self, nombre, edad, direccion):
        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion

    def descripcion(self):
        print("Nombre: ", self.nombre, " edad: " , self.edad, " Direccion: ", self.direccion)


class Empleado(Persona): # Herencia

    def __init__(self, salario, antiguedad, nombre, edad, direccion):
        super().__init__(nombre, edad, direccion)
        self.salario=salario
        self.antiguedad=antiguedad

    # Sobreescritura del método descripción definido en la clase padre:
    def descripcion(self):
        # Se llama el método descripción() del padre:
        super().descripcion()
        print(" Salario: ", self.salario, " Antiguedad: ", self.antiguedad)

# Creación de un objeto persona:

Manuel = Empleado(210, 55, "Manuel", 22, "Tulua")
Manuel.descripcion()



