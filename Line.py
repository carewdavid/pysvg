from . import Shape

class Line(Shape.Shape):
    def __init__(self, startX, startY, endX, endY):
        super().__init__()
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def draw(self, output):
        output.write(f'<line x1="{self.startX}" y1="{self.startY}" x2="{self.endX}" y2="{self.endY}" {self.props()} />')
