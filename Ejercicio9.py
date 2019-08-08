class Empleado:
    def __init__(self):
        self.codigo=""
        self.nombre=""
        self.apellido=""
        self.salarioBase=""


    def retencion(self):
        total=(self.salarioBase*0.1)
        return total

    def nombreCompleto(self):
        completo=(self.nombre)+" "+(self.apellido)
        return completo


    def salarioNeto(self):
        if((self.salarioBase)-(self.salarioBase*0.1))<=828116:
            return ((self.salarioBase)-(self.salarioBase*0.1))+97032
        else:
            return ((self.salarioBase)-(self.salarioBase*0.1))


emp=Empleado()
Codigo = input ("Ingrese su codigo: ") 
Nombre = input("Ingrese su nombre: ")
Apellido = input ("Ingrese su apellido: ")
salarioBase = float(input("Ingrese su salario: "))

emp.Codigo=Codigo
emp.nombre=Nombre
emp.apellido=Apellido
emp.salarioBase=salarioBase

print(emp.retencion())
print(emp.salarioNeto())
print(emp.nombreCompleto())


