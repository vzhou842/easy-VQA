from shape import Shape
from color import Color
from images import create_image
from questions import create_questions
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

def create_data(image_path, num):
  qs = []
  for i in range(num):
    shape = choice(shapes)
    color = choice(colors)

    create_image(f'{image_path}/{i}.png', shape, color)
    qs += create_questions(shape, color, i)
  return qs

train_questions = create_data('data/train/images', NUM_TRAIN)
test_questions = create_data('data/test/images', NUM_TEST)

all_questions = train_questions + test_questions
all_answers = list(set(map(lambda q: q[1], all_questions)))

with open('data/train/questions.json', 'w') as file:
  json.dump(train_questions, file)
with open('data/test/questions.json', 'w') as file:
  json.dump(test_questions, file)

with open('data/answers.txt', 'w') as file:
  for answer in all_answers:
    file.write(f'{answer}\n')

print(f'Generated {NUM_TRAIN} train images and {len(train_questions)} train questions.')
print(f'Generated {NUM_TEST} test images and {len(test_questions)} test questions.')
print(f'{len(all_answers)} total possible answers.')
