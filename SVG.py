from . import Circle
from . import Rect
from . import Ellipse
from . import Line

class SVG:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objs = []

    def circle(self, x, y, radius):
        circ = Circle.Circle(x, y, radius)
        self.objs.append(circ)

    def rect(self, x, y, w, h):
        rect = Rectangle.Rectangle(x, y, w, h)
        self.objs.append(rect)
        return rect

    def Ellipse(self, x, y, rx, ry):
        ell = Ellipse.Ellipse(x, y, rx, ry)
        self.objs.append(ell)
        return ell

    def Line(self, sx, sy, ex, ey):
        line = Line.Line(sx, sy, ex, ey)
        self.objs.append(line)
        return line

    def draw(self):
        print('<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}">'.format(self.width, self.height))
        for object in self.objs:
            object.draw()
        print('</svg>')
