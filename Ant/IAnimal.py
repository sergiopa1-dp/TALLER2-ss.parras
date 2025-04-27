from abc import ABC, abstractmethod

class iAnimal(ABC):
    
    @abstractmethod
    def comer(self, Kilos_concentrado):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass

    @abstractmethod
    def continente_origen(self):
        pass

    @abstractmethod
    def emitir_sonido(self):
        pass