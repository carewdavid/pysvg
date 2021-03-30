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

