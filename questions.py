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
    cur_shape_name = s.name.lower()
    yes_no_questions.append((f'is there a {cur_shape_name}?', 'yes' if s is shape else 'no'))
    yes_no_questions.append((f'is there a {cur_shape_name} in the image?', 'yes' if s is shape else 'no'))
    yes_no_questions.append((f'does the image contain a {cur_shape_name}?', 'yes' if s is shape else 'no'))
    yes_no_questions.append((f'is a {cur_shape_name} present?', 'yes' if s is shape else 'no'))

    yes_no_questions.append((f'is there not a {cur_shape_name}?', 'no' if s is shape else 'yes'))
    yes_no_questions.append((f'is there not a {cur_shape_name} in the image?', 'no' if s is shape else 'yes'))
    yes_no_questions.append((f'does the image not contain a {cur_shape_name}?', 'no' if s is shape else 'yes'))
    yes_no_questions.append((f'is no {cur_shape_name} present?', 'no' if s is shape else 'yes'))

  for c in Color:
    cur_color_name = c.name.lower()
    yes_no_questions.append((f'is there a {cur_color_name} shape?', 'yes' if c is color else 'no'))
    yes_no_questions.append((f'is there a {cur_color_name} shape in the image?', 'yes' if c is color else 'no'))
    yes_no_questions.append((f'does the image contain a {cur_color_name} shape?', 'yes' if c is color else 'no'))
    yes_no_questions.append((f'is a {cur_color_name} shape present?', 'yes' if c is color else 'no'))

    yes_no_questions.append((f'is there not a {cur_color_name} shape?', 'no' if c is color else 'yes'))
    yes_no_questions.append((f'is there not a {cur_color_name} shape in the image?', 'no' if c is color else 'yes'))
    yes_no_questions.append((f'does the image not contain a {cur_color_name} shape?', 'no' if c is color else 'yes'))
    yes_no_questions.append((f'is no {cur_color_name} shape present?', 'no' if c is color else 'yes'))

  questions = list(filter(lambda _: randint(0, 3) is 0, questions))
  yes_no_questions = list(filter(lambda _: randint(0, 23) is 0, yes_no_questions))

  all_questions = questions + yes_no_questions
  return (list(map(lambda x: x + (image_id,), all_questions)), len(yes_no_questions))
