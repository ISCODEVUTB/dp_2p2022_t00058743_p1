from caracterizacion import Caracterizacion


class Personalidad(Caracterizacion):

    __agresivo: bool
    __hostil: bool

    def __init__(self):
        self.__agresivo = False
        self.__hostil = False

    def agresivof(self, agresivo):
        self.__agresivo = agresivo

    def get_agresivof(self):
        return self.__agresivo

    def hostilf(self, hostil):
        self.__hostil = hostil

    def get_hostilf(self):
        return self.__hostil

    def __str__(self) -> str:
        if (self.__agresivo):
            return "Personaje Agresivo"
        else:
            if (self.__hostil):
                return "Personaje Hostil"
            else:
                return "Personaje: Agresivo y Hostil"
