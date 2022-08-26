# -*- coding: utf-8 -*-
"""pythr.py: Visual modeling helper."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

import abc


class Entity_manager():

    entity_list = []
    camera_list = []
    light_list = []

    def entity_list_append(self, entity_class, entity_type) -> None:
        if entity_type == 'shape':
            self.entity_list.append(entity_class)
        elif entity_type == 'camera':
            self.camera_list.append(entity_class)
        elif entity_type == 'light':
            self.light_list.append(entity_class)

    def clear_entity_list(self) -> None:
        for i in self.entity_list: del i
        self.entity_list.clear()

        for i in self.camera_list: del i
        self.camera_list.clear()

        for i in self.light_list: del i
        self.light_list.clear()

    def get_entity_list(self, entity_type):
        if entity_type == 'shape':
            return self.entity_list
        elif entity_type == 'camera':
            return self.camera_list
        elif entity_type == 'light':
            return self.light_list
        else:
            return self.entity_list


class Entity(abc.ABC, Entity_manager):
    manager = Entity_manager()

    @abc.abstractmethod
    def return_dict(self):
        pass

    def get_name(self, entity_type):
        entity_number = self.manager.get_entity_list(entity_type).index(self)
        if entity_type == 'shape':
            return ''.join(('Shape', str(entity_number)))
        elif entity_type == 'camera':
            return  ''.join(('Camera', str(entity_number)))
        elif entity_type == 'light':
            return  ''.join(('light', str(entity_number)))
        else:
            return 'NaN'


class Box(Entity):
    def __init__(
            self,
            width: float,
            height: float,
            depth: float,
            name: str = 'Entity',
            color:int = 0xffffff,
            texture = None,
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshBasicMaterial',
            cast_shadow = True,
            receive_shadow = True
            ) -> None:
        self.geometry_type = 'BoxGeometry'
        self.geometry = {
                'width': width,
                'height': height,
                'depth': depth
                } 
        self.name = name
        self.position = position
        self.rotation = rotation
        self.material = {'texture': texture} if texture else {'color': color}
        self.material_type = material_type
        self.cast_shadow = cast_shadow
        self.receive_shadow = receive_shadow

    def return_dict(self) -> dict:
        entity_dict = {
                'material_type': self.material_type,
                'geometry_type': self.geometry_type,
                'geometry': self.geometry,
                'material': self.material,
                'position': self.position,
                'rotation': self.rotation,
                'castShadow': self.cast_shadow,
                'receiveShadow': self.receive_shadow

                }
        return entity_dict


class Sphere(Entity):
    def __init__(
            self,
            radius: float,
            widthSegments: float,
            heightSegments: float,
            name: str = 'Entity',
            color:int = 0xffffff,
            texture = None,
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshStandardMaterial',
            cast_shadow = True,
            receive_shadow = True
            ) -> None:
        self.name = name
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
        self.cast_shadow = cast_shadow
        self.receive_shadow = receive_shadow

    def return_dict(self) -> dict:
        entity_dict = {
                'material_type': self.material_type,
                'geometry_type': self.geometry_type,
                'geometry': self.geometry,
                'material': self.material,
                'position': self.position,
                'rotation': self.rotation,
                'castShadow': self.cast_shadow,
                'receiveShadow': self.receive_shadow

                }
        return entity_dict


class Plane(Entity):
    def __init__(
            self,
            width: float,
            height: float,
            name: str = 'Entity',
            color:int = 0xffffff,
            texture = None,
            position: dict = {'x': 0, 'y': 0, 'z': 0}, 
            rotation: dict = {'x': 0, 'y': 0, 'z': 0},
            material_type: str = 'MeshStandardMaterial',
            cast_shadow = False,
            receive_shadow = True
            ) -> None:
        self.geometry_type = 'PlaneGeometry'
        self.geometry = {
                'width': width,
                'height': height
                } 
        self.name = name
        self.position = position
        self.rotation = rotation
        self.material = {'texture': texture} if texture else {'color': color}
        self.material_type = material_type
        self.cast_shadow = cast_shadow
        self.receive_shadow = receive_shadow


    def return_dict(self) -> dict:
        entity_dict = {
                'material_type': self.material_type,
                'geometry_type': self.geometry_type,
                'geometry': self.geometry,
                'material': self.material,
                'position': self.position,
                'rotation': self.rotation,
                'castShadow': self.cast_shadow,
                'receiveShadow': self.receive_shadow
                }
        return entity_dict


class Camera(Entity):
    def __init__(
            self, 
            name: str = 'Entity',
            camera_type: str='PerspectiveCamera', 
            fild_of_view: int=75, 
            aspect_ratio: str='innerWidth / innerHeight',
            clipping_plane_near: float=0.1,
            clipping_plane_far: float=1000,
            position: dict={'x': -40, 'y': 40, 'z': 40}
            ) -> None:
        self.name = name
        self.camera_type = camera_type
        self.fild_of_view = fild_of_view
        self.aspect_ratio = aspect_ratio
        self.clipping_plane_near = clipping_plane_near
        self.clipping_plane_far = clipping_plane_far
        self.position = position

    def return_dict(self) -> dict:
        return self.__dict__


class Light(Entity):
    def __init__(
            self, 
            name: str = 'Entity',
            light_type: str='DirectionalLight',
            color: int=0xffffff,
            intensity: float=1.0,
            shadow: dict={
                'bias': -0.001,
                'mapSize': {'width': 2048, 'height': 2048},
                'camera': {
                    'near': 0.5, 
                    'far': 500, 
                    'left': 100, 
                    'right': -100,
                    'top': 100,
                    'bottom': -100
                }
            },
            target_position: dict={'x': 20, 'y': 100, 'z': 10},
            position: dict={'x': 20, 'y': 100, 'z': 10},
            cast_shadow = True,
            ) -> None:
        self.name = name
        self.color = color
        self.intensity = intensity
        self.light_type = light_type
        self.shadow = shadow
        self.target_position = target_position
        self.position = position
        self.cast_shadow = cast_shadow

    def return_dict(self) -> dict:
        entity_dict = {
                'name': self.name,
                'color': self.color,
                'intensity': self.intensity,
                'light_type': self.light_type,
                'position': self.position,
                'target_position': self.target_position,
                'shadow': self.shadow,
                'castShadow': self.cast_shadow
                }
        return entity_dict


class Entity_fabric:
    @staticmethod
    def create(entity_type, *args, **kwargs):
        shape_dict = {'box': Box, 'sphere': Sphere, 'plane': Plane}
        if entity_type in shape_dict:
            entity = shape_dict[entity_type](*args, **kwargs)
            entity.entity_list_append(entity, 'shape') 
            entity.name = entity.get_name('shape')
        elif entity_type == 'camera':
            entity = Camera(*args, **kwargs)
            entity.entity_list_append(entity, entity_type) 
            entity.name = entity.get_name(entity_type)
        elif entity_type == 'light':
            entity = Light(*args, **kwargs)
            entity.entity_list_append(entity, entity_type) 
            entity.name = entity.get_name(entity_type)
        else:
            entity = Box(*args, **kwargs)
            entity.entity_list_append(entity, 'shape')
            entity.name = entity.get_name('shape')

        return entity

