from PIL import Image, ImageDraw
from random import randint
from shape import Shape
import math

IM_SIZE = 64

MIN_SHAPE_SIZE = 5
MAX_SHAPE_SIZE = IM_SIZE / 2

def createImage(filename, shape, color):
  r = randint(230, 255)
  g = randint(230, 255)
  b = randint(230, 255)
  im = Image.new('RGB', (IM_SIZE, IM_SIZE), (r, g, b))

  draw = ImageDraw.Draw(im)
  drawShape(draw, shape, color)
  del draw

  im.save(f'images/{filename}.png', 'png')

def drawShape(draw, shape, color):
  if shape is Shape.RECTANGLE:
    w = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    h = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    x = randint(w, IM_SIZE - w)
    y = randint(h, IM_SIZE - h)
    draw.rectangle([(x, y), (x + w, y + h)], fill=color.value)

  elif shape is Shape.CIRCLE:
    r = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    x = randint(r, IM_SIZE - r)
    y = randint(r, IM_SIZE - r)
    draw.ellipse([(x, y), (x + r, y + r)], fill=color.value)

  elif shape is Shape.TRIANGLE:
    angle = math.radians(randint(0, 359))
    angle2 = angle + math.pi / 3
    s = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
    x = randint(s, IM_SIZE - s)
    y = randint(s, IM_SIZE - s)
    draw.polygon([
      (x, y),
      (x + s * math.cos(angle), y + s * math.sin(angle)),
      (x + s * math.cos(angle2), y + s * math.sin(angle2)),
    ], fill=color.value)

  else:
    raise Exception('Invalid shape!')
