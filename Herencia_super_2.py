"""
Tomado de Orden de Resolución de Métodos (MRO):
    https://python-para-impacientes.blogspot.com/2015/06/programacion-orientada-objetos-y-iii.html
"""

class Clase_A(object):
    def metodo1(self):
        print("Clase_A.metodo1()")
        
    def metodo3(self):
        print("Clase_A.metodo3()")
        
    def metodo4(self):
        print("Clase_A.metodo4()")

class Clase_A1(Clase_A):
    def metodo1(self):
        print("Clase_A1.metodo1()")

    def metodo2(self):
        print("Clase_A1.metodo2()")

class Clase_A2(Clase_A):
    def metodo1(self):
        print("Clase_A2.metodo1()")

    def metodo3(self):
        print("Clase_A2.metodo3()")

class Clase_X(Clase_A1, Clase_A2):
    def metodo1(self):
        print("Clase_X.metodo1()")

objeto1 = Clase_X()  # Creación de una instancia (objeto) de Clase_X
objeto1.metodo1()  # Clase_X.metodo1()
objeto1.metodo2()  # Clase_A1.metodo2()
objeto1.metodo3()  # Clase_A2.metodo3()
objeto1.metodo4()  # Clase_A.metodo4()