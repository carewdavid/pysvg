class Ellipse:
    def __init__(self, x, y, minorRadius, majorRadius):
        self.x = x
        self.y = y
        self.minR = minorRadius
        self.majR = majorRadius
        self.fill = 'none'
        self.stroke = 'black'

    def draw(self, output):
        output.write(f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.minR}" ry="{self.majR}" {self.props()} />')
