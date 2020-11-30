#Salida de texto

print ("Hola")
#############
#Variables

x = 3#Variable numerica
y = 5
z = x+y
print(z)

#Tipos de Variables

type(x)# Sirve para ver el tipo de variable en consola
a = 5.1 #Tipo Float
b = 5 #Tipo Int
c = "Esta es una cadena" #String

print (c+" asi se agregan cadenas") #Concatenar SOLO CADENAS
print (c+" ", x, y) #Concatenar cadenas con variables numéricas
print(c + str(x+y)) #Aquí convertimos las variables numericas a String con str

#Valores Booleanos

e=True
f=False

valor=x>y#Esta comparacion dara como resultado un valor booleano

if(x>y):
    print(x," es mayor")
else:
    print(y," es mayor")





