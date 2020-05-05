# -*- coding: utf-8 -*


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class SingletonObject(object):
    a = 1

    def __init__(self, x=0):
        self.x = x