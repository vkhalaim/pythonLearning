# -*- coding: utf-8 -*-

from utils import get_input_function


class Storage(object):
    obj = None
    items = None


    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj