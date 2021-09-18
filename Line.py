from . import Shape

class Line(Shape.Shape):
    def __init__(self, startX, startY, endX, endY):
        super().__init__()
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.stroke('black')

    def draw(self, output):
        output.write(f'<line x1="{self.startX:.3f}" y1="{self.startY:.3f}" x2="{self.endX:.3f}" y2="{self.endY:.3f}" {self.props()} />')
