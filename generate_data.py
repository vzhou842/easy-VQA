from shape import Shape
from color import Color
from images import createImage
from random import choice

colors = list(Color)
shaspes = list(Shape)

createImage('rectangle', Shape.RECTANGLE, choice(colors))
createImage('circle', Shape.CIRCLE, choice(colors))
createImage('triangle', Shape.TRIANGLE, choice(colors))
