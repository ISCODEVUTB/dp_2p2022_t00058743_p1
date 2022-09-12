from abc import ABC


class Personajes(ABC):

    def __init__(self):
        self.__id = 0
        self.__nombre = None
        self.__vida = 0
        self.__liga = 0

    def idf(self, id):
        self.__id = id

    def nombref(self, nombre):
        self.__nombre = nombre

    def vidaf(self):
        self.__vida = 800

    def ligaf(self, liga):
        self.__liga = liga

    def __str__(self):
        print("Id : ", self.__id)
        print("Nombre : ", self.__nombre)
        print("Vida : ", self.__vida)
        print("Liga : ", self.__liga)


a = Personajes()
a.idf(12334)
a.__str__()
