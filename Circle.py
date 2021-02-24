class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.fill = 'none'
        self.stroke = 'black'

    def draw(self):
       print('<circle cx="{}" cy="{}" r="{}" stroke="{}" fill="{}"/>'.format(self.x, self.y, self.radius, self.stroke, self.fill) 
