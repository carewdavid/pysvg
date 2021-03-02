import Circle

class SVG:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objs = []

    def draw(self):
        print('<svg xmlns="http://www.w3.org/svg/2000" width="{}" height="{}">'.format(self.width, self.height))
        for object in self.objs:
            object.draw()
        print('</svg>')
