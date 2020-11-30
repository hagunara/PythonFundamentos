class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return "Nombre: "+self.nombre+"\n"+"Edad: "+str(self.edad)
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)#estend aqui importamos los valores de la clase padre
        self.sueldo=sueldo
    def __str__(self):
        return super().__str__() +"\nSueldo: S./"+str(self.sueldo)
#Creando Objeto 
persona1=Persona("Alberto", 18)
empleado1=Empleado("Juanito",19,500.00)

#Consultando Cadena
print(empleado1)

    
        