# -*- coding: utf-8 -*
import threading


class SingletonType(type):
    """
   基于 metaclass 方法实现
   """
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class SingletonObject(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name