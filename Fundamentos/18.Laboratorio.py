class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
#Creando objeto
print("Ingrese los valores correspondientes a base y altura")
rectangulo1 = Rectangulo(int(input()),int(input()))

#Devolviendo Area
print(rectangulo1.area())