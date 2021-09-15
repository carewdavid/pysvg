from . import Shape

class Path(Shape.Shape):
    def __init__(self, x, y):
        super().__init__()
        self.stroke('black')
        self.fill('none')
        self.commands = [] 
        self.moveTo(x, y)

    def move(self, x, y):
        """Move relative to the last point"""
        self.commands.append(f'm {x:.3f} {y:.3f}')
        return self

    def moveTo(self, x, y):
        """Move to the given point"""
        self.commands.append(f'M {x:.3f} {y:.3f}')
        return self

    def line(self, x, y):
        """Draw a line relative to the last point"""
        self.commands.append(f'l {x:.3f} {y:.3f}')
        return self

    def lineTo(self, x, y):
        """Draw a line to the given point"""
        self.commands.append(f'L {x:.3f} {y:.3f}')
        return self

    def curve(self, cx, cy, x, y):
        """Draw a quadratic curve relative to the last point"""
        self.commands.append(f'q {cx:.3f} {cy:.3f} {x:.3f} {y:.3f}')
        return self

    def curveTo(self, cx, cy, x, y):
        """Draw a quadratic curve to (x,y) with control point (cx,cy)"""
        self.commands.append(f'Q {cx:.3f} {cy:.3f} {x:.3f} {y:.3f}')
        return self

    def bezier(self, cx, cy, cx2, cy2, x, y):
        """Draw a cubic curve relative to the last point"""
        self.commands.append(f'c {cx:.3f} {cy:.3f} {cx2:.3f} {cy2:.3f} {x:.3f} {y:.3f}')
        return self

    def bezierTo(self, cx, cy, cx2, cy2, x, y):
        """Draw a cubic curve to (x,y) with control points (cx,cy) and (cx2,cy2)"""
        self.commands.append(f'C {cx:.3f} {cy:.3f} {cx2:.3f} {cy2:.3f} {x:.3f} {y:.3f}')
        return self

    def close(self):
        """Draw a straight line back to the beginning of the path"""
        self.commands.append("Z")
        return self

    def draw(self, output):
        data = "".join(self.commands)
        output.write(f'<path {self.props()} d="{data}"/>')
    
