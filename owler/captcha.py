from operator import itemgetter

from PIL import Image


NUMS = 5


def closest_color(color, colors):
    red, green, blue = color
    distances = [(r - red, g - green, b - blue) for r, g, b in colors]
    distances = [sum((r**2, g**2, b**2)) for r, g, b in distances]
    color_index, _ = min((val, index) for val, index in enumerate(distances))
    return colors[color_index]


captcha = Image.open('captcha.png')
pixels = captcha.load()
width, height = captcha.size

histogram = captcha.getcolors(width * height)
top = sorted(histogram, key=itemgetter(0), reverse=True)[:NUMS + 1]
top_colors = [color for amount, color in top]
background = top_colors[0]

for x in range(width):
    for y in range(height):
        if not pixels[x, y] in top_colors:
            pixels[x, y] = closest_color(pixels[x, y], top_colors)

for letter in range(1, NUMS + 1):
    """ get slice borders and images """

captcha.save('output.png')
