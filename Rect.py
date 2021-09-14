from . import Shape

class Rect(Shape.Shape):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, output):
        output.write(f'<rect x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" {self.props()}/>')

