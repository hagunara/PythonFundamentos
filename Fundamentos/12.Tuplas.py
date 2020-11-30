#Mantiene el orden y conteniedo de los elementos. No se pueden modificar
frutas=("Kiwi", "Sandilla", "Pera")

#Muestra el primero
print(frutas[0])

#Mostrar solo los dos primeros
print(frutas[0:2])

#Ultimo elemto de la tupla
print(frutas[-1])

####CONVIERTE UNA TUPLA EN LISTA####
listaFrutas = list(frutas)
print(listaFrutas)

for i in listaFrutas:
    print(i)
    
for i in frutas:
    print(i, end=" ")# Este parametro para imprimir conseutivos funciona en listas y tuplas, es propiedad de print

#Al igual que las listas, las tuplas tambien se pueden eliminar
del frutas
print(frutas)

    

    
