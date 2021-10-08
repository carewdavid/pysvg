class Filter:
    def __init__(self, id):
        self.id = id
        self.primitives = []

    def blur(self, stdDev):
        primitive = GaussianBlur(stdDev)
        self.primitives.append(primitive)
        return primitive

    def blend(self, mode):
        primitive = Blend(mode)
        self.primitives.append(primitive)
        return primitive

    def use(self):
        return f'url(#{self.id})'

    def draw(self, output):
        output.write(f'<filter id="{self.id}">')
        for primitive in self.primitives:
            primitive.draw(output)
        output.write('</filter>')

class GaussianBlur:
    def __init__(self, stdDev):
        self.stdDev = stdDev

    def draw(self, output):
        output.write(f'<feGaussianBlur stdDeviation="{self.stdDev}"/>')

class Blend:
    def __init__(self, mode, source1="SourceGraphic", source2="BackgroundImage"):
        """Blend source1 and source2
        mode must be one of 'normal', 'screen', 'multiply', 'darken'"""
        self.source1 = source1
        self.source2 = source2
        self.mode = mode

    def draw(self, output):
        output.write(f'<feBlend mode="{self.mode}" in="{self.source1}" in2="{self.source2}"/>')
