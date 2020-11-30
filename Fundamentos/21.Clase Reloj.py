class Reloj:
    def __init__(self,hora,minuto,segundo,formato):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.formato = formato# 0 para 24H -  1 para 12H
    def resetHora(self):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
        self.formato=0
        return "La hora se a reiniciado"
    def mostrarHora(self):
        if self.formato==0:
            self.formato="PM"
        else:
            self.formato="AM"
        return str(self.hora)+" : "+str(self.minuto)+" : "+str(self.segundo)+" - "+str(self.formato)
         
    def convertirPM(self):
        if self.hora > 12:
            self.hora -= 12
    #def convertirAM(self):
     #   if        
print("Ingrese formato de hora para ingresar: \n 1.24H \n 2.12H")

formato= int(input("Ingrese el formato de hora"))
hora = int(input("Ingrese el hora: "))
minuto = int(input("Ingrese el minuto: "))
segundo = int(input("Ingrese el segundo: "))

#Crear objeto
hora1=Reloj(hora,minuto,segundo)
print(hora1.mostrarHora())
print(hora1.convertirPM())
#print(hora1.resetHora())
print(hora1.mostrarHora())