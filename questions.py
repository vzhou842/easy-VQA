from shape import Shape
from color import Color
from random import randint

def create_questions(shape, color, image_id):
  shape_name = shape.name.lower()
  color_name = color.name.lower()

  questions = [
    (f'what shape is in the image?', shape_name),
    (f'what shape is present?', shape_name),
    (f'what shape does the image contain?', shape_name),
    (f'what is the {color_name} shape?', shape_name),

    (f'what color is the {shape_name}?', color_name),
    (f'what is the color of the {shape_name}?', color_name),
    (f'what color is the shape?', color_name),
    (f'what is the color of the shape?', color_name),
  ]

  yes_no_questions = []

  for s in Shape:
    yes_no_questions.append((f'is there a {shape_name} in the image?', 'yes' if s is shape else 'no'))
    yes_no_questions.append((f'does the image contain a {shape_name}?', 'yes' if s is shape else 'no'))
    yes_no_questions.append((f'is a {shape_name} present?', 'yes' if s is shape else 'no'))

    yes_no_questions.append((f'is there not a {shape_name} in the image?', 'no' if s is shape else 'yes'))
    yes_no_questions.append((f'does the image not contain a {shape_name}?', 'no' if s is shape else 'yes'))
    yes_no_questions.append((f'is no {shape_name} present?', 'no' if s is shape else 'yes'))

  for c in Color:
    yes_no_questions.append((f'is there a {color_name} shape in the image?', 'yes' if c is color else 'no'))
    yes_no_questions.append((f'does the image contain a {color_name} shape?', 'yes' if c is color else 'no'))
    yes_no_questions.append((f'is a {color_name} shape present?', 'yes' if c is color else 'no'))

    yes_no_questions.append((f'is there not a {color_name} shape in the image?', 'no' if c is color else 'yes'))
    yes_no_questions.append((f'does the image not contain a {color_name} shape?', 'no' if c is color else 'yes'))
    yes_no_questions.append((f'is no {color_name} shape present?', 'no' if c is color else 'yes'))

  questions = list(filter(lambda _: randint(0, 3) is 0, questions))
  yes_no_questions = list(filter(lambda _: randint(0, 14) is 0, yes_no_questions))

  all_questions = questions + yes_no_questions
  return (list(map(lambda x: x + (image_id,), all_questions)), len(yes_no_questions))
