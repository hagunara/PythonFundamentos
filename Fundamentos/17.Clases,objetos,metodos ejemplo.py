class Aritmetica:
    def __init__(self,operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def suma (self):
        return self.operando1 + self.operando2
    
#Creamos un nuevo objeto

objetoSuma=Aritmetica(5,5)

#Consultamos objeto creado

print(objetoSuma.suma())    