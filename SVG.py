from . import Circle

class SVG:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objs = []

    def circle(self, x, y, radius):
        circ = Circle.Circle(x, y, radius)
        self.objs.append(circ)

    def draw(self):
        print('<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}">'.format(self.width, self.height))
        for object in self.objs:
            object.draw()
        print('</svg>')
