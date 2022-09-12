from caracterizacion import Caracterizacion
    # __frio: bool
    # __calor: bool
class Debilidades(Caracterizacion):
    def __init__(self):
        self.__frio = False
        self.__calor = False

    def friof(self, frio):
        self.__frio = frio

    def calorf(self, calor):
        self.__calor = calor

    def __str__(self) -> str:
        if(self.__frio):
            print("Debilidad : Calor")
        else:
            if(self.__calor):
                print("Debilidad : Frio")
            else:
                print("Debilidad: Frio, Calor")