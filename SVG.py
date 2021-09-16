import sys
from . import Circle
from . import Rect
from . import Ellipse
from . import Line
from . import Path
from . import Filter

INCH = 96
FOOT = INCH * 12
MILE = FOOT * 5280
CENTIMETER = 37.795
MILLIMETER = CENTIMETER * .1
METER = CENTIMETER * 100
KILOMETER = METER * 1000

LETTER = (8.5 * INCH, 11 * INCH)
POSTCARD = (4 * INCH, 6 * INCH)
A4 = (21 * CENTIMETER, 29.7 * CENTIMETER)
A3 = (29.7 * CENTIMETER, 42 * CENTIMETER)

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
        rect = Rect.Rect(x, y, w, h)
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

    def filter(self, name):
        filt = Filter.Filter(name)
        self.objs.append(filt)
        return filt

    def draw(self, out=None):
        output = out or self.output
        output.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="{}" height="{}">'.format(self.width, self.height))
        for object in self.objs:
            object.draw(output)
        output.write('</svg>')

class Group(SVG):
    def __init__(self, name=None):
        self.objs = []
        self.attrs = {}

        if name:
            self.name = name
        else:
            name = ''

    def scale(self, x, y=None):
        if y is None:
            y = x
        self.attrs["transform"] = f'{self.attrs.get("transform", "")} scale({x}, {y})'
        return self

    def translate(self, x, y=0):
        self.attrs["transform"] = f'{self.attrs.get("transform", "")} translate({x}, {y})'
        return self

    def rotate(self, angle, x=0, y=0):
        self.attrs["transform"] = f'{self.attrs.get("transform", "")} rotate({a}, {x}, {y})'
        return self

    def props(self):
        #Is it time to just extend Shape yet?
        return " ".join([f'{attribute}="{value}"' for attribute, value in self.attrs.items()])

    def draw(self, output):
        output.write(f'<g inkscape:groupmode="layer" inkscape:label="{self.name}" id="{self.name}" {self.props()}>')
        for object in self.objs:
            object.draw(output)
        output.write('</g>')
