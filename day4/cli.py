"""
The forklifts can only access a roll of paper if there are fewer than four rolls
of paper in the eight adjacent positions.
"""

import itertools
import click
echo = click.echo

@click.group()
def day4():
    """Solves Day 4's problems"""

@day4.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    grid = parse_grid(input)
    height = len(grid)
    width = len(grid[0])

    directions=list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    directions.remove((0,0))

    def get_neighbors(row, col):
        result = []
        for r_delta, c_delta in directions:
            r = row + r_delta
            c = col + c_delta
            if (r < 0 or r >= height):
                continue
            if (c < 0 or c >= width):
                continue
            result.append(grid[r][c])
        return result
    
    accessible = []
    for r in range(0, height):
        for c in range(0, width):
            if grid[r][c] != "@":
                continue
            neighbors = get_neighbors(r, c)
            blocks = len(list(filter(lambda n: n == '@', neighbors)))

            if blocks < 4:
                accessible.append((r, c))

    echo(len(accessible))

@day4.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

    grid = parse_grid(input)
    height = len(grid)
    width = len(grid[0])

    directions=list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    directions.remove((0,0))

    def get_neighbors(row, col):
        result = []
        for r_delta, c_delta in directions:
            r = row + r_delta
            c = col + c_delta
            if (r < 0 or r >= height):
                continue
            if (c < 0 or c >= width):
                continue
            result.append(grid[r][c])
        return result
    
    def find_accessibles():
        accessible = []
        for r in range(0, height):
            for c in range(0, width):
                if grid[r][c] != "@":
                    continue
                neighbors = get_neighbors(r, c)
                blocks = len(list(filter(lambda n: n == '@', neighbors)))

                if blocks < 4:
                    accessible.append((r, c))
        return accessible
    
    accessibles = find_accessibles()
    total = 0
    while accessibles:
        # echo("Found " + str(len(accessibles)))
        total += len(accessibles)
        for r, c in accessibles:
            grid[r][c] = "."
        accessibles = find_accessibles()

    echo(total)

def parse_grid(input):
    lines = input.read().splitlines()
    return list(map(list, lines))

# When invoked as a script, do this
if __name__ == '__main__':
    day4()