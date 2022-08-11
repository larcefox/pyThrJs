#!/usr/bin/python
import json
import math
from domains.entity_class import Entity_fabric
from domains.entity_class import Entity


box = Entity_fabric.create('box', 1, 1, 5, color=0xff0000)
box1 = Entity_fabric.create('box', 5, 1, 1)
plane = Entity_fabric.create(
        'plane',
        20,
        20,
        texture='textures/blueprint.jpg',
        position={'x':0, 'y': -10, 'z': 0},
        rotation={'x': -(math.pi/2),'y': 0 , 'z': 0}
        )

def send_data():
    geometry = {
            entity.get_name:
            entity.return_dict() for entity in Entity.manager.get_entity_list
            }
    print(geometry)
    return json.dumps(geometry)

