from Ant.guarderia import Guarderia
from Ant.Boa import Boa_Constrictor
guarderia = Guarderia()
boa1 = Boa_Constrictor("Kaa", 15.0, 5, "Brazil", 100.0)
guarderia.set_boa(0, boa1)
result = guarderia.alimentar_boa(boa1)
print(result)  # Should print "Éxito"
