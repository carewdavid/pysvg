class Ellipse:
    def __init__(self, x, y, minorRadius, majorRadius):
        self.x = x
        self.y = y
        self.minR = minorRadius
        self.majR = majorRadius
        self.fill = 'none'
        self.stroke = 'black'

    def draw(self, output):
        output.write('<ellipse cx="{}" cy="{}" rx="{}" ry="{}" fill="{}" stroke="{}"/>'.format(self.x, self.y, self.minR, self.majR, self.fill, self.stroke))
