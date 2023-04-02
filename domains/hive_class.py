from .platform_class import Platform_fabric


class Hive():
    def __init__(self, url) -> None:
        self.url = url
        self.start_platform = Platform_fabric.create(self.url)
        self.all_platforms = self.start_platform.generate_platforms()
        self.start_platform_dx = self.start_platform.size[0]
        self.start_platform_dy = self.start_platform.size[1]
        self.hive_coordinates = {}
        self.places_pre_level = 4
        self.start_platform_lvl = 10        
        self.gap = 10
        self.level = 0
        self.place = 0

    def platform_x_pos(self, n):
        places = {
                0: 1,
                1: 0,
                2: -1,
                3: 0
                }
        return places[n]

    def platform_y_pos(self, n):
        places = {
                0: 0,
                1: 1,
                2: 0,
                3: -1 
                }
        return places[n]

    @staticmethod
    def rounder(number: list, devider:int) -> int:
        return int(round(len(number) if isinstance(number, list) else number / devider, 0))
        
    def place_rotator(self):
        if self.place < (self.places_pre_level - 1):
            self.place += 1 
        else:
            self.place = 0
            self.level += 10

    def place_platform(self):
        for platform in self.all_platforms:
            if platform.hash == self.start_platform.hash:
                self.hive_coordinates[self.start_platform.hash] = {
                        'dx': self.start_platform_dx,
                        'dy': self.start_platform_dy,
                        'x': 0,
                        'y': 0,
                        'z': self.level,
                        }
            else:
                self.hive_coordinates[platform.hash] = {
                        'dx': platform.size[0],
                        'dy': platform.size[1],
                        'x': (0.5 * self.start_platform_dx + self.gap + 0.5 * platform.size[0]) * self.platform_x_pos(self.place),
                        'y': (0.5 * self.start_platform_dy + self.gap + 0.5 * platform.size[1]) * self.platform_y_pos(self.place),
                        'z': self.level
                        }
                self.place_rotator()
                print(self.hive_coordinates[platform.hash])

    def calc_hive(self):
        self.place_platform()
        return self.hive_coordinates



if __name__ == '__main__':
    hive = Hive('http://mail.ru')
    
