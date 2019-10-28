#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      estudiantes
#
# Created:     30/09/2019
# Copyright:   (c) estudiantes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class BuilderSprites:
    _sprites=None
    _plano=None

    def getSprites(self):
        return self._sprites

    def getPlano(self):
        return self._plano

    def setPlano(self, plano):
        self._plano=plano

    def BuildSprite(self):
        pass

    def BuildPlano(self):
        pass

class BuildSprtPersonaje(BuilderSprites):

    def __init__(self, tipo):
        self.__tip=tipo

    def __getSpritesDir(self, a, b):
        return ['Sprites/Personajes/'+ self.__tip + '/'+'%d.gif' % it for it in range(a,b)]

    def BuildSprite(self):
        self._sprites=[self.__getSpritesDir(1,10),self.__getSpritesDir(10,19)]

    def BuildPlano(self):
        self._plano=1

class BuildSprtEscudo(BuilderSprites):

    def __init__(self, mat):
        self.__mater=mat

    def BuildSprite(self):
        self._sprites=['Sprites/Escudos/'+ self.__mater + '/'+'%d.png' % it for it in range(1,5)]

    def BuildPlano(self):
        self._plano=3


class BuildRuido:

    _sonidos=None

    def getSonidos(self):
        return self._sonidos

    def BuildSonido(self):
        pass

class BuildRdoPersonaje(BuildRuido):

    def __init__(self, nom):
        self._nombre=nom

    def BuildSonido(self):
        self._sonidos=['Efects/Gritos/'+self._nombre+'/'+'%d.wav' % it for it in range(1,5)]


def main():
    buld=BuildSprtPersonaje("Arceus")
    buld.BuildPlano()
    buld.BuildSprite()
    print(buld.getSprites())
    buld=BuildSprtEscudo("Madera")
    buld.BuildPlano()
    buld.BuildSprite()
    print(buld.getSprites())
    buld=BuildRdoPersonaje("Prueba")
    buld.BuildSonido()
    print(buld.getSonidos())
    pass

if __name__ == '__main__':
    main()
