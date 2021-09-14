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
        output.write(f'<circle cx="{self.x}" cy="{self.y}" r="{self.radius}" {self.props()}/>')
