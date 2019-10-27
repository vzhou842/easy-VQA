from shape import Shape
from color import Color
from images import createImage
from questions import createQuestions
from random import choice

colors = list(Color)
shapes = list(Shape)

allQuestions = []

for i in range(10):
  shape = choice(shapes)
  color = choice(colors)

  createImage(i, shape, color)

  questions = map(lambda x: x + (i,), createQuestions(shape, color))
  allQuestions += questions

print(allQuestions)
