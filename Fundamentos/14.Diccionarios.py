#Diccionario una especie de arreglo que almacena (key:Value)
diccionario = {
    "IDE":"Integrated Development Environmet",
    "OOP":"Objet Oriented Programing",
    "DBMS": "Data Base Managment System"
}

print(diccionario)  

#Largo de un diccionario
print(len(diccionario))

#Consultar un elemento
print(diccionario["IDE"])
print(diccionario.get("IDE"))

#Modificar valor de diccionario
diccionario["IDE"]="Integrated development environmet"
print(diccionario)

#Recorrer diccionario / solo llaves / keys
for i in diccionario:
    print(i)

#Recorrer diccionario / solo significados / values
for i in diccionario:
    print(diccionario[i])
    
#Consultar existencia de key en diccionario
print("IDE" in diccionario)

#Agregar elemento en diccionario
diccionario["PK"]="Primary Key"
print(diccionario)

#Eliminar elemento de diccionario
diccionario.pop("PK")
print(diccionario)

#Limpiar diccionario
diccionario.clear()
print(diccionario)

#Eliminar Variable de diccionario
del diccionario
print (diccionario)
    
