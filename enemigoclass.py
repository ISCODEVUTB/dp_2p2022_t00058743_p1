from inormal import Normal
from personajesclass import Personajes
from armasclass import Armas


class Enemigo(Personajes, Normal):
    def __init__(self):
        self.__id = 1904
        self.__nombre = "Enemigo"
        self.__vida = 800

    def ca_enemig(self, liga):

        if (liga == "Azura"):
            self.__liga = "Naga"
        else :
            if (liga == "Naga"):
                self.__liga = "Azura"
        
    def get_liga(self):
        return self.__liga

    def __str__(self):
        return self.__id, self.__nombre, self.__vida, self.__liga

    armas = Armas()
    armas.arma_filof("Cuchillo")
    armas.__str__()

a = Personajes()
liga = a.get_ligaf()

enemigo = Enemigo()
enemigo.ca_enemig(liga)
print(enemigo.__str__())

