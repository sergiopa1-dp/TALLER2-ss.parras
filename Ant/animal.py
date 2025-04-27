from Ant.IAnimal import iAnimal
from abc import abstractmethod
class Animal(iAnimal):
    
    def __init__(self, nombre:str,edad:int,peso:float):
        self._nombre=nombre
        self._edad=edad
        self._peso=peso
        self._kilos_comidos=0
        
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_edad(self) -> int:
        return self._edad
    
    def get_peso(self) -> float:
        return self._peso
        
    
    def  set_nombre(self, nombre: str) -> None:
         self._nombre = nombre

    def set_edad(self, edad: int) -> None:
          self._edad = edad

    def set_peso(self, peso: float) -> None:
          self._peso = peso
    
    def comer(self,kilos_concentrado):
        self._kilos_comidos=+kilos_concentrado
    
    def obtener_kilos_comidos(self):
        return self._kilos_comidos
    
    def continente_origen(self):
        return 'Animal domestico sin origen'
    

    @abstractmethod
    def emitir_sonido(self):
        pass