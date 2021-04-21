from . import Shape

class Rect(Shape.Shape):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, output):
        output.write('<rect x="{}" y="{}" width="{}" height="{}" {}/>'.format(self.x, self.y, self.w, self.h, self.props()))

