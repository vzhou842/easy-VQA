from shape import Shape
from color import Color
from random import getrandbits, randint

def createQuestions(shape, color, imageID):
  shapeName = shape.name.lower()
  colorName = color.name.lower()

  questions = [
    (f'what shape is in the image?', shapeName),
    (f'what is the {colorName} shape?', shapeName),
    (f'what color is the {shapeName}?', colorName),
    (f'what color is the shape?', colorName),
  ]

  yesNoQuestions = []

  for s in Shape:
    yesNoQuestions.append((f'is there a {s.name.lower()} in the image?', 'yes' if s is shape else 'no'))
    yesNoQuestions.append((f'is there not a {s.name.lower()} in the image?', 'no' if s is shape else 'yes'))

  for c in Color:
    yesNoQuestions.append((f'is there a {c.name.lower()} shape in the image?', 'yes' if c is color else 'no'))
    yesNoQuestions.append((f'is there not a {c.name.lower()} shape in the image?', 'no' if c is color else 'yes'))

  questions = list(filter(lambda _: bool(getrandbits(1)), questions))
  yesNoQuestions = list(filter(lambda _: randint(0, 4) is 0, yesNoQuestions))

  allQuestions = questions + yesNoQuestions
  return list(map(lambda x: x + (imageID,), allQuestions))
