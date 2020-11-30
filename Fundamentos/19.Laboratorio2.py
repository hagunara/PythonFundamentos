class Cubo:
    def __init__(self,largo,ancho,alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    def volumen(self):
        return self.alto * self.largo * self.ancho
#Ingresa los datos
largo = int(input("Ingrese el largo: "))
ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))

#Creacion de objeto
cubo1 = Cubo(largo,ancho, alto)

#Mostramos el objeto
print(cubo1.volumen())