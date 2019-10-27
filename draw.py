from PIL import Image, ImageDraw
from random import randint
from enum import Enum
import math

IM_SIZE = 64

MIN_SHAPE_SIZE = 5
MAX_SHAPE_SIZE = IM_SIZE / 2

class Shape(Enum):
  RECTANGLE = 1
  CIRCLE = 2
  TRIANGLE = 3

def createImage(filename, shape):
  im = Image.new('RGBA', (IM_SIZE, IM_SIZE), (255, 255, 255, 255))

  draw = ImageDraw.Draw(im)
  drawShape(draw, shape)
  del draw

  im.save(filename, 'png')


def drawShape(draw, shape):
  x = randint(0, IM_SIZE / 2)
  y = randint(0, IM_SIZE / 2)

  if shape is Shape.RECTANGLE:
    w = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    h = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    draw.rectangle([(x, y), (x + w, y + h)], fill=(255, 0, 0))

  elif shape is Shape.CIRCLE:
    r = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    draw.ellipse([(x, y), (x + r, y + r)], fill=(255, 0, 0))

  elif shape is Shape.TRIANGLE:
    angle = math.radians(randint(0, 359))
    angle2 = angle + math.pi / 3
    s = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    draw.polygon([
      (x, y),
      (x + s * math.cos(angle), y + s * math.sin(angle)),
      (x + s * math.cos(angle2), y + s * math.sin(angle2)),
    ], fill=(255, 0, 0))


  else:
    raise Exception('Invalid shape!')

createImage('rectangle.png', Shape.RECTANGLE)
createImage('circle.png', Shape.CIRCLE)
createImage('triangle.png', Shape.TRIANGLE)
