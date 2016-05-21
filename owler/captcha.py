from operator import itemgetter

from PIL import Image


NUMS = 5


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


def crop_to_colors(image, colorset):
    yield image


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
