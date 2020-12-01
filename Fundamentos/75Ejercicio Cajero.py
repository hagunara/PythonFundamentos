class Cajero:
    def __init__(self):
        self.__saldo=1000
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self,saldo):
        self.__saldo=saldo
    
funcion=True
cuenta=Cajero()
while funcion:
    print("Que desea hacer?:\n1.Ingresar Dinero:\n2.Retirar Dinero: \n3.Mostrar Saldo: \n4.Salir")
    opcion=int(input())
    if opcion==1:
        monto=int(input("Monto a ingresar: "))
        if monto>0:
            cuenta.setSaldo(int(cuenta.getSaldo())+monto)
        else:
            print("Monto Invalido")
    elif opcion==2:
        monto=int(input("Monto a retirar: "))
        if monto>0:
            if int(cuenta.getSaldo())-monto >= 0:
                cuenta.setSaldo(int(cuenta.getSaldo())-monto)
            else:
                print("Ud. No cuenta con saldo suficiente")
        else:
            print("Monto Invalido")  
        """
        #completar para que no retire mas dinero del que tiene perro
        if int(cuenta.getSaldo())-monto < 0:
            print("Ud. No cuenta con saldo suficiente")
            #next
        elif int(cuenta.getSaldo())-monto >= 0:
            cuenta.setSaldo(int(cuenta.getSaldo())-monto)
        """  
    elif opcion==3:
        print("Saldo en cuenta: "+ str(cuenta.getSaldo()))
    elif opcion==4:
        break
    else:
        print("Numero invalido")    
        