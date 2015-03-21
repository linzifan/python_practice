# coding: utf-8
from PIL import Image, ImageDraw, ImageFont
import random

__author__ = 'Zifan'

# generate the random code
txt = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 4)
# create image
fontSize = 50
width = int(fontSize * 1.5 * 4)
height = int(fontSize * 1.5)
image = Image.new('RGBA', (width, height), (255, 255, 255))
# start to draw
draw = ImageDraw.Draw(image)
# draw points
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill = (random.randint(0, 126), random.randint(0, 126), random.randint(0, 126)))
# draw text
for t in range(4):
    draw.text(((2.0*t+1)/8*width, height/10.0), txt[t],               font = ImageFont.truetype("Sinhala Sangam MN.ttc", random.randrange(45, 55)),                fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
# image.show()
image.save("validate.png")
