from . import Shape

class Circle(Shape.Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.fill = 'none'
        self.stroke = 'black'

    def draw(self, output):
       output.write('<circle cx="{}" cy="{}" r="{}" {}/>'.format(self.x, self.y, self.radius, self.props()))
