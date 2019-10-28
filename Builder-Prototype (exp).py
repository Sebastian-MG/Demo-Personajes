#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      lenovo
#
# Created:     22/09/2019
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame as pyg
import copy

SIZE = WIDTH, HEIGHT = 400, 300
BACKGROUND_COLOR = pyg.Color('#202020')
FPS = 15

class SpritePers(pyg.sprite.Sprite):
    def __init__(self, chrc):
        super(SpritePers, self).__init__()
        self.person=chrc
        self.direccion=0
        self.ind=0
        self.Derecha()
        self.Detener()
        self.posX=5
        self.piso=200

    def Detener(self):
        self.direccion=0

    def Izquierda(self):
        self.images=self.person.getSprIzq()
        self.ind=0
        self.image=self.images[self.ind]
        self.rect=self.image.get_rect()
        self.direccion=-2

    def Derecha(self):
        self.images=self.person.getSprDer()
        self.ind=0
        self.image=self.images[self.ind].convert()
        self.rect=self.image.get_rect()
        self.direccion=2

    def update(self):
        if self.direccion!=0:
            self.ind+=1
            if self.ind>=len(self.images):
                self.ind=0
        self.image=self.images[self.ind].convert()
        self.rect.left=(self.posX+self.direccion)
        self.posX=self.rect.left
        self.rect.top=self.piso

    def draw(self, marco):
        marco.blit(self.image, self.rect)

class Escudo():
    __material=None

    def getMaterial(self):
        return self.__material

    def setMaterial(self, mat):
        self.__material = mat

class Arma():
    __material=None

    def getMaterial(self):
        return self.__material

    def setMaterial(self, mat):
        self.__material = mat

class Personaje():
    __sprIzq=None
    __sprDer=None
    __escudo=Escudo()
    __arma=Arma()
    __tipo=None

    def getSprIzq(self):
        return self.__sprIzq

    def getSprDer(self):
        return self.__sprDer

    def getEscudo(self):
        return self.__escudo

    def getArma(self):
        return self.__arma

    def getTipo(self):
        return self.__tipo

    def setSprIzq(self, spr):
        self.__sprIzq=spr

    def setSprDer(self, spr):
        self.__sprDer=spr

    def setEscudo(self, esc):
        self.__escudo=esc

    def setArma(self, arm):
        self.__arma=arm

    def setTipo(self, tip):
        self.__tipo=tip

class Prototype:
    _pers=None

    def clone(self):
        pass

class Arceus(Prototype):

    def __init__(self):
        self._pers=Personaje()
        self._pers.setTipo("Arceus")

    def getPersonaje(self):
        return self._pers

    def clone(self):
        return copy.deepcopy(self)

class Orco(Prototype):

    def __init__(self):
        self._pers=Personaje()
        self._pers.setTipo("Orco")

    def getPersonaje(self):
        return self._pers

    def clone(self):
        return copy.deepcopy(self)

class Trol(Prototype):

    def __init__(self):
        self._pers=Personaje()
        self._pers.setTipo("Trol")

    def getPersonaje(self):
        return self._pers

    def clone(self):
        return copy.deepcopy(self)

class ObjectFactory:
    _Orco = None
    _Arceus = None
    _Trol = None

    @staticmethod
    def initialize():
        ObjectFactory._Arceus=Arceus()
        ObjectFactory._Orco=Orco()
        ObjectFactory._Trol=Trol()

    @staticmethod
    def getArceus():
        return ObjectFactory._Arceus.clone()

    @staticmethod
    def getOrco():
        return ObjectFactory._Orco.clone()

    @staticmethod
    def getTrol():
        return ObjectFactory._Trol.clone()

class Builder:
    _personaje=None

    def getPersonaje(self):
        return self._personaje

    def getSprIzq(self):
        pass

    def getSprDer(self):
        pass

    def getEscudo(self):
        pass

    def getArma(self):
        pass

class BuilderArceus(Builder):
    def __init__(self):
        self._personaje=ObjectFactory.getArceus()

    def BuildSprIzq(self):
        self._personaje.getPersonaje().setSprIzq([pyg.image.load('Sprites/Personajes/'+ self._personaje.getPersonaje().getTipo() + '/'+'%d.gif' % it) for it in range(1,9)])

    def BuildSprDer(self):
        self._personaje.getPersonaje().setSprDer([pyg.image.load('Sprites/Personajes/'+ self._personaje.getPersonaje().getTipo() + '/'+'%d.gif' % it) for it in range(10,18)])

    def BuildEscudo(self):
        self._personaje.getPersonaje().setEscudo(Escudo())

    def BuildArma(self):
        self._personaje.getPersonaje().setArma(Arma())

