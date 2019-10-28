#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      lenovo
#
# Created:     10/10/2019
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Escudo():

    def __init__(self):
        self._material=None
        self._sprites = None

    def getMaterial(self):
        return self._material

    def getSprites(self):
        return self._sprites

    def setMaterial(self, mat):
        self._material = mat

    def setSprites(self, sprts):
        self._sprites = sprts

class Personaje():

    def __init__(self):
        self._tipo=None
        self._escudo = Escudo()
        self._sprites = None
        self._ruido = None

    def getTipo(self):
        return self._tipo

    def getEscudo(self):
        return self._escudo

    def getSprites(self):
        return self._sprites

    def getRuido(self):
        return self._ruido

    def setTipo(self, tip):
        self._tipo = tip

    def setSprites(self, sprts):
        self._sprites = sprts

    def setRuido(self, rudo):
        self._ruido = rudo


def main():
    pass

if __name__ == '__main__':
    main()
