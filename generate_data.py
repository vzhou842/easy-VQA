from shape import Shape
from color import Color
from images import createImage
from questions import createQuestions
from random import choice

colors = list(Color)
shapes = list(Shape)

for i in range(10):
  shape = choice(shapes)
  color = choice(colors)
  createImage(i, shape, color)
  createQuestions(shape, color)
