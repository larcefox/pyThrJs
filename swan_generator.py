from domains.platform_class import Platform_fabric, Platform, Platform_manager


def rounder(base: int | list, devider):
    return int(round((len(base) if isinstance(base, list) else base) / devider, 0))

def generate_swan():

    start_page = Platform_fabric.create('http://www.excel-vba.ru/')
    start_page.generate_inner_childs()
    platforms = Platform.manager.get_platform_list()

    platforms_on_level = 4
    level_multiplier = 30
    levels = rounder(platforms, platforms_on_level)
    start_page_level = rounder(levels, 2)
    rects_list = [] 
    gap = 10
    places_x = {
            0: 1,
            1: 0,
            2: -1,
            3: 0
            }

    places_y = {
            0: 0,
            1: 1,
            2: 0,
            3: -1
            }

    for level in range(levels):
        for place in range(platforms_on_level):
                        
            if platforms:

                platform = platforms.pop()

                if platform.get_hash == start_page.get_hash:

                    rects_list.append([
                            {'start_page': {
                                'x': 0,
                                'y': 0,
                                'z': start_page_level * level_multiplier,
                                'dx': start_page.get_size[0],
                                'dy': start_page.get_size[1],
                                }},
                            ])
                else:

                    rects_list.append({platform.get_hash: {
                        'x': (start_page.get_size[0] / 2 +  platform.get_size[0] / 2 + gap) * places_x[place],
                        'y': (start_page.get_size[1] / 2 +  platform.get_size[1] / 2 + gap) * places_y[place],
                        'z': level * level_multiplier,
                        'dx': platform.get_size[0],
                        'dy': platform.get_size[1],
                        }})

    return rects_list


if __name__ == '__main__':
    print(generate_swan())
