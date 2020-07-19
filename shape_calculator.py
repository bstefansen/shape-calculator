import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height

  def set_width(self, newWidth):
    self.width = newWidth

  def set_height(self, newHeight):
    self.height = newHeight

  def get_perimeter(self):
    return ((self.width * 2) + (self.height * 2))

  def get_diagonal(self):
    return ((self.width**2 + self.height**2) ** 0.5)

  def get_amount_inside(self, shape):
    newShapeArea = shape.get_area()
    shapeArea = self.get_area()
    return math.floor(shapeArea/newShapeArea)

  def get_picture(self):
    pictureString = ''
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        pictureString += "*" * self.width + '\n'
      return pictureString

  def __repr__(self):
    return "Rectangle(width=%s, height=%s)" % (self.width, self.height)

class Square(Rectangle):

  def __init__(self, sideLength):
    self.sideLength = sideLength

  def get_area(self):
    return self.sideLength**2

  def set_side(self, newSide):
    self.sideLength = newSide

  def set_width(self, newWidth):
    self.sideLength = newWidth

  def get_perimeter(self):
    return (self.sideLength*4)

  def get_diagonal(self):
    return ((self.sideLength**2 + self.sideLength**2) ** 0.5)

  def get_picture(self):
    pictureString = ''
    if self.sideLength > 50:
      return "Too big for picture."
    else:
      for i in range(self.sideLength):
        pictureString += "*" * self.sideLength + '\n'
      return pictureString

  def __repr__(self):
    return "Square(side=%s)" % self.sideLength