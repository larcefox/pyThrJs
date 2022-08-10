# -*- coding: utf-8 -*-
"""pythr.py: Visual modeling helper."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import abc


class Entity_manager():

    entity_list = set()

    def counter(self, entity_class) -> None:
        self.entity_list.add(entity_class)

    def clear_counter(self):
        self.entity_list.clear()
        for i in self.entity_list: del i

    @property
    def get_entity_list(self):
        return self.entity_list


class Entity(abc.ABC, Entity_manager):
    manager = Entity_manager()

    @abc.abstractmethod
    def return_dict(self):
        pass


class Box(Entity):
    def __init__(
            self,
            width: float,
            height: float,
            depth: float,
            color:dict = {'r': 0, 'g': 0, 'b': 0},
            texture = None,
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshBasicMaterial'
            ) -> None:
        self.counter(self)
        self.geometry_type = 'BoxGeometry'
        self.geometry = {
                'width': width,
                'height': height,
                'depth': depth
                } 
        self.position = position
        self.rotation = rotation
        self.material = {'texture': texture} if texture else {'color': color}
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
            color:dict = {'r': 0, 'g': 0, 'b': 0},
            texture = None,
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
        self.material = {'texture': texture} if texture else {'color': color}
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
            color:dict = {'r': 0, 'g': 0, 'b': 0},
            texture = None,
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
        self.material = {'texture': texture} if texture else {'color': color}
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


