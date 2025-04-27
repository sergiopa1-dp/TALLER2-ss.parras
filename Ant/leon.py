from Ant.animal import Animal

class Leon(Animal):
    def __init__(self, nombre:str,peso:float):
        super().__init__(nombre,None,peso)