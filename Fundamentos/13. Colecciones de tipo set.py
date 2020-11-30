#Set, Son arreglos sin orden, sin elementos reptidos, no se pueden modificar individualmente,
#pero si se pueden agregar o eliminar elementos que lo constituyen

planetas = {"Mercurio", "Venus", "Earth","Mars"}
print(planetas)

#Longitud de set
print(len(planetas))

#Revisar si un elemento esta en un set devuelve false o true
print("Tierra" in planetas)

#Agregar un elemento al set
planetas.add("Jupiter")#NO SE PUEDEN AGREGAR ELEMENTOS REPETIDOS
print(planetas)

#Eliminar con remove, elimina el elemento, pero devuelve una exepcion SI NO SE ENCUENTRA EL ELEMENTO
planetas.remove("Jupiter")

#Eliminar elemento de set sin exepcion
planetas.discard("Jupiter")

#Eliminar todos los ELEMENTOS del set
planetas.clear()

#Elimina el SET como variable
del planetas

