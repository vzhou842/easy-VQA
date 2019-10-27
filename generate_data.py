from shape import Shape
from color import Color
from images import createImage
from questions import createQuestions
from random import choice
import json
import os

if not os.path.exists('data/train/images'):
  os.makedirs('data/train/images/')
if not os.path.exists('data/test/images'):
  os.makedirs('data/test/images/')

colors = list(Color)
shapes = list(Shape)

NUM_TRAIN = 800
NUM_TEST = 200

trainQuestions = []
testQuestions = []

for i in range(NUM_TRAIN):
  shape = choice(shapes)
  color = choice(colors)

  createImage(f'data/train/images/{i}.png', shape, color)
  trainQuestions += createQuestions(shape, color, i)

for i in range(NUM_TEST):
  shape = choice(shapes)
  color = choice(colors)

  createImage(f'data/test/images/{i}.png', shape, color)
  testQuestions += createQuestions(shape, color, i)

with open('data/train/questions.json', 'w') as file:
  json.dump(trainQuestions, file)
with open('data/test/questions.json', 'w') as file:
  json.dump(testQuestions, file)

print(f'Generated {NUM_TRAIN} train images and {len(trainQuestions)} train questions.')
print(f'Generated {NUM_TEST} test images and {len(testQuestions)} test questions.')
