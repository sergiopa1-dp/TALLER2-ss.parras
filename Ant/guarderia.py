from Ant.perro import Perro
from Ant.gato import Gato
# from hamster import Hamster
from Ant.animal import Animal
from Ant.leon import Leon
from Ant.animal_exotico import Animal_Exotico
from Ant.Boa import Boa_Constrictor
from Ant.Huron import Huron
perro1=Perro("Zeus","Rottweiler",3,45.8)
perro1=Perro("Nala","Golder R",1,8.5)

# gatito1=Gato()
# nuevo_hamster=Hamster()
# print(nuevo_hamster.nombre)

gatito1=Gato('Destructor de Mundos','Naranja',5,4)
gatito2=Gato('Gato','Negro',5,4)

print(gatito1.get_nombre())
print(gatito2.get_nombre())
print(perro1.get_nombre())

print(isinstance(perro1,Perro))
print(isinstance(perro1,Animal))



 
perro1.emitir_sonido()
gatito1.emitir_sonido()

boa = Boa_Constrictor("Boa", 25.0, 10, "USD", 400.00)
boa.emitir_sonido()
print(f"Boa: {boa.get_nombre()}, Ratones comidos: {boa.get_ratones_comidos()}, Sonido: {boa.emitir_sonido()},Pais:{boa.get_pais_origen()}, Flete:{boa.calcular_flete()}")


huron = Huron("Huroncito", 10.0, 2, "España", 500.0)
print(f"Hurón: {huron.get_nombre()}, Sonido: {huron.emitir_sonido()}, Pais:{huron.get_pais_origen()},Flete:{huron.calcular_flete()}")



class Guarderia:
    def __init__(self):
        self.boas = [None, None]
        self.hurones = [None, None]
    
    def set_boa(self, index: int, boa: Boa_Constrictor):
        if 0 <= index < 2:
            self.boas[index] = boa
    
    def set_huron(self, index: int, huron: Huron):
        if 0 <= index < 2:
            self.hurones[index] = huron
    
    def alimentar_boa(self, boa: Boa_Constrictor) -> str:
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.sum_raton_comido()
            return "Éxito"
        except ValueError:
            return "La boa está llena"