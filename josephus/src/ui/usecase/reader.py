# -*- coding: utf-8 -*
import abc


class Reader(abc.ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    @abc.abstractmethod
    def read(self):
        pass
