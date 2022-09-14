from abc import ABC


class Personajes(ABC):

    def __init__(self):
        self.__id = 0
        self.__nombre = None
        self.__vida = 0
        self.__liga = "Naga"

    def idf(self, id):
        self.__id = id

    def get_idf(self):
        return self.__id

    def nombref(self, nombre):
        self.__nombre = nombre

    def get_nombref(self):
        return self.__nombre

    def vidaf(self):
        self.__vida = 800

    def get_vidaf(self):
        return self.__vida

    def ligaf(self, liga):
        self.__liga = liga

    def get_ligaf(self):
        return self.__liga

    def __str__(self):
        print("Id : ", self.__id)
        print("Nombre : ", self.__nombre)
        print("Vida : ", self.__vida)
        print("Liga : ", self.__liga)


a = Personajes()
a.idf(0)
a.__str__()

