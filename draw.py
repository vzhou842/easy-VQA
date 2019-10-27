from PIL import Image, ImageDraw
from random import randint

IM_SIZE = 64

MIN_SHAPE_SIZE = 5

def createRectangleImage(filename):
  im = Image.new('RGBA', (IM_SIZE, IM_SIZE), (255, 255, 255, 255))

  draw = ImageDraw.Draw(im)

  x = randint(0, IM_SIZE / 2)
  y = randint(0, IM_SIZE / 2)
  w = randint(MIN_SHAPE_SIZE, IM_SIZE / 2)
  h = randint(MIN_SHAPE_SIZE, IM_SIZE / 2)
  draw.rectangle([(x, y), (x + w, y + h)], fill=(255, 0, 0))

  del draw
  im.save(filename, 'PNG')


def createCircleImage(filename):
  im = Image.new('RGBA', (IM_SIZE, IM_SIZE), (255, 255, 255, 255))

  draw = ImageDraw.Draw(im)

  x = randint(0, IM_SIZE / 2)
  y = randint(0, IM_SIZE / 2)
  r = randint(MIN_SHAPE_SIZE, IM_SIZE / 2 - 1)
  draw.ellipse([(x, y), (x + r, y + r)], fill=(255, 0, 0))

  del draw
  im.save(filename, 'PNG')


createRectangleImage('rectangle.png')
createCircleImage('circle.png')