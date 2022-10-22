from math import sqrt
from graph import get_map
import squarify


html_map = get_map()
rooms_qty = len(html_map['div'])
x = 0.
y = 0.

# counts quantity of tags in div
rooms_dict = {}

def rects_calculate():
    # counts squars of div
    for div_name in html_map['div']:
        rooms_dict[div_name] = [len(html_map['div'][div_name]), sqrt(len(html_map['div'][div_name])), 0]
        for child_div in html_map['div']:
            if child_div in html_map['div'][div_name]:
                rooms_dict[div_name][1] += sqrt(len(html_map['div'][div_name]))
                rooms_dict[div_name][2] += 1
    # gets squares from dict
    rooms_squares = list(value[1] for value in rooms_dict.values())
    # change 0 to 1 in squars list
    rooms_squares = list(map(lambda x: x*100 if x else 100, rooms_squares))

    height = width = sqrt(sum(rooms_squares))
    rooms_squares.sort(reverse=True)
    rooms_squares = squarify.normalize_sizes(rooms_squares, width, height)
    print(sum(rooms_squares), width * height)
    print(rooms_squares)
    rects = squarify.squarify(rooms_squares, x, y, width, height)
    print(rects)
    return rects

if __name__ == '__main__':
    rects_calculate()
