class Filter:
    def __init__(self, id):
        self.id = id
        self.primitives = []

    def blur(self, stdDev):
        primitive = f'<feGaussianBlur stdDeviation="{stdDev}"/>'
        self.primitives.append(primitive)
        return self

    def use(self):
        return f'url(#{self.id})'

    def draw(self, output):
        components = "".join(self.primitives)
        output.write(f'<filter id="{self.id}"> {components} </filter>')

