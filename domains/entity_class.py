# -*- coding: utf-8 -*-
"""pythr.py: Visual modeling helper."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import abc

class Entity(abc.ABC):
    entity_counter = []

    @abc.abstractmethod
    def __init__(self) -> None:
        self.entity_counter.append(self.__class__)
        # super().__init__()

    @abc.abstractmethod
    def return_dict(self):
        pass

class Box(Entity):
    def __init__(
            self,
            width: float,
            height: float,
            depth: float,
            material: dict = {'color': 0xffffff},
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshBasicMaterial'
            ) -> None:
        self.geometry_type = 'BoxGeometry'
        self.geometry = {
                'width': width,
                'height': height,
                'depth': depth
                } 
        self.position = position
        self.rotation = rotation
        self.material = material
        self.material_type = material_type

    def return_dict(self):
        entity_dict = {
                'material_type': self.material_type,
                'geometry_type': self.geometry_type,
                'geometry': self.geometry,
                'material': self.material,
                'position': self.position,
                'rotation': self.rotation

                }
        return entity_dict

class Sphere(Entity):
    def __init__(
            self,
            radius: float,
            widthSegments: float,
            heightSegments: float,
            material: dict = {'color': 0xffffff},
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshBasicMaterial'
            ) -> None:
        self.geometry_type = 'SphereGeometry'
        self.geometry = {
                'radius': radius,
                'widthSegments': widthSegments,
                'heightSegments': heightSegments
                } 
        self.position = position
        self.rotation = rotation
        self.material = material
        self.material_type = material_type

    def return_dict(self):
        entity_dict = {
                'material_type': self.material_type,
                'geometry_type': self.geometry_type,
                'geometry': self.geometry,
                'material': self.material,
                'position': self.position,
                'rotation': self.rotation

                }
        return entity_dict

class Plane(Entity):
    def __init__(
            self,
            width: float,
            height: float,
            material: dict = {'color': 0xffffff},
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshBasicMaterial'
            ) -> None:
        self.geometry_type = 'PlaneGeometry'
        self.geometry = {
                'width': width,
                'height': height
                } 
        self.position = position
        self.rotation = rotation
        self.material = material
        self.material_type = material_type

    def return_dict(self):
        entity_dict = {
                'material_type': self.material_type,
                'geometry_type': self.geometry_type,
                'geometry': self.geometry,
                'material': self.material,
                'position': self.position,
                'rotation': self.rotation
                }
        return entity_dict

class Entity_fabric:
    @staticmethod
    def create(entity_type, *args, **kwargs):
        if entity_type == 'box':
            entity = Box(*args, **kwargs)
        elif entity_type == 'sphere':
            entity = Sphere(*args, **kwargs)
        elif entity_type == 'plane':
            entity = Plane(*args, **kwargs)
        else:
            entity = Box(*args, **kwargs)

        return entity


