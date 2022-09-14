import unittest

from enemigoclass import Enemigo
from personajesclass import Personajes


class Testenemigo(unittest.TestCase):

    def test_ca_enemigo(self):
        a = Enemigo()
        b = Personajes()
        liga = b.get_ligaf()

        a.ca_enemig(liga)

        if (liga == "Azura"):
            self.assertEqual(a.get_liga(), "Naga")
        else :
            if (liga == "Naga"):
                self.assertEqual(a.get_liga(), "Azura")

if __name__ == '__main__':
    unittest.main()
