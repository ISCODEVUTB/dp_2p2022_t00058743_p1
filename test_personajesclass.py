import unittest

from personajesclass import Personajes


class Testanormal(unittest.TestCase):

    def test_anormal(self):
        a = Personajes()
        id = 0
        nombre = ""
        liga = "Azura"

        a.idf(id)
        self.assertEqual(a.get_idf(), id)
        
        a.nombref(nombre)
        self.assertEqual(a.get_nombref(), nombre)
        
        a.vidaf()
        self.assertEqual(a.get_vidaf(), 800)

        a.ligaf(liga)
        self.assertEqual(a.get_ligaf(), liga)

if __name__ == '__main__':
    unittest.main()
