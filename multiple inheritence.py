class shape:
  def __init__(self, sides):
    self.sides = sides

  def numberOfSides(self):
    print(f"{self.sides}")

class color:
  def __init__(self, color):
    self.color = color

  def colorer(self):
    print(f"{self.color}")

def child(shape, color):
  def __init__(self, sides, color):
    shape.__init__(self, sides)
    color.__init__(self, color)

  def about(self):
    print(f"i have {self.numberOfSides()} sides with color {self.colorer}")
