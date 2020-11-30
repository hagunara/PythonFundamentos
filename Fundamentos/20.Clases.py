class Persona:
    def __init__(self,nombre, edad):#Estos son los parametros que te mencionará el IDE
        self.nombre = nombre
        self.edad = edad
    def imprimirDatosObjeto(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        
#Creamos el objeto

persona1=Persona("Juanito",18)

#Imprimir Objeto
print(persona1.imprimirDatosObjeto())