"""
Problem definition here
"""

from collections import namedtuple
from functools import reduce
from operator import mul
from math import sqrt
from queue import PriorityQueue
import matplotlib.pyplot as plt
import itertools
import click
echo = click.echo


@click.group()
def day8():
    """Solves Day 8's problems"""


Point3 = namedtuple("Point3", "x y z")


def distance(a: Point3, b: Point3):
    x_d = a.x - b.x
    y_d = a.y - b.y
    z_d = a.z - b.z
    return sqrt(x_d * x_d + y_d * y_d + z_d * z_d)


def line_to_point(line):
    x, y, z = line.split(",")
    return Point3(int(x), int(y), int(z))


def visualize(points):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    data = list(itertools.zip_longest(*points))
    ax.scatter(*data, marker=".")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

@day8.command()
@click.argument("input", type=click.File("r"))
@click.option("--n", type=click.INT, default=10)
def part1(input, n):
    """Solves part 1"""

    lines = input.read().splitlines()
    points = set(map(line_to_point, lines))

    pairs = set(itertools.combinations(points, 2))
    
    queue = PriorityQueue()
    for pair in pairs:
        queue.put((distance(*pair), pair))

    groups_by_point = {}
    for point in points:
        groups_by_point[point] = frozenset([point])

    closest_n = []
    for _ in range (0, n):
        _, pair = queue.get()
        closest_n.append(pair)

    for a, b in closest_n:
        a_group = groups_by_point[a]
        b_group = groups_by_point[b]
        merged = a_group.union(b_group)
        for point in merged:
            groups_by_point[point] = merged

    final_groups = set(groups_by_point.values())
    # echo(len(final_groups))

    group_queue = PriorityQueue()
    for group in final_groups:
        group_queue.put((-len(group), group))

    biggest = []
    for _ in range(3):
        biggest.append(group_queue.get()[1])

    sizes = map(len, biggest)
    echo(reduce(mul, sizes))


@day8.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

    lines = input.read().splitlines()
    points = set(map(line_to_point, lines))

    pairs = set(itertools.combinations(points, 2))
    
    queue = PriorityQueue()
    for pair in pairs:
        queue.put((distance(*pair), pair))

    groups_by_point = {}
    for point in points:
        groups_by_point[point] = frozenset([point])
    groups = set(groups_by_point.values())

    def merge(a, b):
        a_group = groups_by_point[a]
        b_group = groups_by_point[b]
        if a_group == b_group:
            return False
        merged = a_group.union(b_group)
        for point in merged:
            groups_by_point[point] = merged
        groups.remove(a_group)
        groups.remove(b_group)
        groups.add(merged)
        return True

    pair = (None, None)
    while len(groups) > 1:
        dist, pair = queue.get()
        echo(dist)
        if merge(*pair):
            echo(pair)

        echo(sum(map(len, groups)))
    a, b = pair
    echo(a.x * b.x)
        


# When invoked as a script, do this
if __name__ == '__main__':
    day8()
