import unittest
from Ant.Boa import Boa_Constrictor
from Ant.Huron import Huron

class TestBoa(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Kaa", 15.0, 5, "Brazil", 100.0)
    
    def test_emitir_sonido(self):
        self.assertEqual(self.boa.emitir_sonido(), "¡Tsss!")
    
    def test_calcular_flete(self):
        expected_flete = 15.0 * 100.0  # peso * impuestos
        self.assertEqual(self.boa.calcular_flete(), expected_flete)
    
    def test_alimentar(self):
        initial_ratones = self.boa.get_ratones_comidos()
        self.boa.sum_raton_comido()
        self.assertEqual(self.boa.get_ratones_comidos(), initial_ratones + 1)

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Whiskers", 2.0, 3, "France", 50.0)
    
    def test_emitir_sonido(self):
        self.assertEqual(self.huron.emitir_sonido(), "¡Eek Eek!")
    
    def test_calcular_flete(self):
        expected_flete = 2.0 * 50.0  # peso * impuestos
        self.assertEqual(self.huron.calcular_flete(), expected_flete)

if __name__ == '__main__':
    unittest.main()