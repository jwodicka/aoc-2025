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

    total = 0
    for line in input.read().splitlines():
        # For each line:
        # Find the highest digit in any but the last 11 positions
        # Then find the highest 11 digits right of that digit
        total += int(find_biggest(line, 12))
    echo(total)

def find_biggest(line, n):
    highest = "0"
    highest_pos = -1
    working_line = line[:-(n-1)] if n > 1 else line
    # echo(str(n) + "  " + working_line)
    for pos, char in enumerate(working_line):
        if char > highest:
            highest = char
            highest_pos = pos
    if n == 1:
        return highest
    rest = find_biggest(line[highest_pos+1:], n-1)
    best = highest + rest
    return best


# When invoked as a script, do this
if __name__ == '__main__':
    day3()