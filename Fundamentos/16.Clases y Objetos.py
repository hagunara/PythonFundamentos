class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
#Creacion de Objetos a partir de la clase creada mandandlo los atrivutos correspondientes

persona1=Persona("Esteban",20)

persona2= Persona("Karla",21)

#Consultamos los atrivutos guardados en los objetos

print(persona1.nombre)
print(persona1.edad)

print(persona2.nombre)
print(persona2.edad)

#Cada objeto es indendiente en memoria, por lo sea crean por separado
print(id(persona1))
print(id(persona2))