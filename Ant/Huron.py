from Ant.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
     def __init__(self, nombre:str, peso:float, edad:int, pais_origen: str, impuestos:float) -> None:
          super().__init__(nombre, peso, edad, pais_origen, impuestos)

     def emitir_sonido(self):
          return "¡Eek Eek!"

     def continente_origen(self):
        print ("Europa")