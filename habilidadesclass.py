from caracterizacion import Caracterizacion


class Habilidades(Caracterizacion):
    """
    __adaptacion_ambiental: bool
    __manejo_armas: bool
    """

    def __init__(self):
        self.__adaptacion_ambiental = False
        self.__manejo_armas = False

    def adaptacion_ambientalf(self, adaptacion):
        self.__adaptacion_ambiental = adaptacion

    def manejo_armasf(self, manejo):
        self.__manejo_armas = manejo

    def __str__(self) -> str:
        if (self.__adaptacion_ambiental):
            print("El personaje posee habilidad de Adaptacion Ambiental.")
        else:
            print("El personaje NO posee habilidad de Adaptacion Ambiental.")

        if (self.__manejo_armas):
            print("El personaje posee habilidad de Majeno de Armas.")
        else:
            print("El personaje NO posee habilidad de Majeno de Armas.")


"""
a = Habilidades()
a.adaptacion_ambientalf(False)
a.__str__()
"""
