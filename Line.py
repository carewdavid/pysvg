class Line:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.stroke = 'black'
    def draw(self, output):
        output.write('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" />'.format(self.startX, self.startY, self.endX, self.endY, self.stroke))
