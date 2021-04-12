import sys
from . import Circle
from . import Rect
from . import Ellipse
from . import Line
from . import Path

class SVG:
    def __init__(self, width, height, output=sys.stdout):

        self.width = width
        self.height = height
        self.objs = []
        self.output = output

    def circle(self, x, y, radius):
        circ = Circle.Circle(x, y, radius)
        self.objs.append(circ)
        return circ

    def rect(self, x, y, w, h):
        rect = Rectangle.Rectangle(x, y, w, h)
        self.objs.append(rect)
        return rect

    def ellipse(self, x, y, rx, ry):
        ell = Ellipse.Ellipse(x, y, rx, ry)
        self.objs.append(ell)
        return ell

    def line(self, sx, sy, ex, ey):
        line = Line.Line(sx, sy, ex, ey)
        self.objs.append(line)
        return line

    def path(self, x, y):
        path = Path.Path(x, y)
        self.objs.append(path)
        return path

    def group(self, name=None):
        group = Group(name)
        self.objs.append(group)
        return group

    def draw(self):
        self.output.write('<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}">'.format(self.width, self.height))
        for object in self.objs:
            object.draw(self.output)
        self.output.write('</svg>')

class Group(SVG):
    def __init__(self, name=None):
        self.objs = []

        if name:
            self.name = name
        else:
            name = ''

    def draw(self, output):
        output.write(f'<g id="{self.name}">')
        for object in self.objs:
            object.draw(output)
        output.write('</g>')
