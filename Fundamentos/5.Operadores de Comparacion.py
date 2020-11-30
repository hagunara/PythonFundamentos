a=3
b=2

resultado = (a==b) #Operador de Comparacion

print(resultado)

resultado = a != b #Operador de Diferente

print(resultado)

resultado = a>b #Operador de Mayor que
#Menor que       -- <
#Mayor igual que -- >=
#Menor igual que -- <=
print(resultado)

#Es un numero par la variable a?

if(a%2==0):
    print("Es par")
else:
    print("No es par")

#Es mayor de edad una persona, haga un programa que pida un numero

edad=int(input("Ingrese edad"))

if edad>17:
    print("Es mayor de edad")
else:
    print("Es menor de edad")