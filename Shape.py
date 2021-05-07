class Shape:
    """Super class so SVG objects can set their attributes."""
    def __init__(self):
        self.attrs = {}

    def fill(self, fillColor):
        self.attrs["fill"] = fillColor

    def stroke(self, strokeColor):
        self.attrs["stroke"] = strokeColor

    def strokeWidth(self, strokeWidth):
        self.attrs["stroke-width"] = strokeWidth

    def props(self):
        return " ".join([f'{k}="{v}"' for k, v in self.attrs.items()])
