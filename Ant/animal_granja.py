from Ant.IAnimal import iAnimal

class Animal_Granja(iAnimal):
        def __init__(self, nombre:str):
            self._nombre=nombre
            self._kilos_comidos=0
            self._continente_origen='Asia'
        def comer(self,kilos_concentrado):
              self._kilos_comidos=kilos_concentrado/2

        def continente_origen(self):
              return self._continente_origen