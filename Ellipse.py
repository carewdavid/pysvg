from . import Shape
class Ellipse(Shape.Shape):
    def __init__(self, x, y, minorRadius, majorRadius):
        super().__init__()
        self.x = x
        self.y = y
        self.minR = minorRadius
        self.majR = majorRadius
        self.fill = 'none'
        self.stroke = 'black'

    def draw(self, output):
        output.write(f'<ellipse cx="{self.x:.3f}" cy="{self.y:.3f}" rx="{self.minR:.3f}" ry="{self.majR:.3f}" {self.props()} />')
