class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fill = 'none'
        self.stroke = 'black'

    def draw(self, output):
        output.write('<rect x="{}" y="{}" width="{}" height="{}" fill="{}" stroke="{}"/>'.format(self.x, self.y, self.w, self.h, self.fill, self.stroke, self.strokeWidth))

