# -*- coding: utf-8 -*

import threading


class Singleton(object):
    """
    基于类实现
    """
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):

        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance