from caracterizacion import Caracterizacion


class Personalidad(Caracterizacion):
    """
    __agresivo: bool
    __hostil: bool
    """

    def __init__(self):
        self.__agresivo = False
        self.__hostil = False

    def agresivof(self, agresivo):
        self.__agresivo = agresivo

    def hostilf(self, hostil):
        self.__hostil = hostil

    def __str__(self) -> str:
        if(self.__agresivo):
            print("Personaje Agresivo")
        else:
            if(self.__hostil):
                print("Personaje Hostil")
            else:
                print("Personaje: Agresivo y Hostil")
