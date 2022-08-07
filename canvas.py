#!/usr/bin/python
import json
import math
from domains.entity_class import Entity_fabric


box = Entity_fabric.create('box', 1, 1, 5)

def send_data():
    geometry = {
            'Object1': box.return_dict(),

            'Object2':{
                'material_type': 'MeshBasicMaterial',
                'geometry_type': 'BoxGeometry',
                'geometry':{
                    'width': 5,
                    'height': 1,
                    'depth': 1,
                },
                'material': {
                    'color': 0x00ff00,
                },
                'position':{
                    'x': 0,
                    'y': 0,
                    'z': 0,
                    },
                'rotation':{
                    'x': 0,
                    'y': 0,
                    'z': 0,
                    },
            },
            'Object3':{
                'material_type': 'MeshBasicMaterial',
                'geometry_type': 'BoxGeometry',
                'geometry':{
                    'width': 5,
                    'height': 1,
                    'depth': 1,
                },
                'material': {
                    'color': 0xff0000,
                },
                'position':{
                    'x': 0,
                    'y': 0,
                    'z': 0,
                    },
                'rotation':{
                    'x': 0,
                    'y': 0,
                    'z': 0,
                    },
            },
            'Object4':{
                'material_type': 'MeshBasicMaterial',
                'geometry_type': 'SphereGeometry',
                'geometry':{
                    'radius': 1,
                    'widthSegments': 32,
                    'heightSegments': 16,
                },
                'material': {
                    'color': 0x00ffff,
                },
                'position':{
                    'x': 0,
                    'y': 0,
                    'z': 0,
                    },
                'rotation':{
                    'x': 0,
                    'y': 0,
                    'z': 0,
                    },
            },

            'Object5':{
                'material_type': 'MeshBasicMaterial',
                'geometry_type': 'PlaneGeometry',
                'geometry':{
                    'width': 10,
                    'height': 10,
                },
                'material': {
                    'texture' :'textures/blueprint.jpg',
                },
                'position':{
                    'x': 0,
                    'y': -10,
                    'z': 0,
                    },
                'rotation':{
                    'x': -(math.pi / 2),
                    'y': 0,
                    'z': 0,
                    },
            },
    }
    return json.dumps(geometry)

