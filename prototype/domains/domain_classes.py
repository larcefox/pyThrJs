# -*- coding: utf-8 -*-
import abc


class Observer(metaclass=abc.ABCMeta):
    observers = []
    def __init__(self):
        self._observer_state = None
        __class__.observers.append(self)

    @abc.abstractmethod
    def update(self, arg):
        pass


class Geometry(abc.ABC):

    auto_id = 0

    @abc.abstractmethod
    def serialize(self):
        pass
    
    @abc.abstractmethod
    def set_geometry(self):
        pass

    @abc.abstractmethod
    def set_material(self):
        pass


class Material(abc.ABC):

    auto_id = 0

    @abc.abstractmethod
    def set_mesh_type(self):
        pass


class Shape(abc.ABC):

    auto_id = 0

    @abc.abstractmethod
    def set_size(self):
        pass

    @abc.abstractmethod
    def set_segments_size(self):
        pass
