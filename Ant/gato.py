from Ant.animal import Animal
class Gato(Animal):
    def __init__(self, nombre:str,color:str,edad:int,peso:float):
        super().__init__(nombre,edad,peso)
        self.__color=color
    
    def get_color(self):
        return self.__color
    
    def emitir_sonido(self):
        return 'Miau miau!!'