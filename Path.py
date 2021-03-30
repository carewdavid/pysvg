class Path:
    def __init__(self, x, y):
       self.commands = [] 
       self.moveTo(x, y)

    def move(self, x, y):
        """Move relative to the last point"""
        self.commands.append(f'm {x} {y}')
        return self

    def moveTo(self, x, y):
        """Move to the given point"""
        self.commands.append(f'M {x} {y}')
        return self

    def line(self, x, y):
        """Draw a line relative to the last point"""
        self.commands.append(f'l {x} {y}')
        return self

    def lineTo(self, x, y):
        """Draw a line to the given point"""
        self.commands.append(f'L {x} {y}')
        return self

    def curve(self, cx, cy, x, y):
        """Draw a quadratic curve relative to the last point"""
        self.commands.append(f'q {cx} {cy} {x} {y}')
        return self

    def curveTo(self, cx, cy, x, y):
        """Draw a quadratic curve to (x,y) with control point (cx,cy)"""
        self.commands.append(f'Q {cx} {cy} {x} {y}')
        return self

    def bezier(self, cx, cy, cx2, cy2, x, y):
        """Draw a cubic curve relative to the last point"""
        self.commands.append(f'c {cx} {cy} {cx2} {cy2} {x} {y}')
        return self

    def bezier(self, cx, cy, cx2, cy2, x, y):
        """Draw a cubic curve to (x,y) with control points (cx,cy) and (cx2,cy2)"""
        self.commands.append(f'C {cx} {cy} {cx2} {cy2} {x} {y}')
        return self

    def draw(self):
        data = "".join(self.commands)
        print(f'<path d="{data}"/>')
    
