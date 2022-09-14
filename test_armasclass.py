import unittest

from armasclass import Armas

class Testhabilidades(unittest.TestCase):

    def test_armas(self):
        a = Armas()

        arma_filo="Cuchillo"
        a.arma_filof(arma_filo)
        self.assertEqual(a.get_arma_filof(), "Cuchillo")

        arma_fuego="Pistola"
        a.arma_fuegof(arma_fuego)
        self.assertEqual(a.get_arma_fuegof(), "Pistola")

        otro="Pistola Sable"
        a.otrof(otro)
        self.assertEqual(a.get_otrof(), "Pistola Sable")

if __name__ == '__main__':
    unittest.main()