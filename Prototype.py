#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Estudiantes
#
# Created:     18/09/2019
# Copyright:   (c) Estudiantes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import copy
from Factory import *


class Prototype:
    _pers=None

    def clone(self):
        pass

class Prueba(Prototype):

    def __init__(self):
        self._pers=FactoryPrueba()

    def getPersonaje(self):
        return self._pers.getPersonaje()

    def clone(self):
        return copy.deepcopy(self)

class Mago(Prototype):

    def __init__(self):
        self._pers=FactoryMago()

    def getPersonaje(self):
        return self._pers.getPersonaje()

    def clone(self):
        return copy.deepcopy(self)

class Rottom(Prototype):

    def __init__(self):
        self._pers=FactoryRottom()

    def getPersonaje(self):
        return self._pers.getPersonaje()

    def clone(self):
        return copy.deepcopy(self)

class ObjectFactory:
    _Prueba = None
    _Rottom = None
    _Mago = None

    @staticmethod
    def initialize():
        ObjectFactory._Prueba=Prueba()
        ObjectFactory._Rottom=Rottom()
        ObjectFactory._Mago=Mago()

    @staticmethod
    def getPrueba():
        return ObjectFactory._Prueba.clone()

    @staticmethod
    def getMago():
        return ObjectFactory._Mago.clone()

    @staticmethod
    def getRottom():
        return ObjectFactory._Rottom.clone()


def main():
    ObjectFactory.initialize()
    p1 = ObjectFactory.getPrueba()
    p1.getPersonaje().getEscudo().setMaterial("Madera")
    r1 = ObjectFactory.getRottom()
    r1.getPersonaje().getEscudo().setMaterial("Hierro")
    print(p1.getPersonaje().getSprites())
    print(r1.getPersonaje().getSprites())
    pass

if __name__ == '__main__':
    main()