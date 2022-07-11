#!/usr/bin/python
import json


def send_data():
    geometry = {
            'Object1':{
                'type': 'BoxGeometry',
                'id': 0,
                'width': 1,
                'height': 1,
                'depth': 5,
                'color': 0xff00ff,
                },

            'Object2':{
                'type': 'BoxGeometry',
                'id': 0,
                'width': 5,
                'height': 1,
                'depth': 1,
                'color': 0x00ff00,
                    
            },
            'Object3':{
                'type': 'BoxGeometry',
                'id': 0,
                'width': 1,
                'height': 5,
                'depth': 1,
                'color': 0x0000ff,
                    
            }
    }
    return json.dumps(geometry)

