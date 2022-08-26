#!/usr/bin/python
import json
import math
import random
from domains.entity_class import Entity_fabric
from domains.entity_class import Entity


directional_light = Entity_fabric.create('light')
ambient_light = Entity_fabric.create('light', light_type='AmbientLight')

plane = Entity_fabric.create(
        'plane',
        100, 
        100,
        texture='textures/blueprint.jpg',
        color=0xffffff,
        position={'x':0, 'y': 0, 'z': 0},
        rotation={'x': -(math.pi/2),'y': 0 , 'z': 0}
        )

box = Entity_fabric.create('box', 5, 1, 1, position={'x': 0, 'y': 10, 'z': 0})

for i in list(range(1, 2)):
    Entity_fabric.create(
            'box', 1, 1, 5, 
            position={'x': -25 + i, 'y': 10, 'z': 0}, 
            rotation={'x': i/10, 'y': 0, 'z': 0}, 
            color=0xff0000
            )

# for x in list(range(-9, 8)):
    # for y in list(range(-9, 8)):
        # Entity_fabric.create(
                # 'box', 1, 1, 2, 
                # position={
                    # 'x': random.random() + x * 4, 
                    # 'y': random.random() * 4 + 2, 
                    # 'z': random.random() + y * 5
                    # }, 
                # color=0x80807f)

def send_data():
    # TODO rewrite for loop creation
    camera = Entity_fabric.create('camera')
    lights = {
            light.name:
            light.return_dict() for light in Entity.manager.get_entity_list('light')
            }
    geometries = {
            entity.name:
            entity.return_dict() for entity in Entity.manager.get_entity_list('shape')
            }
    print(lights)
    print(geometries)
    return {
            'camera': camera.return_dict(), 
            'lights': json.dumps(lights),
            'shape': json.dumps(geometries)
            }

