import unittest

from personalidadclass import Personalidad


class Testpersonalidad(unittest.TestCase):

    def test_personalidad(self):
        a = Personalidad()

        agresivo = True
        a.agresivof(agresivo)
        self.assertEqual(a.get_agresivof(), agresivo)
        
        hostil = True
        a.hostilf(hostil)
        self.assertEqual(a.get_hostilf(), hostil)

        if (a.get_agresivof() == True):
            self.assertEqual(a.__str__(), "Personaje Agresivo")
        else:
            if (a.get_hostilf() == True):
                self.assertEqual(a.__str__(), "Personaje Hostil")
            else:
                self.assertEqual(a.__str__(), "Personaje: Agresivo y Hostil")

if __name__ == '__main__':
    unittest.main()
