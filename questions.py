from shape import Shape
from color import Color
from random import getrandbits, randint

def create_questions(shape, color, image_id):
  shape_name = shape.name.lower()
  color_name = color.name.lower()

  questions = [
    (f'what shape is in the image?', shape_name),
    (f'what is the {color_name} shape?', shape_name),
    (f'what color is the {shape_name}?', color_name),
    (f'what color is the shape?', color_name),
  ]

  yes_no_questions = []

  for s in Shape:
    yes_no_questions.append((f'is there a {s.name.lower()} in the image?', 'yes' if s is shape else 'no'))
    yes_no_questions.append((f'is there not a {s.name.lower()} in the image?', 'no' if s is shape else 'yes'))

  for c in Color:
    yes_no_questions.append((f'is there a {c.name.lower()} shape in the image?', 'yes' if c is color else 'no'))
    yes_no_questions.append((f'is there not a {c.name.lower()} shape in the image?', 'no' if c is color else 'yes'))

  questions = list(filter(lambda _: bool(getrandbits(1)), questions))
  yes_no_questions = list(filter(lambda _: randint(0, 4) is 0, yes_no_questions))

  all_questions = questions + yes_no_questions
  return list(map(lambda x: x + (image_id,), all_questions))
