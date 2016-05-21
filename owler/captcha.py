import math
from operator import itemgetter

from PIL import Image

NUMS = 5


class VectorCompare:
    def magnitude(self, values):
        total = sum(element**2 for element, count in values.iteritems())
        return math.sqrt(total)

    def relation(self, values1, values2):
        max_value = 0
        for element, count in values1.iteritems():
            if element in values2:
                max_value += count * values2[element]
        return max_value / (self.magnitude(values1) * self.magnitude(values2))


def closest_color(color, colors):
    red, green, blue = color
    distances = [(r - red, g - green, b - blue) for r, g, b in colors]
    distances = [sum((r**2, g**2, b**2)) for r, g, b in distances]
    color_index, _ = min((val, index) for val, index in enumerate(distances))
    return colors[color_index]


def get_top_colors(image, amount):
    width, height = image.size
    histogram = image.getcolors(width * height)
    top = sorted(histogram, key=itemgetter(0), reverse=True)[:amount]
    return [color for amount, color in top]


def reduce_to_colorset(image, colorset):
    width, height = image.size
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            if not pixels[x, y] in colorset:
                pixels[x, y] = closest_color(pixels[x, y], colorset)


def crop_to_colors(image, colorset, ignore_first=True):
    color_list = colorset[1:] if ignore_first else colorset
    borders = {color: {c: 0 for c in ['xleft', 'xright', 'yupper', 'ylower']} for color in colorset}

    width, height = image.size
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            color = pixels[x, y]
            borders[color]['xleft'] = borders[color]['xleft'] or x
            borders[color]['xright'] = x
            borders[color]['yupper'] = min(y, borders[color]['yupper'])
            borders[color]['ylower'] = max(y, borders[color]['ylower'])

    for color in color_list:
        border = borders[color]
        color_image = image.crop((border['xleft'], border['yupper'], border['xright'], border['ylower']))
        color_image.load()
        color_image.save('{}.png'.format(color))
        yield color_image


def solve_captcha(filename='captcha.png'):
    captcha = Image.open(filename)
    result = []

    top_colors = get_top_colors(captcha, amount=NUMS+1)
    reduce_to_colorset(captcha, top_colors)

    for letter in crop_to_colors(captcha, top_colors):
        pass

    captcha.save('output.png')
    return result


if __name__ == '__main__':
    solve_captcha()
