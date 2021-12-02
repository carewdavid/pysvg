import math
import numpy as np
import util

class Polygon:
    def __init__(self, center, sides, scale, angle=0):
        self.pos = center
        self.sides = sides
        self.scale = scale
        self.rot = angle

    def rotate(self, theta):
        self.rot = theta

    def computeVertices(self):
        vertices = []
        for i in range(self.sides):
            vertex = util.fromAngle((math.tau / self.sides) * i + self.rot) * self.scale
            vertex += self.pos
            vertices.append(vertex)
        return vertices

    def edges(self):
        e = []
        v = self.computeVertices()
        for i in range(len(v)):
            e.append((v[i], v[(i+1) % len(v)]))
        return e

    def intersects(self, other):
        
        return True

    def hatch(self, lines, angle):

        radius = math.sqrt(2 * math.pow(self.scale, 2))
        box = Polygon(self.pos, 4, radius)
        box.rotate(angle)
        corners = box.computeVertices()
        hatches = []


        for i in range(1, lines + 1):
            frac = i / lines
            start = util.lerp(corners[0], corners[1], frac)
            end = util.lerp(corners[3], corners[2], frac)
            hits = []
            vertices = self.computeVertices()
            for k in range(len(vertices)):
                a = vertices[k]
                b = vertices[(k + 1) % len(vertices)]
                cross = util.segmentIntersect(start, end, a, b)
                if cross is not None:
                    hits.append(cross)
            #hits.sort(key=lambda p: util.dist(start, p))
            if len(hits) > 2:
                #print(hits)
                del hits[0]
            if len(hits) > 1:
                hatches.append([hits[0], hits[1]])
        return hatches


    def draw(self, ctx):
        vertices = self.computeVertices()
        path = ctx.path(*vertices[0])
        for x, y in vertices:
            path.lineTo(x, y)
        path.close()
        return path

    def draw_hatched(self, ctx, density, angle=None):
        if angle is None:
            angle = self.rot
        lines = self.hatch(density, angle)
        for start, end in lines:
            ctx.line(*start, *end).stroke('black')