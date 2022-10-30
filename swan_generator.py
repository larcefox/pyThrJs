import squarify
from domains.platform_class import Platform_fabric, Platform, Platform_manager

def generate_swan():
    start_page = Platform_fabric.create('http://docs.python.org')
    start_page.generate_inner_childs()

    x = y = 0.

    values = [i.get_size[0] * i.get_size[1] for i in Platform.manager.get_platform_list()]
    width = sum([i.get_size[0] for i in Platform.manager.get_platform_list()])
    height = sum([i.get_size[1] for i in Platform.manager.get_platform_list()])

    # values must be sorted descending (and positive, obviously)
    values.sort(reverse=True)

    # the sum of the values must equal the total area to be laid out
    # i.e., sum(values) == width * height
    values = squarify.normalize_sizes(values, width, height)

    # returns a list of rectangles
    rects = squarify.squarify(values, x, y, width, height)

    # padded rectangles will probably visualize better for certain cases
    padded_rects = squarify.padded_squarify(values, x, y, width, height)

    return rects
