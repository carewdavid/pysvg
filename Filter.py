class Filter:
    def __init__(self, id):
        self.id = id
        self.primitives = []

    def blur(self, stdDev):
        primitive = GaussianBlur(stdDev)
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
