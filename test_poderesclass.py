import unittest

from poderesclass import Poderes


class Testpoderes(unittest.TestCase):

    def test_poderes(self):
        a = Poderes()

        velocidad = 1
        a.supervelocidad(velocidad)
        self.assertEqual(a.get_supervelocidad(), velocidad)

        fuerza = 1
        a.superfuerza(fuerza)
        self.assertEqual(a.get_supervelocidad(), fuerza)
        
        volar = 1
        a.volarf(volar)
        self.assertEqual(a.get_volarf(), volar)

if __name__ == '__main__':
    unittest.main()