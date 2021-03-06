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
        return self

    def filter(self, filt):
        """Add a filter to the object"""
        self.attrs["filter"] = filt
        return self

    def translate(self, dx, dy):
        """Translate the object by (dx, dy)"""
        self.attrs["transform"] = f'{self.attrs.get("transform", "")} translate({dx},{dy})'
        return self

    def scale(self, sx, sy=None):
        """Scale the object"""
        if sy is None:
            sy=sx
        self.attrs["transform"] = f'{self.attrs.get("transform", "")} scale({sx},{sy})'
        return self

    def rotate(self, angle, x=0, y=0):
        """Rotate the object `angle` radians around (x,y)"""
        self.attrs["transform"] = f'{self.attrs.get("transform", "")} rotate({180/3.1415926 * angle}, {x}, {y})'
        return self

    def addAttribute(self, attrName, attrValue):
        """Add a generic attribute to the object."""
        self.attrs[attrName] = attrValue
        return self

    def props(self):
        """Render a collection of attributes"""
        return " ".join([f'{k}="{v}"' for k, v in self.attrs.items()])
