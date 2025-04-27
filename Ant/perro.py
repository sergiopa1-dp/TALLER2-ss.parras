from Ant.animal import Animal
class  Perro(Animal):
    def __init__(self, nombre:str,raza:str,edad:int,peso:float):
        super().__init__(nombre,edad,peso)
        self.__raza=raza

    def get_raza(self):
        return self.__raza
    
    def emitir_sonido(self):
        return 'Guau guau!!'
    
    # def get_nombre(self):
    #     return  self.__nombre
    # def get_raza(self):
    #     return self.__raza
    # def get_edad(self):
    #     return self.__edad
    # def get_peso(self):
    #     return self.__peso