from os import uname
import numpy as np
import math
import time
import random

def length(vec):
    return math.sqrt(np.sum(vec ** 2))

def norm(vec):
    len = length(vec)
    if len == 0:
        return vec / .000001
    return vec / len

def angle(vec):
    dir = norm(vec)
    return math.atan2(dir[1], dir[0]) + math.pi

def rotate(vec, theta, center=[0,0]):
    vec -= np.array(center)
    mat = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    #'@' does matrix multiplication
    v = vec @ mat
    return v + center

def fromAngle(theta):
    return np.array([math.cos(theta), math.sin(theta)])

def lerp(a, b, frac):
    return a + frac * (b - a)

def dist(a, b):
    return length(b - a)

def map(x, a, b, c, d):
    """Map x from the range (a, b) to (c, d)"""
    return ((x - a) / (b - a)) * (d - c) + c

def clamp(x, lower, upper):
    return max(lower, min(x, upper))

def randomPoint(xmin, xmax, ymin, ymax):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)
    return np.array([x, y])
    
def timestamp_name(prefix, suffix=None):
    t = time.localtime()
    return f'{prefix}_{t.tm_mday}{t.tm_hour}{t.tm_min}{t.tm_sec}_{suffix}.svg'
    
def intersectionTest(a, b, c, d):
    """Find the intersection point between line segments ab and cd, or None if it doesn't exist"""
    denominator = np.linalg.det(np.array([a - b, c - d]).transpose())
    if denominator == 0:
        return None
    t_nominator = np.array([a - c, c - d]).transpose()
    u_nominator = np.array([b - a, a - c]).transpose()

    t = np.linalg.det(t_nominator) / denominator
    u = np.linalg.det(u_nominator) / denominator

    return (t, u)


def segmentIntersect(a, b, c, d):
    point = intersectionTest(a, b, c, d)
    if point is None:
        return None
    t, u = point
    if t >= 0 and t <= 1 and u >= 0 and u <= 1:
        return c + u * (d - c)
    else:
        return None

def rayIntersect(origin, dir, a, b):
    p = intersectionTest(a, b, origin, origin + dir)
    if p is None:
        return None
    t, u = p
    if t >= 0 and t <= 1 and u > 0:
        return a + t * (b - a)
    else:
        return None

def dashLine(start, end, dashLen, gapLen):
    curr = start.copy()
    direction = norm(end - start)
    dash = direction * dashLen
    gap = direction * gapLen
    maxLength = dist(start, end)

    length = 0
    segments = []
    while length <= maxLength:
        segments.append((curr.copy(), curr + dash))
        curr += dash
        length += dashLen
        curr += gap
        length += gapLen
    return segments