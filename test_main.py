import unittest

from armasclass import Armas
from artificialclass import Artificial
from debilidadesclass import Debilidades
from enemigoclass import Enemigo
from humanoclass import Humano
from ianormal import Anormal
from inormal import Normal
from personajesclass import Personajes
from habilidadesclass import Habilidades
from personajesclass import Personajes
from personalidadclass import Personalidad
from poderesclass import Poderes

class Testmain(unittest.TestCase):

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

    def test_habilidades(self):
        a = Habilidades()

        manejo_armas = True
        a.manejo_armasf(manejo_armas)
        self.assertEqual(a.get_manejo_armasf(), True)
        
        adaptacion_ambiental = True
        a.adaptacion_ambientalf(adaptacion_ambiental)
        self.assertEqual(a.get_adaptacion_ambientalf(), True)
        #self.assertTrue(a.get_manejo_armasf())

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

    def test_poderes(self):
        a = Poderes()

        velocidad = 1
        a.supervelocidad(velocidad)
        self.assertEqual(a.get_supervelocidad(), velocidad)

        fuerza = 1
        a.superfuerza(fuerza)
        self.assertEqual(a.get_supervelocidad(), fuerza)
        q= Normal()
        x = Anormal()
        r = Humano()
        h = Artificial()
        volar = 1
        a.volarf(volar)
        self.assertEqual(a.get_volarf(), volar)

        


if __name__ == '__main__':
    unittest.main()