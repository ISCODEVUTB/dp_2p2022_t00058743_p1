import unittest

from debilidadesclass import Debilidades


class Testdebilidades(unittest.TestCase):

    def test_debilidades(self):
        a = Debilidades()

        frio=False
        a.friof(frio)
        self.assertEqual(a.get_friof(), frio)

        calor=False
        a.calorf(calor)
        self.assertEqual(a.get_calorf(), calor)

        if (frio):
            self.assertEqual(a.__str__(), "Debilidad : Calor")
        else:
            if (calor):
                self.assertEqual(a.__str__(), "Debilidad : Frio")
            else:
                self.assertEqual(a.__str__(), "Debilidad: Frio, Calor")

if __name__ == '__main__':
    unittest.main()