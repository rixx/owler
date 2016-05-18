import math
from operator import itemgetter
import sys

from PIL import Image


NUMS = 5


def closest(top, color):
    ri, gi, bi = color
    distances = [(ro - ri, go - gi, bo - bi) for ro, go, bo in top]
    distances = [sum((r**2, g**2, b**2)) for r,g,b in distances]
    index, closest = min((val, index) for val, index in enumerate(distances))
    return top[index]


im = Image.open('captcha.png')
w, h = im.size
histogram = sorted(im.getcolors(w*h), key=itemgetter(0), reverse=True)[:NUMS+1]
top = [color for amount, color in histogram]
background = histogram[0][1]

pix = im.load()
for x in range(w):
    for y in range(h):
        if not pix[x,y] in top:
            pix[x,y] = closest(top, pix[x,y])

im.save('output.png')
