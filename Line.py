class Line:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.stroke = 'black'
    def draw(self):
        print('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" />')
