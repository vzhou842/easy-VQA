from PIL import Image, ImageDraw
from random import randint

IM_SIZE = 64

MIN_RECTANGLE_SIZE = 5

def createRectangleImage(filename):
  # Initialize a blank white image
  im = Image.new('RGBA', (IM_SIZE, IM_SIZE), (255, 255, 255, 255))

  draw = ImageDraw.Draw(im)

  x = randint(0, IM_SIZE / 2)
  y = randint(0, IM_SIZE / 2)
  w = randint(MIN_RECTANGLE_SIZE, IM_SIZE / 2)
  h = randint(MIN_RECTANGLE_SIZE, IM_SIZE / 2)
  draw.rectangle([(x, y), (x + w, y + h)], fill=(255, 0, 0))

  del draw

  # write to stdout
  im.save(filename, 'PNG')

createRectangleImage('test.png')
