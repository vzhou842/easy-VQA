from shape import Shape
from color import Color
from images import createImage
from questions import createQuestions
from random import choice
import json

colors = list(Color)
shapes = list(Shape)

allQuestions = []

NUM_IMAGES = 10

for i in range(NUM_IMAGES):
  shape = choice(shapes)
  color = choice(colors)

  createImage(i, shape, color)

  questions = list(map(lambda x: x + (i,), createQuestions(shape, color)))
  allQuestions += questions

with open('data/questions.json', 'w') as file:
  json.dump(questions, file)

print(f'Generated {NUM_IMAGES} images and {len(allQuestions)} questions.')
