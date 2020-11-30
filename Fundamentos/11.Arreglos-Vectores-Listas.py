arreglo = ["Hola","como","estas","perro"]
print(arreglo)

#Longitud de Arreglo
print(len(arreglo)) 

#Indice de Arreglos
print(arreglo[0]) 

#Navegacion de arreglos inverso, el -1 indica el ultimo, en este caso seria "Perro"
print(arreglo[-1])
print(arreglo[-2])#Indica "Estas"

#Segmentos de Arreglo: Dando como parametros el inicio y el fin-1 del arreglo
print(arreglo[0:2])#"Hola" "Como" No incluye el indice final

#Segmento de arreglo de inicio a fin-1
print(arreglo[:3]) #Hola Como Estas

##############################################################
#Editar listas
arreglo[3] = "gato"
print(arreglo)

#Recorrer lista
for i in arreglo:
    print(i)

#Buscar en lista con IF
if "Gato" in arreglo:
    print("Encontramos ·gato· en el arreglo")
else:
    print("El elemento #gato# no se encontro el la lista")

#Agregar elemento al final del vector
arreglo.append("dime")
print(arreglo)

#Insertar objeto antes del indice indicado
arreglo.insert(0,"Coff Coff")
print(arreglo)

#Remueve un eleneto dentro de un arreglo, siempre en cuando este exista
arreglo.remove("Coff Coff")
print(arreglo)

#Remueve el ultimo elemento del arreglo
arreglo.pop()
print(arreglo)

#Rumueve el elemento indicado 
del arreglo[-1]
print(arreglo)

#Limpiar los elementos de nuestro array
arreglo.clear()
print(arreglo)

#Eliminar arreglo
del arreglo
#print(arreglo)

#Escribir un programa que permita al usuario ingresar 6 números enteros, 
# que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números
# negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa 
#arroje un error si no se ingresaron números positivos.
arreglo2=[]
negativos=0
positivos=0
cantidadPositivos=0
for i in range(6):
    arreglo2.append(int(input()))
    
for i in arreglo2:
    if i>0:
        cantidadPositivos+=1
        positivos+=i
    else:
        negativos+=i

if positivos==0:
    print("No se ingresaron numeros positivos")
else:
    print(negativos)
    print(positivos/cantidadPositivos)
            
        