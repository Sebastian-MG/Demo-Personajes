#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      lenovo
#
# Created:     06/10/2019
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from Builder import *
from ClasesJuego import *


class AbstractFactory:
    _personaje = None

    def getPersonaje(self):
        return self._personaje

    def crearSprite(self):
        pass

    def crearSonido(self):
        pass

class FactoryPrueba(AbstractFactory):

    def __init__(self):
        self._personaje=Personaje()
        self._personaje.setTipo("Prueba")
        self._personaje.setSprites(self.crearSprite())
        self._personaje.setRuido(self.crearSonido())

    def crearSprite(self):
        buld=BuildSprtPersonaje(self._personaje.getTipo())
        buld.BuildPlano()
        buld.BuildSprite()
        return buld.getSprites()

    def crearSonido(self):
        buld=BuildRdoPersonaje(self._personaje.getTipo())
        buld.BuildSonido()
        return buld.getSonidos()

class FactoryMago(AbstractFactory):

    def __init__(self):
        self._personaje=Personaje()
        self._personaje.setTipo("Mago")
        self._personaje.setSprites(self.crearSprite())
        self._personaje.setRuido(self.crearSonido())

    def crearSprite(self):
        buld=BuildSprtPersonaje(self._personaje.getTipo())
        buld.BuildPlano()
        buld.BuildSprite()
        return buld.getSprites()

    def crearSonido(self):
        buld=BuildRdoPersonaje(self._personaje.getTipo())
        buld.BuildSonido()
        return buld.getSonidos()

class FactoryRottom(AbstractFactory):

    def __init__(self):
        self._personaje=Personaje()
        self._personaje.setTipo("Rottom")
        self._personaje.setSprites(self.crearSprite())
        self._personaje.setRuido(self.crearSonido())

    def crearSprite(self):
        buld=BuildSprtPersonaje(self._personaje.getTipo())
        buld.BuildPlano()
        buld.BuildSprite()
        return buld.getSprites()

    def crearSonido(self):
        buld=BuildRdoPersonaje(self._personaje.getTipo())
        buld.BuildSonido()
        return buld.getSonidos()


def main():
    Fac=FactoryPrueba()
    m1=Fac.getPersonaje()
    print(m1.getSprites())
    print(m1.getRuido())
    pass

if __name__ == '__main__':
    main()
