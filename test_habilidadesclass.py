import unittest

from habilidadesclass import Habilidades

class Testhabilidades(unittest.TestCase):

    def test_habilidades(self):
        a = Habilidades()

        manejo_armas = True
        a.manejo_armasf(manejo_armas)
        self.assertEqual(a.get_manejo_armasf(), True)
        
        adaptacion_ambiental = True
        a.adaptacion_ambientalf(adaptacion_ambiental)
        self.assertEqual(a.get_adaptacion_ambientalf(), True)
        #self.assertTrue(a.get_manejo_armasf())

if __name__ == '__main__':
    unittest.main()