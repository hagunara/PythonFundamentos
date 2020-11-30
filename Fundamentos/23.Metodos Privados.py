class Persona:
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno):
        self.nombre=nombre
        self._apellidoPaterno = apellidoPaterno#Atributo parcialmente privado
        self.__apellidoMaterno = apellidoMaterno#Atributo completamente privado, es necesario crear get y set para editarno
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellidoPaterno)
        print(self.__apellidoMaterno)
    def metodoPublico(self):
        return self.__metodoPrivado()
    
    def getApellidoPaterno(self):
        return self._apellidoPaterno
    def setApellidoPaterno(self,apellidoPaterno):
        self._apellidoPaterno=apellidoPaterno
        
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
    def setApellidoMaterno(self,apellidoMaterno):
        
        
        
#Creando objeto
persona1=Persona("Pancracio","Muchos","Muchoss")

#No se pude acceder al metodo privado 
#persona1.__metodoPrivado()

persona1.metodoPublico()
