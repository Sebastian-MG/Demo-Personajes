#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      lenovo
#
# Created:     16/09/2019
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame as pyg
import random

SIZE = WIDTH, HEIGHT = 400, 300
BACKGROUND_COLOR = pyg.Color('#202020')
FPS = 10

class mySprite(pyg.sprite.Sprite):
    def __init__(self, k, i, j, l, r, w, h):
        super(mySprite, self).__init__()
        self.images=[pyg.image.load('Sprites/Personajes/'+ str(k) +'%d.gif' % it) for it in range(i, j)]
        self.ind=0
        self.weed=l
        self.high=r
        self.left=l
        self.right=r
        self.image=self.images[self.ind]
        self.rect = pyg.Rect(self.left, self.right, w, h)
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
            self.left=self.weed
            self.right=self.high
        if self.right>=204 or self.right<=0:
            self.left=self.weed
            self.right=self.high
        #self.movL=0
        self.image=self.images[self.ind]
        self.rect = pyg.Rect(self.left, self.right, 96, 96)

    def movLeft(self, ll):
        self.movL=ll

    def movUp(self, rr):
        self.movR=rr

class personaje(pyg.sprite.Sprite):
    def __init__(self, chrc):
        super(personaje, self).__init__()
        self.images=[pyg.image.load('Sprites/Personajes/' + chrc + "/" +'%d.gif' % it) for it in range(1,18)]
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
    p=input("afasfas")

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
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    sprt.movLeft(-2)
                    sprt.update()
                if event.key == pyg.K_RIGHT:
                    sprt.movLeft(2)
                    sprt.update()
                if event.key == pyg.K_UP:
                    sprt.movUp(-2)
                    sprt.update()
                if event.key == pyg.K_DOWN:
                    sprt.movUp(2)
                    sprt.update()
            elif event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT:
                    sprt.movLeft(None)
                    sprt.update()
                if event.key == pyg.K_RIGHT:
                    sprt.movLeft(None)
                    sprt.update()
                if event.key == pyg.K_UP:
                    sprt.movUp(None)
                    sprt.update()
                if event.key == pyg.K_DOWN:
                    sprt.movUp(None)
                    sprt.update()

        movs.update()
        #movs1.update()
        #movs2.update()
        #movs3.update()
        #movs4.update()

        marco.fill(BACKGROUND_COLOR)

        '''fndm.update()
        fndm.draw(marco)'''
        movs.draw(marco)
        #movs1.draw(marco)
        #movs2.draw(marco)
        #movs3.draw(marco)
        #movs4.draw(marco)

        pyg.display.update()

        clck.tick(FPS)

    pass

if __name__ == '__main__':
    main()
