from Ant.animal import Animal
from Ant.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico,Animal):

     MAX_RATONES= 20
     def __init__(self, nombre:str, peso:float, edad:int, pais_origen: str, impuestos:float) -> None:
          super().__init__(nombre, peso, edad, pais_origen, impuestos)
          self._ratones_comidos = 0
     def sum_raton_comido(self) -> None:
        if self._ratones_comidos < self.MAX_RATONES:
            self._ratones_comidos += 1

     def emitir_sonido(self):
          return "¡Tsss!"

     def continente_origen(self):
        print("América")
     
     def get_ratones_comidos(self) -> int:
          return self._ratones_comidos
     
     def set_ratones_comidos(self, ratones) -> int:
          self._ratones_comidos = ratones

     def sum_raton_comido(self) -> int:
          self._ratones_comidos += 1