class Director():
    __builderPersonaje=None

    def setBuilderPersonaje(self, consPer):
        self.__builderPersonaje=consPer

    def getPersonaje(self):
        return self.__builderPersonaje.getPersonaje().getPersonaje()

    def BuildPersonaje(self):
        self.__builderPersonaje.BuildSprIzq()
        self.__builderPersonaje.BuildSprDer()
        self.__builderPersonaje.BuildEscudo()
        self.__builderPersonaje.BuildArma()

ObjectFactory.initialize()

def main():
    cliente=Director()
    persona=BuilderArceus()
    cliente.setBuilderPersonaje(persona)
    cliente.BuildPersonaje()
    jugador=cliente.getPersonaje()

    pyg.init()

    '''SONG_END = pyg.USEREVENT + 1
    pyg.mixer.music.set_endevent(SONG_END)
    pyg.mixer.music.load('Efects/SevenSeasofRhye.mp3')
    pyg.mixer.music.play()'''

    marco=pyg.display.set_mode(SIZE)
    marco.fill(BACKGROUND_COLOR)

    sprt=SpritePers(jugador)
    clck=pyg.time.Clock()

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
            elif event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT:
                    sprt.Detener()
                if event.key == pyg.K_RIGHT:
                    sprt.Detener()
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    sprt.Izquierda()
                if event.key == pyg.K_RIGHT:
                    sprt.Derecha()
        marco.fill(BACKGROUND_COLOR)
        sprt.update()
        sprt.draw(marco)
        pyg.display.update()
        clck.tick(FPS)
    print(jugador.getEscudo().getMaterial())
    pass

if __name__ == '__main__':
    main()

'''class jugador(pyg.sprite.Sprite):
    def __init__(self, chrc):
        super(personaje, self).__init__()
        self.images=[pyg.image.load('Sprites/' + chrc + "/" +'%d.gif' % it) for it in range(1,18)]
        self.ind=0
        self.startW=5
        self.startU=5
        #self.posW=self.startW
        #self.posW=self.startW
        self.left=self.startW
        self.right=self.startW
        self.image=self.images[self.ind]
        self.rect = pyg.Rect(self.left, self.right, 96, 96)
        self.movL=0
        self.movR=0

    def update(self):
        self.ind+=1
        rand=7
        if self.movL==0:
            self.left+=random.randint(-rand,rand)
        elif self.movL==None:
            self.left+=0
        else:
            self.left+=self.movL
        if self.movR==0:
            self.right+=random.randint(-rand,rand)
        elif self.movR==None:
            self.right+=0
        else:
            self.right+=self.movR
        if self.ind>=len(self.images):
            self.ind=0
        if self.left>=304 or self.left<=0:
            self.left=self.startW
            self.right=self.startU
        if self.right>=204 or self.right<=0:
            self.left=self.startW
            self.right=self.startU
        #self.movL=0
        self.image=self.images[self.ind]
        self.rect = pyg.Rect(self.left, self.right, 96, 96)

    def movLeft(self, ll):
        self.movL=ll

    def movUp(self, rr):
        self.movR=rr

def main():
    pyg.init()

    SONG_END = pyg.USEREVENT + 1

    pyg.mixer.music.set_endevent(SONG_END)
    pyg.mixer.music.load('Efects/SevenSeasofRhye.mp3')
    pyg.mixer.music.play()

    #p=input("afasfas")
    p="Arceus"

    marco=pyg.display.set_mode(SIZE)

    #sprt3=mySprite(20, 19, 35, random.randint(10,250), random.randint(10,150)) #archie
    #sprt1=mySprite(8, 38, 56, random.randint(10,250), random.randint(150,300)) #polilla
    #sprt2=mySprite(7, 33, 37, random.randint(250,500), random.randint(10,150)) #genesect
    #sprt=mySprite(7, 10, 27, 152, 102, 96, 96) #Arceus
    sprt=personaje(p)
    #sprt4=mySprite(5, 67, 71, random.randint(250,500), random.randint(150,300)) #Rotom

    movs = pyg.sprite.Group(sprt)
    #movs1 = pyg.sprite.Group(sprt1)
    #movs2 = pyg.sprite.Group(sprt2)
    #movs3 = pyg.sprite.Group(sprt3)
    #movs4 = pyg.sprite.Group(sprt4)

    fnd=mySprite(10, 8, 9, 0, 0, 300, 400) #Arceus
    fndm = pyg.sprite.Group(fnd)
    fnd.movLeft(None)
    fnd.movUp(None)
    fnd.update()

    clck=pyg.time.Clock()

    while True:
'''
