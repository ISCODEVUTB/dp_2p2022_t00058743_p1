from caracterizacion import Caracterizacion


class Debilidades(Caracterizacion):
    
    __frio: bool
    __calor: bool
    
    def __init__(self):
        self.__frio = False
        self.__calor = False

    def friof(self, frio):
        self.__frio = frio

    def get_friof(self):
        return self.__frio

    def calorf(self, calor):
        self.__calor = calor

    def get_calorf(self):
        return self.__calor

    def __str__(self) -> str:
        if (self.__frio):
            return "Debilidad : Calor"
        else:
            if (self.__calor):
                return "Debilidad : Frio"
            else:
                return "Debilidad: Frio, Calor"
