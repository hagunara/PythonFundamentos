#For Bucle

for num in range(0, 11, 2):#Inicio, Fin -1, paso en paso
    print(num)
    
for i in "Hola":
    print(i)
else:
    print("Fin del ciclo for")
    
#Cuantas letras a contiene una palabra si la palabra tiene una o terminar el ciclo
palabra="kehace"
cantidad=0
print("--------------")

for i in palabra:
    if i=="a":
        cantidad +=1
    elif i=="o":
        break
else:
    print("Se termino el conteo sin encontrar o")
        
print("Se obtenieron:", cantidad ," de letras a")

#Obtener lo numeros impares entre 0-5 con continue

for i in range(6):
     if i%2 != 0:
         continue
     else:
         print(i)
#Hacer el siguiente diagrama usando for

v="*"
#*
#**
#****
#*****
for i in range(4):
    print(v)
    v+="*"
#Hacer el siguiente diagrama usando for

v="*"
#   *   
#  ***  
# ***** 
#*******
for i in range(4):
   
