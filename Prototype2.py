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
import random

class Prototype:

    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

class Type1(Prototype):
    def __init__(self, number):
        self._type="tipo1"
        self._value=number

    def clone(self):
        return copy.copy(self)

class Type2(Prototype):
    def __init__(self, number):
        self._type="tipo2"
        self._value=number

    def clone(self):
        return copy.copy(self)

class ObjectFactory:

    _t1v1 = None
    _t2v1 = None
    _t1v2 = None
    _t2v2 = None

    @staticmethod
    def initialize():
        ObjectFactory._t1v1 = Type1(1)
        ObjectFactory._t1v2 = Type1(2)
        ObjectFactory._t2v1 = Type2(1)
        ObjectFactory._t2v2 = Type2(2)

    @staticmethod
    def getT1V1():
        return ObjectFactory._t1v1.clone()

    @staticmethod
    def getT1V2():
        return ObjectFactory._t1v2.clone()

    @staticmethod
    def getT2V1():
        return ObjectFactory._t2v1.clone()

    @staticmethod
    def getT2V2():
        return ObjectFactory._t2v2.clone()

def main():
    ObjectFactory.initialize()

    if random.randint(0,1)==1:
        instance = ObjectFactory.getT1V2()
    else:
        instance = ObjectFactory.getT2V1()

    print ("%s: %s" % (instance.getType(), instance.getValue()))
    print ("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.getT2V2()
    print ("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.getT1V1()
    print ("%s: %s" % (instance.getType(), instance.getValue()))
    pass

if __name__ == '__main__':
    main()
