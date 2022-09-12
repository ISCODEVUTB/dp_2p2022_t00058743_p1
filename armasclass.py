from caracterizacion import Caracterizacion


class Armas(Caracterizacion):

    def __init__(self):
        self.__arma_filo = ""
        self.__arma_fuego = ""
        self.__otro = ""

    def arma_filof(self, arma_filo):
        self.__arma_filo = arma_filo

    def arma_fuegof(self, arma_fuego):
        self.__arma_fuego = arma_fuego

    def otrof(self, otro):
        self.__otro = otro

    def __str__(self) -> str:
        print("Arma de filo : ", self.__arma_filo)
        print("Arma de fuego : ", self.__arma_fuego)
        print("Otro tipo de arma : ", self.__otro)
# a = Armas()
# a.__str__()
