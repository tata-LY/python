#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from PIL import Image
from PIL import ImageDraw

image = Image.open('C:/Users/Administrator/Desktop/1.jpg')
draw = ImageDraw.Draw(image)
draw.text((10, 10), 'lytest')
image.show()

