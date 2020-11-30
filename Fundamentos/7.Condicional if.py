#~Estructura

condicion=True

if condicion:
    print("La condicion resulto en True")
else:
    print("La condicion resulto en False")
    
#Abreviacion de IF

print("La condicion es verdadera") if condicion else print("La condicion es falsa")

#Uso de if con 3 posibles respuestas
#Ingrese un numero entre 1 y 3 , pase a letras
num=int(input("Ingrese un numero entre 1 y 3: "))

#Estructura de IF
if num==1:#Obligatoria para la estructura basica de if
    print("Uno")
elif num==2: #Opcional
    print("Dos")
elif num==3: #Opcional
    print("Tres")
else: #Opcional
    print("Numero fuera de rango")
    