class Shape:
    """Super class so SVG objects can set their attributes."""
    def __init__(self):
        self.attrs = {}

    def fill(self, fillColor):
        """Set fill style"""
        self.attrs["fill"] = fillColor
        return self

    def stroke(self, strokeColor):
        """Set stroke style"""
        self.attrs["stroke"] = strokeColor
        return self

    def strokeWidth(self, strokeWidth):
        """Set stroke width in px"""
        self.attrs["stroke-width"] = strokeWidth
        return self

    def opacity(self, opacity):
        """Set the opacity of the object. Number between 0 and 1.0"""
        self.attrs["opacity"] = opacity

    def filter(self, filt):
        """Add a filter to the object"""
        self.attrs["filter"] = filt

    def addAttribute(self, attrName, attrValue):
        """Add a generic attribute to the object."""
        self.attrs[attrName] = attrValue
        return self

    def props(self):
        """Render a collection of attributes"""
        return " ".join([f'{k}="{v}"' for k, v in self.attrs.items()])
