class Empleado:
    def __init__(self):
        self.nombre="Federico"
        self.apellido=""
        self.edad=22
    def saludar(self):
        return "Hola me llamo " + self.nombre
    def saludar2(self):
        print("Hola me llamo " + self.nombre + " el saludar2")


emp = Empleado()
pepe = Empleado()
print(emp.saludar())
print(pepe.saludar2())
