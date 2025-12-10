"""
Problem definition here
"""

from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np
import itertools
import click
echo = click.echo

Point2 = namedtuple("Point2", "x y")

class Rect:
    ul: Point2
    lr: Point2
    def __init__(self, a: Point2, b: Point2):
        x_min = min(a.x, b.x)
        x_max = max(a.x, b.x)
        y_min = min(a.y, b.y)
        y_max = max(a.y, b.y)
        self.ul = Point2(x_min, y_min)
        self.lr = Point2(x_max, y_max)

    def contains(self, p: Point2):
        return p.x > self.ul.x and p.x < self.lr.x and p.y > self.ul.y and p.y < self.lr.y
    
    def crossed_by(self, a: Point2, b: Point2):
        if a.x == b.x:
            x = a.x
            min_y = min(a.y, b.y)
            max_y = max(a.y, b.y)
            # X strictly between, y outside(inclusive)
            return x > self.ul.x and x < self.lr.x and min_y <= self.ul.y and max_y >= self.lr.y
        elif a.y == b.y:
            y = a.y
            min_x = min(a.x, b.x)
            max_x = max(a.x, b.x)
            # Y strictly between, x outside(inclusive)
            return y > self.ul.y and y < self.lr.y and min_x <= self.ul.x and max_x >= self.lr.x
        else:
            raise ValueError("Pairs should be collinear")
    
    def area(self):
        return area(self.ul, self.lr)

def line_to_point(line):
    x, y = line.split(",")
    return Point2(int(x), int(y))

def line_to_array(line):
    x, y = line.split(",")
    return [int(x), int(y)]

def area(a: Point2, b: Point2):
    d_x = abs(a.x - b.x) + 1
    d_y = abs(a.y - b.y) + 1
    return d_x * d_y

def visualize(points):
    fig = plt.figure()
    ax = fig.add_subplot()
    data = list(itertools.zip_longest(*points))
    ax.scatter(*data, marker=".")
    pairs = list(itertools.pairwise(points))
    # Close the loop
    pairs.append((points[-1], points[0]))
    for a, b in pairs:
        ax.plot((a.x, b.x), (a.y, b.y))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()

@click.group()
def day9():
    """Solves Day 9's problems"""

@day9.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    lines = input.read().splitlines()
    points = set(map(line_to_point, lines))

    pairs = set(itertools.combinations(points, 2))

    best_area = 0
    for a, b in pairs:
        a = area(a, b)
        if a > best_area:
            best_area = a

    echo(best_area)


@day9.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

    # Look at all possible pairwise rectangles
    # If the rectangle is bigger than the best we've seen, is it valid?
    # A rectangle is invalid if:
    #   It contains a red point that is not on its perimeter
    #   Any line segment fully bisects it

    lines = input.read().splitlines()
    points = list(map(line_to_point, lines))
    echo(points)

    pairs = set(itertools.combinations(points, 2))
    segments = list(itertools.pairwise(points))
    # Close the loop
    segments.append((points[-1], points[0]))

    def is_valid(r: Rect):
        contained = list(filter(lambda p : r.contains(p), points))
        if contained:
            return False
        crossed = list(filter(lambda s : r.crossed_by(*s), segments))
        if crossed:
            return False
        return True

    best_area = 0
    best_rect = Rect(Point2(0,0), Point2(0,0))
    for a, b in pairs:
        r = Rect(a, b)
        if r.area() > best_area and is_valid(r):
            best_area = r.area()
            best_rect = r

    echo(best_area)
    # x_max = max(points, key=lambda p : p.x).x
    # y_max = max(points, key=lambda p : p.y).y
    # echo(x_max)
    # echo(y_max)
    # # points = np.array([seq], np.int32)
    # image = np.ndarray((x_max, y_max), np.int8)

    # echo(image)


    # visualize(points)
                  

# When invoked as a script, do this
if __name__ == '__main__':
    day9()