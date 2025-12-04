"""
Problem definition here
"""

import click
echo = click.echo

@click.group()
def day3():
    """Solves Day 3's problems"""

@day3.command()
@click.argument("input", type=click.File("r"))
def part1(input):
    """Solves part 1"""

    total = 0
    for line in input.read().splitlines():
        # For each line:
        # Find the highest digit in any but the last position (first instance)
        # Then find the highest digit right of that digit
        highest = "0"
        highest_pos = -1
        for pos, char in enumerate(line[:-1]):
            if char > highest:
                highest = char
                highest_pos = pos
        next_highest = "0"
        for char in line[highest_pos+1:]:
            if char > next_highest:
                next_highest = char
        best_str = highest + next_highest
        best = int(best_str)
        total += best
    echo(total)

@day3.command()
@click.argument("input", type=click.File("r"))
def part2(input):
    """Solves part 2"""

# When invoked as a script, do this
if __name__ == '__main__':
    day3()