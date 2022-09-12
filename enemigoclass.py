from inormal import Normal
from personajesclass import Personajes
from armasclass import Armas


class Enemigo(Personajes, Normal):

    def __ca_enemig(self, id, nombre, vida, liga):
        self.__id = 1904
        self.__nombre = "Enemigo"
        self.__vida = 800
        if (liga == "Azura"):
            self.__liga = "Naga"
        else:
            self.__liga = "Azura"
    armas = Armas()
    armas.arma_filof("Cuchillo")
    armas.__str__()