"""
Problem definition here
"""

from collections import namedtuple
import matplotlib.pyplot as plt
import itertools
import click
echo = click.echo

Point2 = namedtuple("Point2", "x y")

def line_to_point(line):
    x, y = line.split(",")
    return Point2(int(x), int(y))

def area(a: Point2, b: Point2):
    d_x = abs(a.x - b.x) + 1
    d_y = abs(a.y - b.y) + 1
    return d_x * d_y

def visualize(points):
    fig = plt.figure()
    ax = fig.add_subplot(projection='2d')
    data = list(itertools.zip_longest(*points))
    ax.scatter(*data, marker=".")
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

    lines = input.read().splitlines()
    points = list(map(line_to_point, lines))

    visualize(points)
                  

# When invoked as a script, do this
if __name__ == '__main__':
    day9()