#!/usr/bin/python
import json


def main():
    geometry = {
            'BoxGeometry':{
                'id':0,
                'width':1,
                'height':1,
                'depth':5,
                'color':0x0000FF,
                }
            }
    return json.dumps(geometry)

if __name__ == '__main__':
    print(main())
