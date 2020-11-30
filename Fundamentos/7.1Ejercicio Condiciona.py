#Ingresar dos numeros, decir si uno u otro es par, caso contrario
#Indicar que los dos son impares o pares si asi corresponde
class Pares:
    def __init__(self,numero1,numero2):
        self.__numero1=numero1
        self.__numero2=numero2
    def numeroPar(self):
        resultado=""
        if int(self.__numero1) % 2 == 0 and int(self.__numero2) % 2 == 0:
            resultado="Los dos numeros ingresados son Pares"
        elif int(self.__numero1) % 2 != 0 and int(self.__numero2) % 2 != 0:
            resultado="Los dos numeros son Impares"
        elif int(self.__numero1) % 2 == 0 and int(self.__numero2) % 2 != 0:
            resultado="El primer numero es Par, el segundo es impar"
        else:
            resultado="El primer numero es Impar, el segundo es par"
        return resultado
        
num1=int(input("Ingrese primer número: "))
num2=int(input("Ingrese segundo número: "))

comparacion=Pares(num1,num2)
print(comparacion.numeroPar())
