#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      estudiantes
#
# Created:     10/10/2019
# Copyright:   (c) estudiantes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Factory import *
import pygame as pyg
import random

SIZE = WIDTH, HEIGHT = 400, 300
BACKGROUND_COLOR = pyg.Color('#202020')
FPS = 15

class PersJugable(pyg.sprite.Sprite):
    def __init__(self, personaje):
        super(PersJugable, self).__init__()
        self._personaje=personaje
        self.velocidad=0
        self.ind=0
        self.posX=5
        self.piso=200
        self.Derecha()
        self.Detener()

    def Detener(self):
        self.velocidad=0

    def setPosX(self, newX):
        self.posX=newX

    def Izquierda(self):
        self.images=self._personaje.getSprites()[1]
        self.ind=0
        self.image=self.images[self.ind]
        self.rect=self.image.get_rect()
        self.velocidad=-2

    def Derecha(self):
        self.images=self._personaje.getSprites()[0]
        self.ind=0
        self.image=self.images[self.ind].convert()
        self.rect=self.image.get_rect()
        self.velocidad=2

    def update(self):
        if self.velocidad!=0:
            self.ind+=1
            if self.ind>=len(self.images):
                self.ind=0
        self.image=self.images[self.ind].convert()
        self.rect.left=(self.posX+self.velocidad)
        self.posX=self.rect.left
        self.rect.top=self.piso

    def draw(self, marco):
        marco.blit(self.image, self.rect)

class PersNPC(PersJugable):
    perseguir=None

    def Existir(self):
        if self.perseguir!=None:
            if self.perseguir.posX<5 and self.posX==5:
                self.Detener()
            elif self.perseguir.posX>295 and self.posX==295:
                self.Detener()
            else:
                if self.perseguir.posX>self.posX:
                    self.Derecha()
                elif self.perseguir.posX<self.posX:
                    self.Izquierda()
                else:
                    self.Detener()
        else:
            if self.posX<5:
                self.Derecha()
                self.velocidad=random.randint(2,8)
            elif self.posX>275:
                self.Izquierda()
                self.velocidad=-1*(random.randint(2,8))
            else:
                if random.randint(0,1)==0:
                    self.Derecha()
                    #self.velocidad=random.randint(2,8)
                else:
                    if random.randint(0,1)==0:
                        self.Izquierda()
                        #self.velocidad=-1*(random.randint(2,8))
                    else:
                        self.Detener()

def main():
    ObjectFactory.initialize()
    pyg.init()
    Fac=FactoryArceus()
    m1=Fac.getPersonaje()
    Fac=FactoryMago()
    m2=Fac.getPersonaje()
    #orda=[Fac.getPersonaje() for i in range(random.randint(1,5))]
    #print(m1.getSprites())
    #print(m1.getRuido())
    pyg.init()

    SONG_END = pyg.USEREVENT + 1

    pyg.mixer.music.set_endevent(SONG_END)
    pyg.mixer.music.load('Efects/SevenSeasofRhye.mp3')
    pyg.mixer.music.play()

    marco=pyg.display.set_mode(SIZE)

    #sprt3=mySprite(20, 19, 35, random.randint(10,250), random.randint(10,150)) #archie
    #sprt1=mySprite(8, 38, 56, random.randint(10,250), random.randint(150,300)) #polilla
    #sprt2=mySprite(7, 33, 37, random.randint(250,500), random.randint(10,150)) #genesect
    #sprt=mySprite(7, 10, 27, 152, 102, 96, 96) #Arceus
    sprt=PersJugable(m1)
    npc=PersNPC(m2)
    npc.setPosX(random.randint(15,200))
    orda=[PersNPC(Fac.getPersonaje()) for i in range(random.randint(1,5))]
    for np in orda:
        np.setPosX(random.randint(15,200))
    #sprt4=mySprite(5, 67, 71, random.randint(250,500), random.randint(150,300)) #Rotom

    #movs = pyg.sprite.Group(sprt)
    #orda = pyg.sprite.Group(npc)
    #movs1 = pyg.sprite.Group(sprt1)
    #movs2 = pyg.sprite.Group(sprt2)
    #movs3 = pyg.sprite.Group(sprt3)
    #movs4 = pyg.sprite.Group(sprt4)

    '''fnd=mySprite(10, 8, 9, 0, 0, 300, 400) #Arceus
    fndm = pyg.sprite.Group(fnd)
    fnd.movLeft(None)
    fnd.movUp(None)
    fnd.update()'''

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
                if event.key == pyg.K_p:
                    if npc.perseguir==None:
                        npc.perseguir=sprt
                    else:
                        npc.perseguir=None
                    for np in orda:
                        if np.perseguir==None:
                            np.perseguir=sprt
                        else:
                            np.perseguir=None
        marco.fill(BACKGROUND_COLOR)
        marco.fill(BACKGROUND_COLOR)
        npc.Existir()
        npc.update()
        npc.draw(marco)
        for np in orda:
            np.Existir()
            np.update()
            np.draw(marco)
        sprt.update()
        sprt.draw(marco)
        pyg.display.update()
        clck.tick(FPS)
    print(jugador.getEscudo().getMaterial())
    pass

if __name__ == '__main__':
    main()
