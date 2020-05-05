# -*- coding: utf-8 -*

from singleton1 import singleton
from singleton2 import SingletonObject
from singleton3 import Singleton as Singleton3
from singleton4 import Singleton as Singleton4
from singleton5 import SingletonObject as Singleton5

if __name__ == '__main__':
    singleton1 = singleton
    singleton2 = singleton
    if (singleton1 is singleton2):
        print('singleton1 verify pass')

    singleton1 = SingletonObject(1)
    singleton2 = SingletonObject(2)

    if (singleton1 is singleton2):
        print('singleton2 verify pass')

    singleton1 = Singleton3().instance()
    singleton2 = Singleton3().instance()

    if (singleton1 is singleton2):
        print('singleton3 verify pass')

    singleton1 = Singleton4()
    singleton2 = Singleton4()

    if (singleton1 is singleton2):
        print('singleton4 verify pass')

    singleton1 = Singleton5('1')
    singleton2 = Singleton5('2')

    if (singleton1 is singleton2):
        print('singleton5 verify pass')
