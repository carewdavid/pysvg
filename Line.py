from . import Shape

class Line(Shape.Shape):
    def __init__(self, startX, startY, endX, endY):
        super().__init__()
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def draw(self, output):
        output.write('<line x1="{}" y1="{}" x2="{}" y2="{}" {} />'.format(self.startX, self.startY, self.endX, self.endY, self.props()))
