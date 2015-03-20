# coding: utf-8
from PIL import Image, ImageFont, ImageDraw
import random

num = random.randint(0, 200)
img = Image.open("0000.jpg")
img = img.resize((256, 256))
draw = ImageDraw.Draw(img)
# Draw red circle
draw.point([224, 32], "Red")
for ind in range(0, 32):
    draw.arc([223 - ind, 31 - ind, 225 + ind, 33 + ind], 0, 360, 'Red')
# add number of text    
number_font = ImageFont.truetype('Georgia.TTF', 42)
if num > 99:
    draw.text((208, 2), "...", font=number_font)
elif num < 10:
    draw.text((214, 3), str(num), font=number_font)
else:
    draw.text((204, 3), str(num), font=number_font)
img.save('0000-out3.png')
