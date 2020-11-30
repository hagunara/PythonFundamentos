def miFuncion():
    print("Mi primera funcion")

miFuncion()
miFuncion()

#Parametro: Variable definida entre los parentesis de una funcion 
#Argumento: (arg) Valor enviado a la funcion 

def funcionConArgumentos(nombre, apellido):
    print("El nombre recibido es: ",nombre," y el apellido es: ",apellido)
    
funcionConArgumentos("Juan","Campos")
funcionConArgumentos("Me","charlyy")

##Funciones con retorno
def suma(a,b):
    return a+b

print(suma(5,3))

##Funciones con retorno con valores de default
def multiplicacion(a=0,b=0):
    return a*b

print(multiplicacion(2,5))