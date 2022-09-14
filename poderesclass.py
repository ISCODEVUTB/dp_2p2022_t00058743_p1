from caracterizacion import Caracterizacion


class Poderes(Caracterizacion):

    __super_velocidad: int
    __super_fuerza: int
    __volar: bool


    def __init__(self):
        self.__super_velocidad  = 0
        self.__super_fuerza = 0
        self.__volar = False

    def supervelocidad(self, velocidad):
        self.__super_velocidad = velocidad

    def get_supervelocidad(self):
        return self.__super_velocidad

    def superfuerza(self, fuerza):
        self.__super_fuerza = fuerza

    def get_superfuerza(self):
        return self.__super_fuerza

    def volarf(self, volar):
        self.__volar = volar

    def get_volarf(self):
        return self.__volar

    def __str__(self):
        if(self.__super_velocidad > 0 ):
            print(f"Tiene Super Velocidad \n Valor= {self.__super_velocidad}")
        else :
            print("No tiene Super Velocidad")
        if(self.__super_fuerza > 0 ):
            print(f"Tiene Super Fuerza\n Valor= {self.__super_fuerza}")
        else :
            print("No tiene Super Fuerza")
        if(self.__volar == 1):
            print("Puefe Volar")
        else :
            print("No Puede Volar")

p = Poderes()
p.supervelocidad(123)
p.__str__()