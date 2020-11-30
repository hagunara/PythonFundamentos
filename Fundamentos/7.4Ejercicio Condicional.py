class Aritmetica:
    def __init__(self,numero1,numero2):
        self.__numero1=numero1
        self.__numero2=numero2
    def sumar(self):
        suma=int(self.__numero1)+int(self.__numero2)
        return suma
    def resta(self):
        suma=int(self.__numero1)-int(self.__numero2)
        return suma
    def multiplicacion(self):
        suma=int(self.__numero1)*int(self.__numero2)
        return suma
    def division(self):
        suma=int(self.__numero1)/int(self.__numero2)
        return suma
    
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese segundo número: "))
operacion1=Aritmetica(num1,num2)
opcion=str(input("Ingrese:\n    S: Para Sumar \n    R: Para Restar\n    P ó M: Para Multiplicar\n    D: Para Dividir\n").lower())
if opcion=="s":
    print(operacion1.sumar())
elif opcion=="r":
    print(operacion1.resta())
elif opcion=="p" or opcion =="m":
    print(operacion1.multiplicacion())
elif opcion=="d":
    print(operacion1.division())
else:
    print("Ingresaste una opcion invalida")


