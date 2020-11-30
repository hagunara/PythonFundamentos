class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre= nombre
    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        self.__edad=edad

        
#Objeto de clase
persona1=Persona("Juan",18)
persona2=Persona("Luna",18)

#Obtener elemento de objeto
print(persona1.getNombre())
print(persona1.getEdad())

#Modificar elementos de un objeto
persona1.setNombre("Juanita la del barrio")
persona1.setEdad(52)


print(persona1.getNombre())
print(persona1.getEdad())